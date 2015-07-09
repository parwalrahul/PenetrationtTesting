#! /usr/bin/python

import os
import time
import commands

def a():
	os.system("dialog --no-shadow --infobox ' Welcome to the Reconnaissance tool' 10 40") 
	time.sleep(2)
	os.system("dialog --no-shadow --menu 'Select Your Choice : ' 20 100 7 1 'Gather information about any website and it(s) owner.' 2 'Know the route to the server where website is hosted.' 3 'Back ' 2> /root/Desktop/Project/choice.txt")
	f=open('/root/Desktop/Project/choice.txt','r')
	c=f.read()
	if c=='1':
		os.system("dialog --no-shadow --inputbox 'Enter website name : (Example : google.com) ' 10 50 2> /root/Desktop/Project/hello.txt")
		f=open('/root/Desktop/Project/hello.txt','r')
		x=f.read()
		os.system("dialog --no-shadow --infobox '  Fetching Data.. ' 10 40")
		os.system("whois -H "+x+" > /root/Desktop/dump/info" +x)
		os.system("sed -i 's/WHOIS/master/g' /root/Desktop/dump/info"+x)
		os.system("sed -i 's/whois/master/g' /root/Desktop/dump/info"+x)
		os.system("dialog --no-shadow --textbox /root/Desktop/dump/info"+x+" 20 80")

	if c=='2':
		os.system("dialog --no-shadow --inputbox 'Enter website name : (Example : google.com) ' 10 50 2> /root/Desktop/Project/hello.txt")
		f=open('/root/Desktop/Project/hello.txt','r')
		x=f.read()
		os.system("dialog --no-shadow --infobox '  Fetching Data.. ' 10 40")
		os.system("traceroute "+x+" > /root/Desktop/dump/route"+x)
		os.system("dialog --no-shadow --textbox /root/Desktop/dump/route"+x+" 30 100")

	if c==3:
		exit(0)
