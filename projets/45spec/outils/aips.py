# Lit la notice professionnelle (AIPS) d'un produit sur compendium.ch : aips.py <nom | numéro de produit> [motifs...] ; la recherche liste d'abord les produits : relance avec le numéro du bon produit (AAI)
import sys, re, html, json, requests
S = requests.Session(); S.headers["User-Agent"] = "Mozilla/5.0"
q = sys.argv[1]; mots = sys.argv[2:]
r = S.post("https://compendium.ch/search/searchproducts", json={"SearchType": "Product", "Input": {"q": q, "limit": 20}}).json()
P = r.get("products", [])
for p in P[:8]: print(p.get("productNumber"), p.get("description") or p.get("productDescription"), p.get("atcCode"))
import os; os.makedirs("/tmp/src", exist_ok=True)
if q.isdigit(): num = q            # aips.py <numéro de produit> : lit exactement ce produit (la recherche par nom prend le premier trouvé)
elif not P: sys.exit("aucun produit")
else: num = P[0].get("productNumber") or r["productNumbersEnabled"][0]
t = S.get(f"https://compendium.ch/product/{num}/mpro").text
t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", t, flags=re.S); t = html.unescape(re.sub(r"<[^>]+>", " ", t)); t = re.sub(r"\s+", " ", t)
open(f"/tmp/src/aips_{q}.txt", "w").write(t)
print("produit", num, "caractères", len(t))
for m in mots:
    for x in list(re.finditer(m, t, re.I))[:2]: print("--", m, "::", t[max(0, x.start()-150): x.start()+700])
