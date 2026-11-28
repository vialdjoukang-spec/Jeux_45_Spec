"""Applique les décisions de contrôle AIPS à un système (0 token, idempotent).
Usage : python3 appliquer_aips.py <systeme> <decisions.json>
decisions.json : {"_defaut": "...", "<pathologie>": "texte qui remplace la mention AIPS", "<pathologie>|s": "nouvelle ligne s entière"}
Remplace, dans la ligne « s » de chaque pathologie, « posologies à vérifier dans l'AIPS (Swissmedic) » (et variantes)
par le texte décidé ; « _defaut » vaut pour les pathologies sans décision propre.
Signature : AAI (Anthropic AI)"""
import json, os, re, sys
RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
MOTIF = re.compile(r"(?:les )?posologies (?:restent )?à vérifier dans l'AIPS \(Swissmedic\)|elles restent à vérifier dans l'AIPS \(Swissmedic\)")

def main():
    sysn, dec = sys.argv[1], json.load(open(sys.argv[2], encoding="utf-8"))
    f = os.path.join(RAC, "conception/outils", sysn, "pathologies.txt")
    out, cur, n, vus = [], None, 0, set()
    for l in open(f, encoding="utf-8").read().split("\n"):
        if l.startswith("@ "):
            cur = l.split("|", 1)[1].strip()
        elif l.startswith("s ") and cur:
            if cur + "|s" in dec:
                l = "s " + dec[cur + "|s"]; n += 1; vus.add(cur)
            elif MOTIF.search(l):
                rep = dec.get(cur, dec.get("_defaut"))
                if rep:
                    l = MOTIF.sub(lambda m: rep, l, count=1); n += 1; vus.add(cur)
        out.append(l)
    open(f, "w", encoding="utf-8").write("\n".join(out))
    manq = [k for k in dec if not k.startswith("_") and k.split("|")[0] not in vus]
    print("%s : %d ligne(s) s modifiée(s)%s" % (sysn, n, (" ; décisions sans cible : %s" % manq) if manq else ""))

if __name__ == "__main__":
    main()
