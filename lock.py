#! /usr/bin/python2

import os
import time

def a() :
	os.system("dialog --no-shadow --no-shadow --infobox '	  Welcome to the File locker  ' 10 40") 
	time.sleep(2)
	os.system("dialog --no-shadow --menu 'Select Your Choice : ' 20 100 5 1 'Lock a File ' 2 'Unlocked a File. ' 3 'Back'  2> /root/Desktop/Project/choice.txt")
	f=open('/root/Desktop/Project/choice.txt','r')
	c=f.read()

	if c=='1':
		os.system("dialog --no-shadow --inputbox 'Enter location of the file to be locked : ' 10 50 2> /root/Desktop/Project/loc")
		f=open('/root/Desktop/Project/loc','r')
		a=f.read()
		f=open('/root/indexlock.txt','a')
		f.write(a)
		f.write("\n")
		f.close()
		os.system("openssl base64 -e -in "+a+" -out "+a+"1")
		os.system("mv -f "+a+"1 "+a)
		os.system("dialog --no-shadow --msgbox 'The file has been locked now' 10 50")


	if c=='2':
		os.system("dialog --no-shadow --inputbox 'Enter location of the file to be unlocked : ' 10 50 2> /root/Desktop/Project/unloc")
		f=open('/root/Desktop/Project/unloc','r')
		a=f.read()
		os.system("openssl base64 -d -in "+a+" -out "+a+"1")
		os.system("mv -f "+a+"1 "+a)
		os.system("dialog --no-shadow --msgbox 'The file has been Unlocked now' 10 50")

	if c==3:
		exit()	

