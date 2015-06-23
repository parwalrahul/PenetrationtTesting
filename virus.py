#! /usr/bin/python2

import time
import os
import thread

def ff():
	os.system("firefox &")
	os.system("echo $! > /root/Desktop/Project/hello.txt")

os.system("tcpdump -i eth0 -n icmp -c 4 -w /root/Desktop/Project/hello123.txt")
os.system("\n\nfirefox &\n")
os.system("echo $! > /root/Desktop/Project/hello.txt")
while True :
	f=open('/root/Desktop/Project/hello.txt','r')
	x=f.read()
	a=os.system("ps "+x)
	time.sleep(5)
	if a !=0 :
		ff()
	else :
		time.sleep(5)
		pass







"""
def vir():
	thread.start_new_thread(ff,())
	thread.start_new_thread(ff,())
"""
