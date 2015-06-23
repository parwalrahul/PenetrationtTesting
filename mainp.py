#! /usr/bin/python2


import nmap
import network
import arpspoof
import lock
import os
import commands
import time
import signal

os.system("dialog --infobox ' Welcome to the Network Tool \n    BY Rahul Parwal' 10 50") 
time.sleep(2)
def a() :
	os.system("dialog --menu 'Select Your Choice : ' 20 80 7 1 'For Scanning devices on network . ' 2 'For Arp Spoofing' 3 'Basic Network Options ' 4 'Lock and Unlock a file' 5 'Exit' 2> /root/Desktop/Project/choice.txt")
	f=open('/root/Desktop/Project/choice.txt','r')
	c=f.read()
	if c=='1':
		nmap.a()
		a()
	if c=='2':
		arpspoof.a()
		a()
	if c=='3':	
		network.a()
		a()
	if c=='4':
		lock.a()
		a()
	if c=='5':
		print "\n"*100
		exit(0)



a()
