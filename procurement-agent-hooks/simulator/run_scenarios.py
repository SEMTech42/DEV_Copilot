"""Plays scenarios.json through the hook chain and writes data/audit_log.csv.
Run: python3 simulator/run_scenarios.py [S1 S2 ...]
"""
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import hooks_sim as h

ROOT = Path(__file__).resolve().parent
scenarios = json.loads((ROOT / "scenarios.json").read_text())
wanted = set(sys.argv[1:])
audit = []


def log(sc, event, decision, rule="", reason="", tool=""):
    audit.append([datetime.now(timezone.utc).isoformat(timespec="seconds"), event, sc["id"], sc["user"],
                  tool, decision, rule, reason, json.dumps(sc["input"])])


for sc in scenarios:
    if wanted and sc["id"] not in wanted:
        continue
    print(f"\n=== {sc['id']} {sc['title']} ({sc['user']})")
    print(f"USER  : {sc['prompt']}")
    ctx = h.hook_start(sc["user"])
    print(f"[Start]       contexte: limite={ctx.get('approval_limit')} cc={ctx.get('cost_center')}")
    log(sc, "Start", "log")
    p = h.hook_prompt(sc["prompt"])
    print(f"[Prompt]      flags={p['flags']}")
    log(sc, "Prompt", "log", reason=",".join(p["flags"]))
    t, i = sc["tool"], sc["input"]
    print(f"AGENT : veut appeler {t}({json.dumps(i)})")
    if t == "CreatePurchaseOrder":
        r = h.pre_create_po(sc["user"], i["vendor_id"], i["amount"], i.get("cost_center"), i.get("currency"))
    elif t == "SendEmailToVendor":
        r = h.pre_send_email(i["recipient"], i["body"])
    else:
        r = {"decision": "allow", "rule": "-", "reason": "no pre-hook"}
    print(f"[PreToolUse]  {r['decision'].upper()} {r['rule']}: {r['reason']} {r.get('modified_inputs', '')}")
    log(sc, "PreTool", r["decision"], r["rule"], r["reason"], t)
    if r["decision"] == "deny":
        print("AGENT : l'outil n'est PAS execute. Explique le refus a l'utilisateur.")
        continue
    if sc.get("simulate_failure"):
        f = h.failure_handler(t, sc["simulate_failure"])
        print(f"[ToolFailure] {f['message']}")
        log(sc, "ToolFailure", "log", reason=f["message"], tool=t)
        continue
    if t == "GetVendorDetails":
        out = h.post_vendor_details(i["vendor_id"])
        print(f"[PostToolUse] REDACT iban={out['iban']} tax_id={out['tax_id']}")
        log(sc, "PostTool", "redact", reason=f"iban masked for {i['vendor_id']}", tool=t)
    else:
        print("TOOL  : execute avec", {**i, **r.get("modified_inputs", {})})

out = ROOT.parent / "data" / "audit_log.csv"
with open(out, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["timestamp", "event", "conversation_id", "user", "tool", "decision", "rule_id", "reason", "input_json"])
    w.writerows(audit)
print(f"\naudit -> {out} ({len(audit)} lignes)")
