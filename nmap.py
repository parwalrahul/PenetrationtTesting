#! /usr/bin/python2

import os
import time
import signal

def a() :
	def my(x,y):
		os.system("dialog --no-shadow --infobox 'Process stopped. \nThank You. ' 10 40")
		time.sleep(1)
		os.system("pkill gnome-terminal")  

	signal.signal(2,my)


	os.system("dialog --no-shadow --no-shadow --infobox '	       Welcome to the Scanning Tool ' 10 50") 
	time.sleep(2)
	def n():
		os.system("dialog --no-shadow --no-shadow --title 'Network Mapping Options :' --menu 'Select Your Choice : ' 20 80 10 1 'Complete Network Scanning for Active Devices. ' 2 'Scan one or more Host' 3 'Perform Version Detection on Host ' 4 'Find if the ports of host machine are Filtered or not' 5 'Scan a host protected by Firewall' 6 'Know Host interfaces and Routes' 7 'Port Scanning  ' 8 'Internse Port Scanning' 9 'OS Scanning' 10 'Back'  2> /root/Desktop/dump/choice.txt")
		f=open('/root/Desktop/dump/choice.txt','r')
		c=f.read()
		if c=='1' :
			os.system("dialog --no-shadow --no-shadow --title 'Network Scanning' --inputbox 'Enter Your IP Address : ' 10 50 2> /root/Desktop/dump/hello.txt")
			f=open('/root/Desktop/dump/hello.txt','r')
			x=f.read()
			y=x+'/24'
			os.system("dialog --no-shadow --no-shadow --title 'Network Scanning' --infobox 'Please wait for some time till the scanning process is going on....' 10 50")
			os.system("nmap -sP "+y+" > /root/Desktop/dump/result")
			os.system("dialog --no-shadow --no-shadow --title 'Network Scanning' --textbox /root/Desktop/dump/result 20 60")

		if c=='2' :
			os.system("dialog --no-shadow --no-shadow --inputbox 'Enter the number of hosts that you want to scan : ' 10 50 2> /root/Desktop/dump/choice")
			f=open('/root/Desktop/dump/choice','r')
			y=f.read()
			q=int(float(y))
			while q>0 :
				os.system("dialog --no-shadow --no-shadow --inputbox 'Enter Host(s) IP Address : ' 10 50 2>> /root/Desktop/dump/hello.txt")
				f1=open('/root/Desktop/dump/hello.txt','ab')
				f1.write(" ")
				f1.close()
				q=q-1
			f1=open('/root/Desktop/dump/hello.txt','r')
			x=f1.readline()
			os.system("dialog --no-shadow --no-shadow --infobox 'Please wait till scanning report is being generated...' 10 50")
			os.system("nmap "+x+" > /root/Desktop/dump/result")
			os.system("dialog --no-shadow --no-shadow --textbox /root/Desktop/dump/result 20 60")
			os.system("rm -f /root/Desktop/dump/choice /root/Desktop/dump/hello /root/Desktop/dump/result")

		if c=='3':
			os.system("dialog --no-shadow --no-shadow --inputbox 'Enter Host(s) IP Address or URL : ' 10 50 2> /root/Desktop/dump/hello")
			f=open('/root/Desktop/dump/hello.txt','r')
			x=f.read()
			os.system("dialog --no-shadow --no-shadow --infobox 'Please wait till the processing is being done...' 10 50")
			os.system("nmap -sV "+x+" > /root/Desktop/dump/result")
			os.system("dialog --no-shadow --no-shadow --textbox /root/Desktop/dump/result 20 60")


		if c=='4':
			os.system("dialog --no-shadow --no-shadow --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/dump/hello.txt")
			f=open('/root/Desktop/dump/hello.txt','r')
			x=f.read()
			os.system("dialog --no-shadow --no-shadow --infobox 'Please wait till the processing is being done...' 10 50")
			os.system("nmap -sA "+x+" > /root/Desktop/dump/result")
			os.system("dialog --no-shadow --no-shadow --textbox /root/Desktop/dump/result 20 60")

		if c=='5':
			os.system("dialog --no-shadow --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/dump/hello.txt")
			f=open('/root/Desktop/dump/hello.txt','r')
			x=f.read()
			os.system("dialog --no-shadow --infobox 'Please wait till the processing is being done...' 10 50")
			os.system("nmap -PN "+x+" > /root/Desktop/dump/result")
			os.system("dialog --no-shadow --textbox /root/Desktop/dump/result 20 60")

		if c=='6':
			os.system("dialog --no-shadow --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/dump/hello.txt")
			f=open('/root/Desktop/dump/hello.txt','r')
			x=f.read()
			os.system("dialog --no-shadow --infobox 'Please wait till the processing is being done...' 10 50")
			os.system("nmap --iflist "+x+" > /root/Desktop/dump/result")
			os.system("dialog --no-shadow --textbox /root/Desktop/dump/result 20 100")

		if c=='7' :
			os.system("dialog --no-shadow --menu 'Port Scanning Choices : ' 20 80 7 1 'Single Port Scannning ' 2 'Scan a TCP Port ' 3 'Scan a UDP port' 4 'Scan Discrete Ports' 5 'Scan a range of ports.' 6 'Back' 2> /root/Desktop/dump/choice.txt")
			f=open('/root/Desktop/dump/choice.txt','r')
			d=f.read()
			if d=='1':
				os.system("dialog --no-shadow --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/dump/hello.txt")
				f=open('/root/Desktop/dump/hello.txt','r')
				x=f.read()
				os.system("dialog --no-shadow --inputbox 'Enter Host(s) Port Number : ' 10 50 2> /root/Desktop/dump/port.txt")
				f=open('/root/Desktop/dump/port.txt','r')
				y=f.read()
				os.system("dialog --no-shadow --infobox 'Please wait till the processing is being done...' 10 50")
				os.system("nmap -p "+y+" "+x+" > /root/Desktop/dump/result")
				os.system("dialog --no-shadow --textbox /root/Desktop/dump/result 20 100")

			if d=='2':
				os.system("dialog --no-shadow --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/dump/hello.txt")
				f=open('/root/Desktop/dump/hello.txt','r')
				x=f.read()
				os.system("dialog --no-shadow --inputbox 'Enter Host(s) Port Number : ' 10 50 2> /root/Desktop/dump/port.txt")
				f=open('/root/Desktop/dump/port.txt','r')
				y=f.read()
				os.system("dialog --no-shadow --infobox 'Please wait till the processing is being done...' 10 50")
				os.system("nmap -p T:"+y+" "+x+" > /root/Desktop/dump/result")
				os.system("dialog --no-shadow --textbox /root/Desktop/dump/result 20 100")

	
			if d=='3':
				os.system("dialog --no-shadow --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/dump/hello.txt")
				f=open('/root/Desktop/dump/hello.txt','r')
				x=f.read()
				os.system("dialog --no-shadow --inputbox 'Enter Host(s) Port Number : ' 10 50 2> /root/Desktop/dump/port.txt")
				f=open('/root/Desktop/dump/port.txt','r')
				y=f.read()
				os.system("dialog --no-shadow --infobox 'Please wait till the processing is being done...' 10 50")
				os.system("nmap -p U:"+y+" "+x+" > /root/Desktop/dump/result")
				os.system("dialog --no-shadow --textbox /root/Desktop/dump/result 20 100")	

	
			if d=='4':
				os.system("dialog --no-shadow --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/dump/hello.txt")
				f=open('/root/Desktop/dump/hello.txt','r')
				x=f.read()
				os.system("dialog --no-shadow --inputbox 'Enter the number of ports that you want to scan : ' 10 50 2> /root/Desktop/dump/choice")
				f=open('/root/Desktop/dump/choice','r')
				z=f.read()
				q=int(float(z))
				while q>0 :
					os.system("dialog --no-shadow --inputbox 'Enter Port Number : ' 10 50 2>> /root/Desktop/dump/port.txt")
					f1=open('/root/Desktop/dump/port.txt','ab')
					f1.write(",")
					f1.close()
					q=q-1
				f1=open('/root/Desktop/dump/port.txt','r')
				y=f1.readline()
				os.system("dialog --no-shadow --infobox 'Please wait till the processing is being done...' 10 50")
				os.system("nmap -p "+y+" "+x+" > /root/Desktop/dump/result")
				os.system("dialog --no-shadow --textbox /root/Desktop/dump/result 20 100")
				os.system("rm -f /root/Desktop/dump/port.txt")

			if d=='5':
				os.system("dialog --no-shadow --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/dump/hello.txt")
				f=open('/root/Desktop/dump/hello.txt','r')
				x=f.read()
				os.system("dialog --no-shadow --inputbox 'Enter Lower Limit of Port Number : ' 10 50 2>> /root/Desktop/dump/port.txt")
				f1=open('/root/Desktop/dump/port.txt','ab')
				f1.write("-")
				f1.close()
				os.system("dialog --no-shadow --inputbox 'Enter Upper Limit of Port Number : ' 10 50 2>> /root/Desktop/dump/port.txt")	
				f1=open('/root/Desktop/dump/port.txt','r')
				y=f1.readline()
				os.system("dialog --no-shadow --infobox 'Please wait till the processing is being done...' 10 50")
				os.system("nmap -p "+y+" "+x+" > /root/Desktop/dump/result")
				os.system("dialog --no-shadow --textbox /root/Desktop/dump/result 20 100")
				os.system("rm -f /root/Desktop/dump/port.txt")
			if d=='6':
				n()
			
		if c=='8':
			os.system("dialog --no-shadow --menu 'Intense Scanning Choices : ' 20 80 7 1 'Intense Scannning ' 2 'Internse Scanning + UDP  ' 3 'Intense Scanning - All TCP ' 4 'Intense Scanning - No Ping ' 5 'Scan a range of ports. ' 6 'Back ' 2> /root/Desktop/dump/choice.txt")
			f=open('/root/Desktop/dump/choice.txt','r')
			d=f.read()
			if d =='1':
				os.system("dialog --no-shadow --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/dump/hello.txt")
				f=open('/root/Desktop/dump/hello.txt','r')
				x=f.read()
				os.system("dialog --no-shadow --infobox 'Please wait till the processing is being done...' 10 50")
				os.system("nmap -T4 -A -v "+x+" > /root/Desktop/dump/result")
				os.system("dialog --no-shadow --textbox /root/Desktop/dump/result 20 60")

			if d =='2':
				os.system("dialog --no-shadow --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/dump/hello.txt")
				f=open('/root/Desktop/dump/hello.txt','r')
				x=f.read()
				os.system("dialog --no-shadow --infobox 'Please wait till the processing is being done...\nThis may take upto 10 minutes....\nIf you want to opt out press CTRL + C.. ' 10 50")
				os.system("nmap -sS -sU -T4 -A -v "+x+" > /root/Desktop/dump/result")
				os.system("dialog --no-shadow --textbox /root/Desktop/dump/result 20 60")

			if d=='3':
				os.system("dialog --no-shadow --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/dump/hello.txt")
				f=open('/root/Desktop/dump/hello.txt','r')
				x=f.read()
				os.system("dialog --no-shadow --infobox 'Please wait till the processing is being done...\nThis may take up some time..... \nIf Yoy want to opt out press CTRL + C.. ' 10 50")
				os.system("nmap -p 1-65535 -T4 -A -v "+x+" > /root/Desktop/dump/result")
				os.system("dialog --no-shadow --textbox /root/Desktop/dump/result 20 60")

			if d=='4':
				os.system("dialog --no-shadow --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/dump/hello.txt")
				f=open('/root/Desktop/dump/hello.txt','r')
				x=f.read()
				os.system("dialog --no-shadow --infobox 'Please wait till the processing is being done...\nThis may take up some time..... \nIf Yoy want to opt out press CTRL + C.. ' 10 50")
				os.system("nmap -Pn -T4 -A -v "+x+" > /root/Desktop/dump/result")
				os.system("dialog --no-shadow --textbox /root/Desktop/dump/result 20 60")
			
			if d=='5':
				n()


		if c=='9':
			os.system("dialog --no-shadow --inputbox 'Enter Host(s) IP Address : ' 10 50 2> /root/Desktop/dump/hello.txt")
			f=open('/root/Desktop/dump/hello.txt','r')
			x=f.read()
			os.system("dialog --no-shadow --infobox 'Please wait till the processing is being done..' 10 50")
			os.system("nmap -sS -O "+x+" > /root/Desktop/dump/result")
			os.system("cat /root/Desktop/dump/result | grep Running > /root/Desktop/dump/result1")
			os.system("dialog --no-shadow --textbox /root/Desktop/dump/result1 10 60")

		if c==10:
			exit()

	
	n()



