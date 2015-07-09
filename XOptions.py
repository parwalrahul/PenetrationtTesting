#! /usr/bin/python2

import os
import time
import commands
import random


def a():
	os.system("dialog --no-shadow --infobox '	    Welcome to the X-Options  ' 10 40") 
	time.sleep(2)
	def x():
		os.system("dialog --no-shadow --title 'X-Options' --menu 'Select Your Choice : ' 20 100 7 1 'Use Terminal inside the Browser ' 2 'Use your System(s) Linux Terminal in your Smart Phone ' 3 'Create QR Code ' 4 'Read QR Code ' 5 'Compress a File.' 6 'Decompress a File.' 7 'Back' 2> /root/Desktop/dump/choice")
		f=open('/root/Desktop/dump/choice','r')
		c=f.read()
		if c=='1':
			os.system("dialog --no-shadow --msgbox 'Login inside the browser as a non root account.\nTo access as a root use : su - root ' 10 40")
			ip=commands.getoutput("ifconfig | grep Bcast | awk '{print $2}' | cut -c 6-18")
			f=open('/root/Desktop/dump/ip','w')
			f.write(ip)
			f.write(":4200")
			f.close()
			f=open('/root/Desktop/dump/ip','r')
			addr=f.read()
			os.system("service shellinabox restart")
			os.system("firefox "+addr)
			x()
		
		if c=='2':
			ip=commands.getoutput("ifconfig | grep Bcast | awk '{print $2}' | cut -c 6-18")
			f=open('/root/Desktop/dump/ip','w')
			f.write("https://")			
			f.write(ip)
			f.write(":4200")
			f.close()
			os.system("service shellinabox start > /dev/null")
			os.system("qrencode -s 12*12 -o /root/Desktop/dump/terminal.png < /root/Desktop/dump/ip")
			os.system("dialog --no-shadow --msgbox 'Read the QR code with the QR code reader of your Smartphone' 10 50")
			os.system("display /root/Desktop/dump/terminal.png")
			x()

		if c=='3':
			os.system("dialog --no-shadow --inputbox 'Enter the data or link that you want to convert to QR code' 10 30 2> /root/Desktop/dump/qr")
			rand=random.randint(1,1000)
			r=str(rand)
			os.system("qrencode -s 12*12 -o /root/Desktop/"+r+"qrcode.png < /root/Desktop/dump/qr")
			os.system("dialog --no-shadow --msgbox 'The QR code is saved at Desktop. Press OK to see the QR code.' 10 40")
			os.system("display /root/Desktop/"+r+"qrcode.png")
			x()

		if c=='4':
			os.system("dialog --no-shadow --inputbox 'Enter the path of the QR coded File :' 10 50 2> /root/Desktop/dump/dqr")
			f=open('/root/Desktop/dump/dqr','r')
			link=f.read()
			os.system("zbarimg "+link+" > /root/Desktop/dump/decode")
			os.system("dialog --no-shadow --textbox /root/Desktop/dump/decode 10 30")
			x()

		if c==5:
			exit()


	x()

a()
