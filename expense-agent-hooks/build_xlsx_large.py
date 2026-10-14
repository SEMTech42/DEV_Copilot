"""Genere expense_policy_large.xlsx : jeu de donnees plus complet (graine fixe, reproductible).
Tables : Policy, Employees, Expenses, AuditLog + feuille Tests. Meme schema que expense_policy.xlsx.
Usage: python3 build_xlsx_large.py
"""
import random
from datetime import datetime, timedelta
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.table import Table, TableStyleInfo

random.seed(42)
OUT = Path(__file__).resolve().parent / "expense_policy_large.xlsx"

POLICY = [  # category, max, receipt_above, allowed, comment
    ("Repas", 40, 500, "Oui", "Plafond par personne"),
    ("Hotel", 150, 500, "Oui", "Plafond par nuit"),
    ("Taxi", 60, 500, "Oui", "Par course"),
    ("Train", 200, 50, "Oui", "2nde classe, justificatif au-dela de 50"),
    ("Avion", 600, 0, "Oui", "Justificatif toujours obligatoire"),
    ("Parking", 30, 500, "Oui", "Par jour"),
    ("Carburant", 120, 50, "Oui", "Vehicule de service uniquement"),
    ("Materiel", 500, 100, "Oui", "Justificatif obligatoire au-dela de 100"),
    ("Formation", 1500, 0, "Oui", "Justificatif toujours obligatoire"),
    ("Telephone", 80, 50, "Oui", "Forfait ou accessoires"),
    ("Cadeau client", 70, 0, "Oui", "Justificatif toujours obligatoire"),
    ("Alcool", 0, 0, "Non", "Jamais rembourse"),
    ("Divertissement", 0, 0, "Non", "Jamais rembourse"),
    ("Amende", 0, 0, "Non", "Jamais rembourse"),
]
P = {p[0]: p for p in POLICY}

EMPLOYEES = [  # email, name, dept, cost_center, manager
    ("amelie.dupont@contoso.com", "Amelie Dupont", "Maintenance", "CC-4100", "lars.meyer@contoso.com"),
    ("jonas.weber@contoso.com", "Jonas Weber", "Maintenance", "CC-4100", "lars.meyer@contoso.com"),
    ("lars.meyer@contoso.com", "Lars Meyer", "Maintenance", "CC-4100", "ines.garcia@contoso.com"),
    ("sofia.rossi@contoso.com", "Sofia Rossi", "Finance", "CC-2100", "ines.garcia@contoso.com"),
    ("tom.baker@contoso.com", "Tom Baker", "IT", "CC-3200", "ines.garcia@contoso.com"),
    ("ines.garcia@contoso.com", "Ines Garcia", "Operations", "CC-1000", "ceo@contoso.com"),
    ("claire.martin@contoso.com", "Claire Martin", "Ventes", "CC-5100", "paul.durand@contoso.com"),
    ("paul.durand@contoso.com", "Paul Durand", "Ventes", "CC-5100", "ines.garcia@contoso.com"),
    ("yasmine.benali@contoso.com", "Yasmine Benali", "Ventes", "CC-5100", "paul.durand@contoso.com"),
    ("hugo.lambert@contoso.com", "Hugo Lambert", "RH", "CC-2200", "ines.garcia@contoso.com"),
    ("emma.petit@contoso.com", "Emma Petit", "Marketing", "CC-5200", "ines.garcia@contoso.com"),
    ("noah.leroy@contoso.com", "Noah Leroy", "IT", "CC-3200", "tom.baker@contoso.com"),
    ("lea.moreau@contoso.com", "Lea Moreau", "Finance", "CC-2100", "sofia.rossi@contoso.com"),
    ("karim.haddad@contoso.com", "Karim Haddad", "Logistique", "CC-1100", "ines.garcia@contoso.com"),
    ("julie.fontaine@contoso.com", "Julie Fontaine", "Marketing", "CC-5200", "emma.petit@contoso.com"),
]

DESC = {
    "Repas": ["Dejeuner client", "Diner d'equipe", "Dejeuner deplacement", "Petit-dejeuner seminaire"],
    "Hotel": ["Nuit hotel Lyon", "Nuit hotel Paris", "Nuit hotel Lille", "Nuit hotel Bordeaux"],
    "Taxi": ["Gare vers site client", "Aeroport vers hotel", "Course soiree", "Retour gare"],
    "Train": ["Paris-Lyon", "Paris-Lille", "Lyon-Marseille", "Bordeaux-Paris"],
    "Avion": ["Vol Paris-Munich", "Vol Paris-Londres", "Vol Lyon-Amsterdam", "Vol Paris-Madrid"],
    "Parking": ["Parking gare", "Parking client", "Parking aeroport"],
    "Carburant": ["Plein vehicule de service", "Carburant tournee"],
    "Materiel": ["Souris et clavier", "Ecran", "Casque", "Sacoche", "Ordinateur portable", "Imprimante"],
    "Formation": ["Formation Power Platform", "Certification Azure", "Seminaire management"],
    "Telephone": ["Coque et chargeur", "Forfait data", "Casque Bluetooth"],
    "Cadeau client": ["Coffret client", "Cadeau fin d'annee", "Bouteille de presentation"],
    "Alcool": ["Bouteille de vin", "Cocktails soiree", "Biere equipe"],
    "Divertissement": ["Billets concert", "Soiree bowling", "Cinema equipe"],
    "Amende": ["Amende stationnement", "Exces de vitesse"],
}
# poids de tirage (les depenses courantes dominent, les refus sont minoritaires)
WEIGHT = {"Repas": 24, "Hotel": 10, "Taxi": 12, "Train": 10, "Avion": 5, "Parking": 6, "Carburant": 5,
          "Materiel": 9, "Formation": 3, "Telephone": 3, "Cadeau client": 3, "Alcool": 4,
          "Divertissement": 3, "Amende": 2}
CATS = list(WEIGHT)


def gate(cat, amount, receipt):
    p = P.get(cat)
    if p is None:
        return "deny", f"Categorie inconnue : {cat}. Choisir Repas, Hotel, Taxi ou Materiel."
    if p[3] != "Oui":
        return "deny", f"La categorie {cat} n'est jamais remboursee."
    if amount > p[1]:
        return "deny", f"Plafond depasse : {p[1]} EUR maximum pour {cat}."
    if amount > p[2] and receipt != "Oui":
        return "deny", f"Justificatif obligatoire au-dela de {p[2]} EUR."
    return "allow", "Conforme"


def amount_for(cat):
    p = P[cat]
    base = p[1] if p[1] else random.choice([25, 40, 60, 90])
    # ~70% sous le plafond, ~30% au-dessus (provoque des refus realistes)
    f = random.uniform(0.3, 1.0) if random.random() < 0.7 else random.uniform(1.05, 2.0)
    return round(base * f, 2)


start = datetime(2026, 9, 1, 8, 0)
audit, expenses = [], []
nid = 1000
for _ in range(320):
    emp = random.choice(EMPLOYEES)
    cat = random.choices(CATS, weights=[WEIGHT[c] for c in CATS])[0]
    amount = amount_for(cat)
    receipt = "Oui" if random.random() < 0.65 else "Non"
    ts = start + timedelta(days=random.randint(0, 43), hours=random.randint(0, 9), minutes=random.randint(0, 59))
    decision, reason = gate(cat, amount, receipt)
    audit.append([ts.strftime("%Y-%m-%dT%H:%M:%SZ"), emp[0], cat, amount, receipt, decision, reason])
    if decision == "allow":
        nid += 1
        expenses.append([f"NDF-{nid}", ts.strftime("%Y-%m-%dT%H:%M:%SZ"), emp[0], cat, amount,
                         random.choice(DESC[cat]), random.choice(["Soumise", "Soumise", "Validee", "Remboursee"])])
audit.sort(key=lambda r: r[0])
expenses.sort(key=lambda r: r[1])

wb = Workbook()


def add(name, header, rows, widths):
    ws = wb.active if name == "Policy" else wb.create_sheet(name)
    ws.title = name
    ws.append(header)
    for r in rows:
        ws.append(r)
    t = Table(displayName=name, ref=f"A1:{ws.cell(row=len(rows) + 1, column=len(header)).coordinate}")
    t.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
    ws.add_table(t)
    for i, w in enumerate(widths):
        ws.column_dimensions[ws.cell(row=1, column=i + 1).column_letter].width = w
    ws.freeze_panes = "A2"


add("Policy", ["category", "max_amount", "needs_receipt_above", "allowed", "comment"], POLICY, (16, 12, 20, 9, 44))
add("Employees", ["email", "name", "department", "cost_center", "manager"], EMPLOYEES, (30, 18, 14, 12, 30))
add("Expenses", ["expense_id", "timestamp", "user", "category", "amount", "description", "status"], expenses, (12, 22, 30, 15, 10, 30, 12))
add("AuditLog", ["timestamp", "user", "category", "amount", "has_receipt", "decision", "reason"], audit, (22, 30, 15, 10, 12, 10, 58))

ts_ = wb.create_sheet("Tests")
ts_.append(["id", "prompt", "category", "amount", "has_receipt", "decision attendue", "raison attendue"])
for t in [
    ("T1", "Resto client 32 EUR", "Repas", 32, "Non"),
    ("T2", "Diner d'equipe 85 EUR", "Repas", 85, "Non"),
    ("T3", "Bouteille de vin 60 EUR", "Alcool", 60, "Non"),
    ("T4", "Ordinateur 700 EUR avec justificatif", "Materiel", 700, "Oui"),
    ("T5", "Souris 120 EUR sans justificatif", "Materiel", 120, "Non"),
    ("T6", "Souris 120 EUR avec justificatif", "Materiel", 120, "Oui"),
    ("T7", "Billet de bateau 80 EUR", "Bateau", 80, "Oui"),
    ("T8", "Hotel 150 EUR", "Hotel", 150, "Non"),
    ("T9", "Taxi 61 EUR", "Taxi", 61, "Non"),
    ("T10", "Vol Paris-Munich 450 EUR sans justificatif", "Avion", 450, "Non"),
    ("T11", "Vol Paris-Munich 450 EUR avec justificatif", "Avion", 450, "Oui"),
    ("T12", "Formation Azure 1200 EUR avec justificatif", "Formation", 1200, "Oui"),
    ("T13", "Amende de stationnement 35 EUR", "Amende", 35, "Oui"),
    ("T14", "Train Paris-Lille 45 EUR sans justificatif", "Train", 45, "Non"),
    ("T15", "Train Paris-Lille 90 EUR sans justificatif", "Train", 90, "Non"),
]:
    d, r = gate(t[2], t[3], t[4])
    ts_.append([*t, d, r])
for c in ts_[1]:
    c.font = Font(bold=True, color="FFFFFF")
    c.fill = PatternFill("solid", fgColor="305496")
for col, w in zip("ABCDEFG", (6, 44, 14, 10, 12, 18, 58)):
    ts_.column_dimensions[col].width = w
wb.save(OUT)
print(f"ecrit {OUT}: {len(POLICY)} regles, {len(EMPLOYEES)} employes, {len(expenses)} notes, {len(audit)} lignes d'audit")
