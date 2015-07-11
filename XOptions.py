#! /usr/bin/python2

import os
import time
import commands
import random


def a():
	os.system("dialog --no-shadow --infobox '	    Welcome to the X-Options  ' 10 40") 
	time.sleep(2)
	def x():
		os.system("dialog --no-shadow --title 'X-Options' --menu 'Select Your Choice : ' 20 100 9 1 'Use Terminal inside the Browser ' 2 'Use your System(s) Linux Terminal in your Smart Phone ' 3 'Create QR Code ' 4 'Read QR Code ' 5 'Compress a File.' 6 'Decompress a File.' 7 'Create a RAM Disk on this system' 8 'Increase Swap Memory Temporarily' 9 'Back' 2> /root/Desktop/dump/choice")
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

		if c=='5':
			os.system("dialog --no-shadow --inputbox 'Enter the path of the File to be compressed :' 10 50 2> /root/Desktop/dump/compress")
			f=open('/root/Desktop/dump/compress','r')
			compress=f.read()
			os.system("bzip2 "+compress)
			os.system("dialog --no-shadow --msgbox 'File Successfully compressed' 10 40")
			x()

		if c=='6':
			os.system("dialog --no-shadow --inputbox 'Enter the path of the File to uncompress (.bz2 extension only) :' 10 50 2> /root/Desktop/dump/unzip")
			f=open('/root/Desktop/dump/unzip','r')
			compress=f.read()
			os.system("bunzip2 "+compress)
			os.system("dialog --no-shadow --msgbox 'File Successfully Uncompressed' 10 40")
			x()
			
		if c=='7':
			os.system("dialog --no-shadow --msgbox 'RAM Disk is basically the usage of RAM to store data.\nIt is a temporary created Disk available only till the next boot.\nIt can be used to store data where you need faster access of files. (Ex: Document Root of the Webserver)\nPlease make up a backup of the data that you will store on this disk' 14 50")
			os.system("dialog --no-shadow --inputbox 'Enter the path of the Folder to be converted to RAM Disk :' 10 50 2> /root/Desktop/dump/ramdisk")
			f=open('/root/Desktop/dump/ramdisk','r')
			rdisk=f.read()
			os.system("dialog --no-shadow --inputbox 'Enter the size of the RAM Disk (Range- 5MB to 100MB , Enter 5 for 5MB) :' 10 50 2> /root/Desktop/dump/disksize")	
			f=open('/root/Desktop/dump/disksize','r')
			sdisk=f.read()
			os.system("mount -t tmpfs -o size="+sdisk+"m tmpfs "+rdisk)
			os.system("dialog --no-shadow --msgbox 'RAM Disk Successfully created' 10 40")	
			x()

		if c=='8':
			os.system("dialog --no-shadow --inputbox 'Enter the size of Additional SWAP that you want to create. (Range- 1MB to 2000MB , Enter 5 for 5MB) :' 10 50 2> /root/Desktop/dump/swapsize")	
			f=open('/root/Desktop/dump/swapsize','r')
			ssize=f.read()
			os.system("dd if=/dev/zero of=/swapfile bs=1M count="+ssize+" > /dev/null")
			os.system("chmod 600 /swapfile")
			os.system("swapon /swapfile")
			x()
			
		if c==9:
			exit()


	x()
