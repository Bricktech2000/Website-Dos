#NOT WORKING, PYTHON IS NOT ASYNC
#NOT ABLE TO SEND A BUNCH OF ASYNC REQUESTS, IGNORING RESPONSES
#JUST GONNA USE NODEJS, LOL



import requests_async as requests #async
import asyncio
#import time
url = input('URL: ') #'https://emilien.ml/TIH4G'
if url == '': url = 'https://emilien.ml/TIH4G' #'https://192.168.1.2/TIH4G'
#rps = 1 / int(input('Swarms per Second: '))
#nreq = int(input('Number of Requests per Swarm: '))

async def func():
    async with requests.Session() as session:
        while True:
            print('Sending Request to ' + url)
            session.get(url, verify=False) #no ssl check
            #rs = (grequests.get(url, verify=False), ) * nreq #no ssl check
            #grequests.map(rs)
            #time.sleep(rps)

asyncio.run(func())
