#! /usr/bin/python2

import os
import time
import signal

def a() :
	def my(x,y):
		os.system("dialog --infobox 'Process stopped. \nThank You. ' 10 40")
		time.sleep(1)
		os.system("pkill gnome-terminal")  

	signal.signal(2,my)


	os.system("dialog --infobox '	Welcome to the network mapper' 10 50") 
	time.sleep(2)
	def n():
		os.system("dialog --menu 'Select Your Choice : ' 20 80 10 1 'Complete Network Scanning for active devices. ' 2 'Scan one or more Host' 3 'Know the Mac Address of host' 4 'Find if the ports of host machine are filtered or not' 5 'Scan a host protected by Firewall' 6 'Know Host interfaces and routes' 7 'Port Scanning  ' 8 'Internse Port Scanning' 9 'Back'  2> /root/Desktop/Project/choice.txt")
		f=open('/root/Desktop/Project/choice.txt','r')
		c=f.read()
		if c=='1' :
			os.system("dialog --inputbox 'Enter Your IP Address : ' 10 50 2> /root/Desktop/Project/hello.txt")
			f=open('/root/Desktop/Project/hello.txt','r')
			x=f.read()
			y=x+'/24'
			os.system("dialog --infobox 'Please wait for some time till the nmap process is going on....' 10 50")
			os.system("nmap -sP"+y+" > /root/Desktop/Project/result")
			os.system("dialog --textbox /root/Desktop/Project/result 20 60")

		if c=='2' :
			os.system("dialog --inputbox 'Enter the number of hosts that you want to scan : ' 10 50 2> /root/Desktop/Project/choice")
			f=open('/root/Desktop/Project/choice','r')
			y=f.read()
			q=int(float(y))
			while q>0 :
				os.system("dialog --inputbox 'Enter Host(s) IP Address : ' 10 50 2>> /root/Desktop/Project/hello.txt")
				f1=open('/root/Desktop/Project/hello.txt','ab')
				f1.write(" ")
				f1.close()
				q=q-1
			f1=open('/root/Desktop/Project/hello.txt','r')
			x=f1.readline()
			os.system("dialog --infobox 'Please wait till scanning report is being generated...' 10 50")
			os.system("nmap "+x+" > /root/Desktop/Project/result")
			os.system("dialog --textbox /root/Desktop/Project/result 20 60")
			os.system("rm -f /root/Desktop/Project/choice /root/Desktop/Project/hello /root/Desktop/Project/result")

		if c=='3':
			os.system("dialog --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/Project/hello.txt")
			f=open('/root/Desktop/Project/hello.txt','r')
			x=f.read()
			os.system("dialog --infobox 'Please wait till the Mac Detail is being searched...' 10 50")
			os.system("ping -c 3 "+x+" > /dev/null")
			os.system("arp "+x+" > /root/Desktop/Project/result")
			os.system("dialog --textbox /root/Desktop/Project/result 10 80")

		if c=='4':
			os.system("dialog --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/Project/hello.txt")
			f=open('/root/Desktop/Project/hello.txt','r')
			x=f.read()
			os.system("dialog --infobox 'Please wait till the processing is being done...' 10 50")
			os.system("nmap -sA "+x+" > /root/Desktop/Project/result")
			os.system("dialog --textbox /root/Desktop/Project/result 20 60")

		if c=='5':
			os.system("dialog --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/Project/hello.txt")
			f=open('/root/Desktop/Project/hello.txt','r')
			x=f.read()
			os.system("dialog --infobox 'Please wait till the processing is being done...' 10 50")
			os.system("nmap -PN "+x+" > /root/Desktop/Project/result")
			os.system("dialog --textbox /root/Desktop/Project/result 20 60")

		if c=='6':
			os.system("dialog --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/Project/hello.txt")
			f=open('/root/Desktop/Project/hello.txt','r')
			x=f.read()
			os.system("dialog --infobox 'Please wait till the processing is being done...' 10 50")
			os.system("nmap --iflist "+x+" > /root/Desktop/Project/result")
			os.system("dialog --textbox /root/Desktop/Project/result 20 100")

		if c=='7' :
			os.system("dialog --menu 'Port Scanning Choices : ' 20 80 7 1 'Single Port Scannning ' 2 'Scan a TCP Port ' 3 'Scan a UDP port' 4 'Scan Discrete Ports' 5 'Scan a range of ports.' 6 'Back' 2> /root/Desktop/Project/choice.txt")
			f=open('/root/Desktop/Project/choice.txt','r')
			d=f.read()
			if d=='1':
				os.system("dialog --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/Project/hello.txt")
				f=open('/root/Desktop/Project/hello.txt','r')
				x=f.read()
				os.system("dialog --inputbox 'Enter Host(s) Port Number : ' 10 50 2> /root/Desktop/Project/port.txt")
				f=open('/root/Desktop/Project/port.txt','r')
				y=f.read()
				os.system("dialog --infobox 'Please wait till the processing is being done...' 10 50")
				os.system("nmap -p "+y+" "+x+" > /root/Desktop/Project/result")
				os.system("dialog --textbox /root/Desktop/Project/result 20 100")

			if d=='2':
				os.system("dialog --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/Project/hello.txt")
				f=open('/root/Desktop/Project/hello.txt','r')
				x=f.read()
				os.system("dialog --inputbox 'Enter Host(s) Port Number : ' 10 50 2> /root/Desktop/Project/port.txt")
				f=open('/root/Desktop/Project/port.txt','r')
				y=f.read()
				os.system("dialog --infobox 'Please wait till the processing is being done...' 10 50")
				os.system("nmap -p T:"+y+" "+x+" > /root/Desktop/Project/result")
				os.system("dialog --textbox /root/Desktop/Project/result 20 100")

	
			if d=='3':
				os.system("dialog --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/Project/hello.txt")
				f=open('/root/Desktop/Project/hello.txt','r')
				x=f.read()
				os.system("dialog --inputbox 'Enter Host(s) Port Number : ' 10 50 2> /root/Desktop/Project/port.txt")
				f=open('/root/Desktop/Project/port.txt','r')
				y=f.read()
				os.system("dialog --infobox 'Please wait till the processing is being done...' 10 50")
				os.system("nmap -p U:"+y+" "+x+" > /root/Desktop/Project/result")
				os.system("dialog --textbox /root/Desktop/Project/result 20 100")	

	
			if d=='4':
				os.system("dialog --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/Project/hello.txt")
				f=open('/root/Desktop/Project/hello.txt','r')
				x=f.read()
				os.system("dialog --inputbox 'Enter the number of ports that you want to scan : ' 10 50 2> /root/Desktop/Project/choice")
				f=open('/root/Desktop/Project/choice','r')
				z=f.read()
				q=int(float(z))
				while q>0 :
					os.system("dialog --inputbox 'Enter Port Number : ' 10 50 2>> /root/Desktop/Project/port.txt")
					f1=open('/root/Desktop/Project/port.txt','ab')
					f1.write(",")
					f1.close()
					q=q-1
				f1=open('/root/Desktop/Project/port.txt','r')
				y=f1.readline()
				os.system("dialog --infobox 'Please wait till the processing is being done...' 10 50")
				os.system("nmap -p "+y+" "+x+" > /root/Desktop/Project/result")
				os.system("dialog --textbox /root/Desktop/Project/result 20 100")
				os.system("rm -f /root/Desktop/Project/port.txt")

			if d=='5':
				os.system("dialog --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/Project/hello.txt")
				f=open('/root/Desktop/Project/hello.txt','r')
				x=f.read()
				os.system("dialog --inputbox 'Enter Lower Limit of Port Number : ' 10 50 2>> /root/Desktop/Project/port.txt")
				f1=open('/root/Desktop/Project/port.txt','ab')
				f1.write("-")
				f1.close()
				os.system("dialog --inputbox 'Enter Upper Limit of Port Number : ' 10 50 2>> /root/Desktop/Project/port.txt")	
				f1=open('/root/Desktop/Project/port.txt','r')
				y=f1.readline()
				os.system("dialog --infobox 'Please wait till the processing is being done...' 10 50")
				os.system("nmap -p "+y+" "+x+" > /root/Desktop/Project/result")
				os.system("dialog --textbox /root/Desktop/Project/result 20 100")
				os.system("rm -f /root/Desktop/Project/port.txt")
			if d=='6':
				n()
			
		if c=='8':
			os.system("dialog --menu 'Intense Scanning Choices : ' 20 80 7 1 'Intense Scannning ' 2 'Internse Scanning + UDP  ' 3 'Intense Scanning - All TCP ' 4 'Intense Scanning - No Ping ' 5 'Scan a range of ports. ' 6 'Back ' 2> /root/Desktop/Project/choice.txt")
			f=open('/root/Desktop/Project/choice.txt','r')
			d=f.read()
			if d =='1':
				os.system("dialog --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/Project/hello.txt")
				f=open('/root/Desktop/Project/hello.txt','r')
				x=f.read()
				os.system("dialog --infobox 'Please wait till the processing is being done...' 10 50")
				os.system("nmap -T4 -A -v "+x+" > /root/Desktop/Project/result")
				os.system("dialog --textbox /root/Desktop/Project/result 20 60")

			if d =='2':
				os.system("dialog --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/Project/hello.txt")
				f=open('/root/Desktop/Project/hello.txt','r')
				x=f.read()
				os.system("dialog --infobox 'Please wait till the processing is being done...\nThis may take upto 10 minutes....\nIf you want to opt out press CTRL + C.. ' 10 50")
				os.system("nmap -sS -sU -T4 -A -v "+x+" > /root/Desktop/Project/result")
				os.system("dialog --textbox /root/Desktop/Project/result 20 60")

			if d=='3':
				os.system("dialog --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/Project/hello.txt")
				f=open('/root/Desktop/Project/hello.txt','r')
				x=f.read()
				os.system("dialog --infobox 'Please wait till the processing is being done...\nThis may take up some time..... \nIf Yoy want to opt out press CTRL + C.. ' 10 50")
				os.system("nmap -p 1-65535 -T4 -A -v "+x+" > /root/Desktop/Project/result")
				os.system("dialog --textbox /root/Desktop/Project/result 20 60")

			if d=='4':
				os.system("dialog --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/Project/hello.txt")
				f=open('/root/Desktop/Project/hello.txt','r')
				x=f.read()
				os.system("dialog --infobox 'Please wait till the processing is being done...\nThis may take up some time..... \nIf Yoy want to opt out press CTRL + C.. ' 10 50")
				os.system("nmap -Pn -T4 -A -v "+x+" > /root/Desktop/Project/result")
				os.system("dialog --textbox /root/Desktop/Project/result 20 60")
			
			if d=='5':
				n()


		if c==9:
			exit()
	
	n()


