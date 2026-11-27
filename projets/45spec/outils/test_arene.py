import sys,threading,http.server,functools,socketserver
from playwright.sync_api import sync_playwright
racine=sys.argv[1]
H=functools.partial(http.server.SimpleHTTPRequestHandler,directory=racine)
H.log_message=lambda *a:None
srv=socketserver.TCPServer(("127.0.0.1",0),H);port=srv.server_address[1]
threading.Thread(target=srv.serve_forever,daemon=True).start()
err=[]
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page()
    pg.on("pageerror",lambda e:err.append("JS "+str(e)))
    pg.on("console",lambda m:m.type=="error" and err.append("console "+m.text))
    pg.on("response",lambda r:r.status>=400 and err.append(f"{r.status} {r.url}"))
    pg.goto(f"http://127.0.0.1:{port}/conception/prototypes/arene45/index.html");pg.wait_for_timeout(4000)
    b.close()
srv.shutdown();print("erreurs:",len(err));[print(e) for e in err[:10]]
