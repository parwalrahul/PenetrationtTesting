#! /usr/bin/python2

import os
import time
import signal


def hello(x,y):
	os.system("ifconfig wlan0 up")
	os.system("service network restart > /dev/null")
	



signal.signal(2,hello)

def a():
	while True :
		i=2
		while i<252:
			p=str(i)
		 	os.system("ifconfig wlan0 192.168.1."+p)
			os.system("ifconfig wlan0 down")
			os.system("macchanger -r wlan0 > /dev/null")
			os.system("ifconfig wlan0 up")
			time.sleep(5)
			i=i+1




