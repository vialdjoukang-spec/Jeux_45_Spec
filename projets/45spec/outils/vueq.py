# Vue compacte des questions d'une forme compacte (AAI)
import sys, importlib.util
sys.path.insert(0,'projets/45spec')
s=importlib.util.spec_from_file_location("m",sys.argv[1]); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
for i,q in enumerate(m.Q,1):
    print(f"Q{i} {q['f']} d{q['d']} m{q.get('m','-')} | {q['st']} | {q['p']}")
    for o in q['o']:
        if isinstance(o,tuple): print("   ", "V" if o[0] else "f", o[1], "—", o[2][:90])
        else: print("   ",o)
