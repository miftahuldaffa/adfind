##!/usr/bin/env python
#-*- coding: utf-8 -*-

#Dfv47@MiftahulDaffa
#Recode sertain authornya cuk

#Color
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
b='\033[1;34m'
w='\033[1;37m' 


try:
        import os, sys, readline, rlcompleter, requests, urllib
except Exception as F:
        exit("[ModuleErr] %s"%(F))

if sys.version[0] in '3':
        exit("[sorry] use python version 2")

from time import sleep;from urllib2 import *

def back():
		pil = raw_input(r+"\n  ["+y+"*"+r+"] "+y+"Click enter to return to the main menu...")
		if pil == "":
			print"";os.system('clear');dfv()
		elif pil == "":
			print"";os.system('clear');dfv()
		else:
			print"";os.system('clear');dfv()
			

#Admin Finder
def admin(host):
		print w+"\n  ["+g+"#"+w+"] Result "+g+":"+w+" "
		print ""
		if host.startswith("http://") or host.startswith("https://") is False:
			host = "http://" + host or "https://" + host
		finder = open('wordlist.txt', 'r')
		for i in finder:
			target = host + "/" + i
			try:
				yop = Request(target);buka = urlopen(yop);sleep(1.5)
				print w+"  ["+g+"   FOUND   "+w+"]"+y+" => " + w + target
				continue
			except URLError,HTTPError:
				print w+"  [ "+r+"NOT FOUND "+w+"]"+y+" => " + w + target
				continue
			except KeyboardInterrupt:
				break
		back() 

#banner
def banner(): 
    os.system('clear') 
    print b+"          --[ "+w+"P A G E _ A D M I N _ L O G I N _ S C A N N I N G "+b+"]--"
    print g+"  _______      __   __                    _______                      "
    print g+" |   _   | .--|  | |  | .-----. .-----.  |   _   | .----. .---.-. .-----."
    print g+" |.  1   | |  _  | |  | |  _  | |  _  |  |   1___| |  __| |  _  | |     |"
    print g+" |.  _   | |_____| |__| |_____| |___  |  |____   | |____| |___._| |__|__|"
    print g+" |:  |   |  "+w+"Author "+b+": "+w+"Dfv47"+g+"      |_____|  |:  1   | "+r+"@"+w+"GT72   " 
    print g+" |::.|:. |  "+w+"Code   "+b+": "+w+"Python"+g+"              |::.. . | "+r+"@"+w+"BBC-Community"
    print g+" `--- ---'                               `-------' "+r+"@"+w+"Zx-Team       "

def dfv(): 
    try:
     banner() 
     choice = raw_input(w+'  ['+r+'*'+w+'] Please turn on you internet for using this tools...'+r+'('+w+'type enter'+r+')')
     if choice == 'Y' or choice == 'ye' or choice == 'satu':  
         wongedan = raw_input(w+"\n  ["+g+"?"+w+"] Input website/host "+g+":"+w+" ")
         admin(wongedan) 
     elif choice == 'Y' or choice == 'ye' or choice == 'satu':  
         wongedan = raw_input(w+"\n  ["+g+"?"+w+"] Input website/host "+g+":"+w+" ")
         admin(wongedan)   
     else:
         wongedan = raw_input(w+"\n  ["+g+"?"+w+"] Input website/host "+g+":"+w+" ")
         admin(wongedan)     
    except KeyboardInterrupt:sys.exit()


if __name__=='__main__':
    dfv()
