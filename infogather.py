#! /usr/bin/python

import os
import time
import commands
import signal

def a():

	def my(x,y):
		os.system("dialog --no-shadow --infobox 'Downloading Stopped.\nThank You.' 10 40")
		time.sleep(1)
		os.system("killall wget")	
		info()
  

	signal.signal(2,my)


	os.system("dialog --no-shadow --infobox ' Welcome to the Reconnaissance tool' 10 40") 
	time.sleep(2)
	def info():	
		os.system("dialog --no-shadow --menu 'Select Your Choice : ' 20 100 7 1 'Gather information about any website and it(s) owner.' 2 'Know the route to the server where website is hosted.' 3 'Download the Complete Website on your System.' 4 'Get info about Webserver & Website.' 5 'Back.' 2> /root/Desktop/Project/choice.txt")
		f=open('/root/Desktop/Project/choice.txt','r')
		c=f.read()
		if c=='1':
			os.system("dialog --no-shadow --inputbox 'Enter website name : (Example : google.com) ' 10 50 2> /root/Desktop/Project/hello.txt")
			f=open('/root/Desktop/Project/hello.txt','r')
			x=f.read()
			os.system("dialog --no-shadow --infobox '  Fetching Data.. ' 10 40")
			os.system("whois -H "+x+" > /root/Desktop/dump/info" +x)
			os.system("sed -i 's/WHOIS/master/g' /root/Desktop/dump/info"+x)
			os.system("sed -i 's/whois/master/g' /root/Desktop/dump/info"+x)
			os.system("dialog --no-shadow --textbox /root/Desktop/dump/info"+x+" 20 80")
			info()

		if c=='2':
			os.system("dialog --no-shadow --inputbox 'Enter website name : (Example : google.com) ' 10 50 2> /root/Desktop/Project/hello.txt")
			f=open('/root/Desktop/Project/hello.txt','r')
			x=f.read()
			os.system("dialog --no-shadow --infobox '  Fetching Data.. ' 10 40")
			os.system("traceroute "+x+" > /root/Desktop/dump/route"+x)
			os.system("dialog --no-shadow --textbox /root/Desktop/dump/route"+x+" 30 100")
			info()
		
		if c=='3':
			os.system("dialog --no-shadow --inputbox 'Enter Complete Website Address : (Example : https://www.google.com) ' 10 50 2> /root/Desktop/dump/site")
			f=open('/root/Desktop/dump/site','r')
			website=f.read()
			#os.system("cd /root/Desktop")
			os.system("dialog --no-shadow --msgbox 'The Website will be mirrored at the current working directory.' 10 50")
			os.system("dialog --no-shadow --infobox 'The Website Downloading Process Started.. Please wait for some time. \nPress Ctrl + C to stop downloading. ' 10 40")
			l=commands.getoutput("wget -m -p -E -k -K -np -v "+website+" > /dev/null")
			os.system("dialog --no-shadow --msgbox 'Website Successfully Captured' 10 50")
			info()


		if c=='4':
			os.system("dialog --no-shadow --inputbox ' Enter Website Address:\n(Example: www.google.com) ' 10 50 2> /root/Desktop/dump/site")
			f=open('/root/Desktop/dump/site','r')
			site=f.read()
			os.system("dialog --no-shadow --infobox 'The Information Gathering Process is going on.. \nPlease wait till the report is being processed. ' 10 40")
			l=commands.getoutput("curl -X GET -v "+site)
			f=open('/root/Desktop/result','w')
			f.write(l)
			f.close()
			#os.system("grep -A1000000 Host /root/Desktop/dump/result > /root/Desktop/dump/result1")
			os.system("dialog --no-shadow --msgbox 'The Report is stores at /root/Desktop/result' 20 80")
			info()

		if c==5:
			exit()
	
	info()


