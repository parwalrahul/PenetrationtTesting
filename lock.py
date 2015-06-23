#! /usr/bin/python2

import os
import time

def a() :
	os.system("dialog --infobox '	  Welcome to the File locker  ' 10 40") 
	time.sleep(2)
	os.system("dialog --menu 'Select Your Choice : ' 20 100 5 1 'Lock (Encrypt) a File ' 2 'Unlock (Decrypt) a file. ' 3 'Back'  2> /root/Desktop/Project/choice.txt")
	f=open('/root/Desktop/Project/choice.txt','r')
	c=f.read()

	if c=='1':
		os.system("dialog --inputbox 'Enter location of the file to be locked : ' 10 50 2> /root/Desktop/Project/loc")
		f=open('/root/Desktop/Project/loc','r')
		a=f.read()
		os.system("openssl genrsa 1028 > /root/Desktop/Project/private.txt")
		os.system("openssl rsa -in /root/Desktop/Project/private.txt -pubout > /root/Desktop/Project/public.txt")
		os.system("openssl rsautl -encrypt -inkey /root/Desktop/Project/public.txt -pubin -in "+a+" > /root/Desktop/Project/new.txt")
		os.system("mv -f /root/Desktop/Project/new.txt "+a)
		os.system("dialog --msgbox 'The file has been locked now' 10 50")


	if c=='2':
		os.system("dialog --inputbox 'Enter location of the file to be unlocked : ' 10 50 2> /root/Desktop/Project/loc")
		f=open('/root/Desktop/Project/loc','r')
		a=f.read()
		os.system("openssl rsautl -decrypt -inkey /root/Desktop/Project/private.txt -in "+a+" > /root/Desktop/Project/new.txt")
		os.system("mv -f /root/Desktop/Project/new.txt "+a)
		os.system("dialog --msgbox 'The file has been Unlocked now' 10 50")

	if c==3:
		exit()	

