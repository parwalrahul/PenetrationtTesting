#! /usr/bin/python2


import nmap
import network
import arpspoof
import lock
import dos
import infogather
import os
import commands
import time
import signal
import thread
import random
import XOptions

os.system("dialog --no-shadow --infobox '         Welcome to the Nasty Tool  \n\n\n\n\n\n\n             By : Rahul Parwal' 10 50") 
time.sleep(2)
def a() :
	os.system("dialog --no-shadow --backtitle '\t\t\t\t\t\t\t\tNasty Tool' --title 'Main Menu ' --menu 'Select Your Choice : ' 20 80 8 1 'For Scanning devices on network . ' 2 'For MITM Attacks.' 3 'Basic Network Options ' 4 'Lock and Unlock a file' 5 'Perform DOS attack' 6 'Gather info about victims' 7 'X-Options' 8 'Exit'  2> /root/Desktop/Project/choice.txt")
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
		dos.a()
		a()
	if c=='6':
		infogather.a()
		a()
	if c=='7':
		XOptions.a()
		a()
	if c=='8':
		print "\n"*100
		exit(0)


a()
