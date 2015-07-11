#! /usr/bin/python2

import facts
import nmap
import aboutme
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
	os.system("dialog --no-shadow --title 'Main Menu ' --menu 'Select Your Choice : ' 20 80 10 1 'For Scanning devices on the Network  ' 2 'For MITM Attacks (Man in the Middle) & Blocks' 3 'Basic Network and System Information ' 4 'Lock and Unlock a file' 5 'DOS attacks (Denial of Service)' 6 'Gather Information about Victims' 7 'X-Options' 8 'Do You Know ?' 9 'About Us' 10 'Exit'  2> /root/Desktop/Project/choice.txt")
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
		facts.a()
		a()
	if c=='9':
		aboutme.a()
		a()
	if c=='10':
		print "\n"*100
		exit(0)


a()
