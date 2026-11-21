import sys,subprocess,time
from playwright.sync_api import sync_playwright
srv=subprocess.Popen(['python3','-m','http.server','8765','-d','/tmp/w/www'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);time.sleep(1)
try:
  with sync_playwright() as p:
    b=p.chromium.launch(args=['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'])
    pg=b.new_page(viewport={'width':1600,'height':1000})
    pg.on('console',lambda m:print('CON',m.text)); pg.on('pageerror',lambda e:print('ERR',e))
    for cfg,out in zip(sys.argv[1::2],sys.argv[2::2]):
      pg.goto('about:blank'); pg.goto('http://localhost:8765/reseau3d.html#'+cfg+'&capture'); pg.wait_for_function("document.title==='PRET'",timeout=90000)
      pg.wait_for_timeout(900); pg.screenshot(path=out,type='png'); print('ok',out)
    b.close()
finally: srv.kill()
