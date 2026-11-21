import subprocess,time
from playwright.sync_api import sync_playwright
srv=subprocess.Popen(['python3','-m','http.server','8766','-d','/tmp/w/www'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);time.sleep(1)
try:
  with sync_playwright() as p:
    b=p.chromium.launch(args=['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']);pg=b.new_page(viewport={'width':1600,'height':1000})
    pg.on('pageerror',lambda e:print('ERR',e));pg.goto('http://localhost:8766/anatomie.html');pg.wait_for_function("document.title==='PRET'",timeout=100000);pg.screenshot(path='/tmp/w/anatomie.png');print('ok')
finally: srv.kill()
