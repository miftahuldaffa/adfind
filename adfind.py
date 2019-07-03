#!/usr/bin/env python3

'''
Adlog - Find Admin Login Web
This project was created by Dfv47 with Black Coder Crush. 
Copyright 21 - 06 - 2k19 @m_d4fv
'''
try:
        import asyncio,aiohttp,time,socket,os,sys
except Exception as F:
        exit("[ModuleErr] %s"%(F))
from aiohttp import ClientSession

if sys.version[0] in '2':
        exit("[sorry] Use python version 3")

# Color
a='\033[1;30m'
r='\033[1;31m'
re='\033[2;31m'
g='\033[32;1m' 
gr='\033[2;32m' 
y='\033[1;33m'
ye='\033[2;33m'
c='\033[1;36m' 
cy='\033[2;36m' 
w='\033[1;37m' 
n='\033[0;00m' 
br='\033[91;7m' 

def banner(): 
    os.system('clear')
    print (c+"        ___")
    print (c+"       __H__  "+w+"{ "+a+"v.1.5 "+w+"}")
    print (c+" ___ _| ["+br+"'"+n+c+"]___ ___  "+w+"Author "+r+":"+w+" Dfv47   ")
    print (c+"| .'| . ["+br+"'"+n+c+"] . | . | "+w+"Team   "+r+":"+w+" Black Coder Crush")
    print (c+"|__,|___["+br+"'"+n+c+"]___|_  | "+w+"Github "+r+":"+w+" https://github.com/md4fv ")
    print (c+"         V    |___| "+r+"* "+a+"Page Admin login scanning in website ")    
        
'''
Coded  : @m_d4fv
Author : Dfv47
Team   : Black Coder Crush
Phone  : 6282223108828
Email  : daffamfthhsn21@gmail.com
Thanks : CRABS, ZoneExploiter, CytoXploit
'''

#Mulai proses
banner() 
target = input(c+"["+w+"?"+c+"] "+w+"Type your website "+c+":"+w+" ")

#Cek wordlist
time.sleep(1)
print ("\n[*] Checking wordlist ..")
try:
	wu = open("admin.txt","r").readlines()
	x = len(wu)
except IOError:
	print ("[!] Can't load "+c+"admin.txt, "+w+"file not exist")
	sys.exit()		
time.sleep(1)
print ("[#] Load \033[2;32m{}\033[0;00m\033[1;37m words in wordlist.txt ".format(x))

time.sleep(1)
localtime = time.asctime( time.localtime(time.time()) )
print ("\n[*] Starting @", localtime)
print ("")

#Target input
target = target.replace('https://', '')
target = target.replace('https://www.', '')
target = target.replace('http://', '')
target = target.replace('http://www.', '')
tar_list = target.split('/')
for tar in tar_list:
    if tar == '':
        tar_list.remove(tar)
target = '/'.join(tar_list)
target = 'http://' + target+'/'

start = time.time()
dfv = []
conn = aiohttp.TCPConnector(
        family=socket.AF_INET,
    )
    
def daf():
    a=time.ctime().split(' ')[4]
    return a
    
#Status website
async def fetch(url, session):
    async with session.get(url) as response: 
        status = response.status 
        if status == 200:
            print(w+"["+cy+daf()+n+w+"] ["+ye+"{}\033[0;00m\033[1;37m] {} ".format(status, response.url,))
            dfv.append(response.url)
        elif status == 404:
            print(w+"["+cy+daf()+n+w+"] ["+re+"{}\033[0;00m\033[1;37m] {} ".format(status, response.url,))
        elif status == 403:
            print(w+"["+cy+daf()+n+w+"] ["+gr+"{}\033[0;00m\033[1;37m] {} ".format(status, response.url,))
        else:
            print(w+"["+cy+daf()+n+w+"] ["+cy+"{}\033[0;00m\033[1;37m] {} ".format(status, response.url,))
        return await response.read()

#Mulai wordlist
async def run():
    url = target + "{}"
    tasks = []
    admin_list = open('admin.txt', 'r')
    paths = []
    for path in admin_list:
        path = path.replace('\n','')
        paths.append(path)
    async with ClientSession(connector=conn) as session: #creates the tasks
        for i in paths:
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)
        responses = asyncio.gather(*tasks)
        await responses
        
#Mulai Loop        
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run())
loop.run_until_complete(future)

#Hasil
end = time.time()
script_time = end - start
print("\n[*] Scan complete at \033[32;1m{} \033[0;00mseconds to complete @ {} ".format(script_time, localtime))
print(w+"\n["+c+"*"+w+"] Results :")
if len(dfv) == 0:
    print("[!] No result !!!")
else:
    for y in dfv:
        print(c+"\n *"+w+" ",y)
