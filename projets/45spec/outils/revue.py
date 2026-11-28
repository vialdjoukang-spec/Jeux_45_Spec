# Vue de relecture d'une forme compacte (0 token) : notions (clé, rubrique, poids, source abrégée, énoncé) puis questions (options justes entières, distracteurs en bref) : revue.py <compact.py> [n|q|qc] (qc = questions sans les explications) (AAI)
import sys, importlib.util
sys.path.insert(0, 'projets/45spec')
s = importlib.util.spec_from_file_location("m", sys.argv[1]); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
quoi = sys.argv[2] if len(sys.argv) > 2 else "nq"
if "n" in quoi:
    for i, t in enumerate(getattr(m, "_N", m.N), 1):
        k = t[0] if len(t) == 7 else ""; r, na, p, sw, so, e = t[-6:]
        print(f"N{i:02d} {k} [{r}/{na}/p{p}{'/CH' if sw else ''}] {e}  «{so[:70]}»")
if "q" in quoi:
    for i, q in enumerate(m.Q, 1):
        s_ = q.get("s"); print(f"\nQ{i} {q['f']} d{q['d']} m{q.get('m','-')} {q['a']}{' série '+str(s_[1])+'/'+str(s_[2]) if s_ else ''} | {q['st']} || {q['p']}")
        for v, t, w in q['o']:
            if "c" in quoi: print(("   V " if v else "   f ") + t)
            else: print("   V " + t + "  — " + w if v else "   f " + t + "  — " + w[:110])
