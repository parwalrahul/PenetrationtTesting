#! /usr/bin/python2

import os
import time

def a():
	os.system("dialog --infobox '	  The basic network options  ' 10 40") 
	time.sleep(1)
	def nw():
		os.system("dialog --menu 'Select Your Choice : ' 20 100 7 1 'Know your IP Address ' 2 'Know your MAC address. ' 3 'Change your IP address. ' 4 'Change Your MAC address ' 5 'Back' 2> /root/Desktop/Project/choice.txt")
		f=open('/root/Desktop/Project/choice.txt','r')
		c=f.read()
		if c=='1':
			f=open('/root/Desktop/Project/ip.txt','w')
			f.write("Your IP Address is : \n")
			f.close()
			os.system("ifconfig | grep Bcast | awk '{print $2}' | cut -c 6-18 >> /root/Desktop/Project/ip.txt")
			os.system("dialog --textbox /root/Desktop/Project/ip.txt 10 30")

		if c=='2':
			f=open('/root/Desktop/Project/mac.txt','w')
			f.write("Your MAC Address is : \n")
			f.close()
			os.system("ifconfig | grep HWaddr | awk '{print $5}' >> /root/Desktop/Project/mac.txt")
			os.system("dialog --textbox /root/Desktop/Project/mac.txt 10 30")
	

		if c=='3':
			f=open('/root/Desktop/Project/ip.txt','w')
			a=f.write("Your Current IP  Address is : \n")
			f.close()
			os.system("ifconfig | grep Bcast | awk '{print $2}' | cut -c 6-18 >> /root/Desktop/Project/ip.txt")
			os.system("dialog --textbox /root/Desktop/Project/ip.txt 10 40")
			f=open('/root/Desktop/Project/ip.txt','w')
			a=f.write("Your New IP  Address is : \n")
			f.close()
			os.system("dialog --inputbox 'Enter New IP Address : ' 10 50 2> /root/Desktop/Project/ipnew.txt")
			f=open('/root/Desktop/Project/ipnew.txt','r')
			a=f.read()
			f.close()
			os.system("ifconfig eth0 "+a)
			f=open('/root/Desktop/Project/ip.txt','a')
			f.write(a)
			f.close()
			os.system("dialog --textbox /root/Desktop/Project/ip.txt 10 30")

		if c=='4':
			f=open('/root/Desktop/Project/mac.txt','w')
			a=f.write("Your Current MAC  Address is : \n")
			f.close()
			os.system("ifconfig | grep HWaddr | awk '{print $5}' >> /root/Desktop/Project/mac.txt")
			os.system("dialog --textbox /root/Desktop/Project/mac.txt 10 40")
			f=open('/root/Desktop/Project/mac.txt','w')
			a=f.write("Your New MAC  Address is : \n")
			f.close()
			os.system("dialog --inputbox 'Enter New MAC Address : ' 10 50 2> /root/Desktop/Project/macnew.txt")
			f=open('/root/Desktop/Project/macnew.txt','r')
			a=f.read()
			f.close()
			os.system("ifconfig eth0 hw ether "+a)
			f=open('/root/Desktop/Project/mac.txt','a')
			f.write(a)
			f.close()
			os.system("dialog --textbox /root/Desktop/Project/mac.txt 10 30")

		if c==5:
			exit()
	nw()
