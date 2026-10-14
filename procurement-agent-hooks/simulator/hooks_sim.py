"""Reference implementation of the hook workflow logic, run against data/*.csv.

Use it to validate policy decisions before rebuilding them in Power Automate.
Run:  python3 simulator/hooks_sim.py
"""
import csv
import re
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
IBAN_RE = re.compile(r"[A-Z]{2}\d{2}[A-Z0-9]{10,30}")


def load(name, key):
    with open(DATA / name, newline="") as f:
        return {r[key]: r for r in csv.DictReader(f)}


VENDORS = load("vendors.csv", "vendor_id")
VENDORS_BY_NAME = {v["name"].lower(): v for v in VENDORS.values()}
EMPLOYEES = load("employees.csv", "upn")
BUDGETS = load("budgets.csv", "cost_center")
DOMAINS = {v["email_domain"] for v in VENDORS.values() if v["status"] == "Approved"}


def mask_iban(iban):
    return iban[:4] + " **** **** " + iban[-4:] if len(iban) > 8 else "****"


def hook_start(upn):
    """Start hook -> user context (Dataverse lookup)."""
    e = EMPLOYEES.get(upn)
    if not e:
        return {"found": False}
    return {
        "found": True, "department": e["department"], "cost_center": e["cost_center"],
        "approval_limit": float(e["approval_limit_eur"]), "manager": e["manager_upn"],
        "categories": e["can_buy_categories"].split(";"), "active": e["active"] == "true",
    }


def hook_prompt(prompt):
    """User prompt submitted hook -> flag sensitive data."""
    flags = []
    if IBAN_RE.search(prompt.replace(" ", "")):
        flags.append("IBAN")
    if re.search(r"\b(?:\d[ -]?){13,16}\b", prompt):
        flags.append("CARD_NUMBER")
    return {"flags": flags, "action": "log_only"}


def pre_create_po(upn, vendor_id, amount, cost_center=None, currency=None):
    """Pre tool use hook for CreatePurchaseOrder -> allow / modify / deny."""
    ctx = hook_start(upn)
    v = VENDORS.get(vendor_id)
    if not ctx["found"] or not ctx["active"]:
        return {"decision": "deny", "rule": "R1", "reason": "Your account is not active for purchasing."}
    if not v:
        return {"decision": "deny", "rule": "R3", "reason": f"Unknown vendor {vendor_id}."}
    if v["status"] == "Blocked":
        return {"decision": "deny", "rule": "R2", "reason": f"Vendor {v['name']} is blocked by Procurement/Compliance."}
    if v["status"] != "Approved":
        return {"decision": "deny", "rule": "R3", "reason": f"Vendor {v['name']} is not approved yet (status: {v['status']})."}
    if v["category"] not in ctx["categories"]:
        return {"decision": "deny", "rule": "R4", "reason": f"You are not permitted to buy {v['category']}."}
    if amount > ctx["approval_limit"]:
        return {"decision": "deny", "rule": "R5",
                "reason": f"Amount {amount:,.0f} exceeds your limit of {ctx['approval_limit']:,.0f}. Manager approval ({ctx['manager']}) required."}
    cc = cost_center or ctx["cost_center"]
    b = BUDGETS.get(cc)
    if b and amount > float(b["remaining_eur"]):
        return {"decision": "deny", "rule": "R6", "reason": f"Cost center {cc} has only {b['remaining_eur']} left this quarter."}
    mods = {}
    if not cost_center:
        if not ctx["cost_center"]:
            return {"decision": "deny", "rule": "R7", "reason": "No cost center on your profile; ask Finance."}
        mods["cost_center"] = ctx["cost_center"]
    if currency != v["currency"]:
        mods["currency"] = v["currency"]
    if mods:
        return {"decision": "modify", "rule": "R7/R8", "modified_inputs": mods, "reason": "Inputs normalised from profile/vendor."}
    return {"decision": "allow", "rule": "R9", "reason": "Within policy."}


def pre_send_email(recipient, body):
    """Pre tool use hook for SendEmailToVendor."""
    domain = recipient.split("@")[-1].lower()
    if domain not in DOMAINS:
        return {"decision": "deny", "rule": "R10", "reason": f"Recipient domain {domain} is not an approved vendor domain."}
    if IBAN_RE.search(body.replace(" ", "")):
        return {"decision": "deny", "rule": "R11", "reason": "Email body contains bank details; use the secure portal."}
    return {"decision": "allow", "rule": "R12", "reason": "Recipient verified."}


def post_vendor_details(vendor_id):
    """Post tool use hook for GetVendorDetails -> redacted result."""
    v = dict(VENDORS[vendor_id])
    v["iban"] = mask_iban(v["iban"])
    v["tax_id"] = "*" * (len(v["tax_id"]) - 3) + v["tax_id"][-3:]
    v.pop("risk_score", None)
    return v


def failure_handler(tool, error):
    ticket = "INC-4821"
    return {"ticket": ticket, "message": f"{tool} is temporarily unavailable. Ticket {ticket} opened.", "error": error}


if __name__ == "__main__":
    cases = [
        ("A1 over limit", pre_create_po("amelie.dupont@contoso.com", "V-1001", 48000, "CC-4100", "EUR"), "deny"),
        ("A2 within limit", pre_create_po("amelie.dupont@contoso.com", "V-1001", 8000, "CC-4100", "EUR"), "allow"),
        ("A3 blocked vendor", pre_create_po("lars.meyer@contoso.com", "V-1008", 1000, "CC-4100", "USD"), "deny"),
        ("A4 pending vendor", pre_create_po("lars.meyer@contoso.com", "V-1007", 1000, "CC-4100", "EUR"), "deny"),
        ("A5 category not permitted", pre_create_po("jonas.weber@contoso.com", "V-1001", 1000, "CC-4100", "EUR"), "deny"),
        ("A6 missing cost center", pre_create_po("amelie.dupont@contoso.com", "V-1009", 900, None, "GBP"), "modify"),
        ("A7 wrong currency", pre_create_po("amelie.dupont@contoso.com", "V-1009", 900, "CC-4100", "EUR"), "modify"),
        ("A8 inactive employee", pre_create_po("old.employee@contoso.com", "V-1003", 100, "CC-2100", "EUR"), "deny"),
        ("A9 over budget", pre_create_po("ines.garcia@contoso.com", "V-1002", 99000, "CC-4100", "EUR"), "deny"),
        ("A10 intern no cc", pre_create_po("new.intern@contoso.com", "V-1003", 100, None, "EUR"), "deny"),
        ("E1 bad domain", pre_send_email("x@gmail.com", "hello"), "deny"),
        ("E2 iban in body", pre_send_email("orders@acme-industrial.com", "pay DE89 3704 0044 0532 0130 00"), "deny"),
        ("E3 ok email", pre_send_email("orders@acme-industrial.com", "Please confirm delivery date"), "allow"),
    ]
    fails = 0
    for name, res, expected in cases:
        ok = res["decision"] == expected
        fails += not ok
        print(f"{'PASS' if ok else 'FAIL'}  {name:28} -> {res['decision']:6} {res['reason']}")
    print("prompt flags:", hook_prompt("my card is 4111 1111 1111 1111"))
    print("redacted:", {k: post_vendor_details("V-1001")[k] for k in ("name", "iban", "tax_id")})
    print("failure:", failure_handler("CreatePurchaseOrder", "timeout"))
    raise SystemExit(1 if fails else 0)
