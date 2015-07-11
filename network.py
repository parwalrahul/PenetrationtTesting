#! /usr/bin/python2

import os
import time

def a():
	os.system("dialog --no-shadow --infobox ' The Basic Network & System Options  ' 10 40") 
	time.sleep(1)
	def nw():
		os.system("dialog --no-shadow --title 'Network & System Options' --menu 'Select Your Choice : ' 20 100 10 1 'Know your IP Address ' 2 'Know your MAC address. ' 3 'Change your IP address. ' 4 'Change Your MAC address ' 5 'Know Hosts MAC Address ' 6 'Know the Speed of your Lan Card.' 7 'Know your Gateway(s) Address' 8 'Know Your Kernel Details' 9 'Know Your CPU Details' 10 'Back' 2> /root/Desktop/Project/choice.txt")
		f=open('/root/Desktop/Project/choice.txt','r')
		c=f.read()
		if c=='1':
			f=open('/root/Desktop/Project/ip.txt','w')
			f.write("Your IP Address is : \n")
			f.close()
			os.system("ifconfig | grep Bcast | awk '{print $2}' | cut -c 6-18 >> /root/Desktop/Project/ip.txt")
			os.system("dialog --no-shadow --textbox /root/Desktop/Project/ip.txt 10 30")
			nw()


		if c=='2':
			f=open('/root/Desktop/Project/mac.txt','w')
			f.write("Your MAC Address is : \n")
			f.close()
			os.system("ifconfig | grep HWaddr | awk '{print $5}' >> /root/Desktop/Project/mac.txt")
			os.system("dialog --no-shadow --textbox /root/Desktop/Project/mac.txt 10 30")
			nw()


		if c=='3':
			f=open('/root/Desktop/Project/ip.txt','w')
			a=f.write("Your Current IP  Address is : \n")
			f.close()
			os.system("ifconfig | grep Bcast | awk '{print $2}' | cut -c 6-18 >> /root/Desktop/Project/ip.txt")
			os.system("dialog --no-shadow --textbox /root/Desktop/Project/ip.txt 10 40")
			f=open('/root/Desktop/Project/ip.txt','w')
			a=f.write("Your New IP  Address is : \n")
			f.close()
			os.system("dialog --no-shadow --inputbox 'Enter New IP Address : ' 10 50 2> /root/Desktop/Project/ipnew.txt")
			f=open('/root/Desktop/Project/ipnew.txt','r')
			a=f.read()
			f.close()
			os.system("ifconfig eth0 "+a)
			f=open('/root/Desktop/Project/ip.txt','a')
			f.write(a)
			f.close()
			os.system("dialog --no-shadow --textbox /root/Desktop/Project/ip.txt 10 30")
			nw()


		if c=='4':
			f=open('/root/Desktop/Project/mac.txt','w')
			a=f.write("Your Current MAC  Address is : \n")
			f.close()
			os.system("ifconfig | grep HWaddr | awk '{print $5}' >> /root/Desktop/Project/mac.txt")
			os.system("dialog --no-shadow --textbox /root/Desktop/Project/mac.txt 10 40")
			f=open('/root/Desktop/Project/mac.txt','w')
			a=f.write("Your New MAC  Address is : \n")
			f.close()
			os.system("dialog --no-shadow --inputbox 'Enter New MAC Address : ' 10 50 2> /root/Desktop/Project/macnew.txt")
			f=open('/root/Desktop/Project/macnew.txt','r')
			a=f.read()
			f.close()
			os.system("ifconfig eth0 hw ether "+a)
			f=open('/root/Desktop/Project/mac.txt','a')
			f.write(a)
			f.close()
			os.system("dialog --no-shadow --textbox /root/Desktop/Project/mac.txt 10 30")
			nw()

		if c=='5':
			os.system("dialog --no-shadow --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/Project/hello.txt")
			f=open('/root/Desktop/Project/hello.txt','r')
			x=f.read()
			os.system("dialog --no-shadow --infobox 'Please wait till the Mac Detail is being searched...' 10 50")
			os.system("ping -c 3 "+x+" > /dev/null")
			os.system("arp "+x+" > /root/Desktop/Project/result")
			os.system("dialog --no-shadow --textbox /root/Desktop/Project/result 10 80")
			nw()


		if c=='6':
			os.system("ethtool eth0 > /root/Desktop/dump/lan")
			os.system("cat /root/Desktop/dump/lan | grep Speed > /root/Desktop/dump/speed")
			os.system("dialog --no-shadow --textbox /root/Desktop/dump/speed 10 30")
			nw()

		
		if c=='7':
			os.system("route -n | grep UG | awk '{print $2}' > /root/Desktop/dump/route")
			os.system("dialog --no-shadow --textbox /root/Desktop/dump/route 10 60")
			nw()

		if c=='8':
			os.system("uname -a > /root/Desktop/dump/kernel")
			os.system("dialog --no-shadow --textbox /root/Desktop/dump/kernel 10 60")
			nw()

		if c=='9':
			os.system("lscpu > /root/Desktop/dump/cpu")
			os.system("dialog --no-shadow --textbox /root/Desktop/dump/cpu 20 60")
			nw()

		if c==10:
			exit()


	nw()


