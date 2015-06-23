#! /usr/bin/python

import signal

#Any two parameters(x,y / p,q / a,b etc) need to come here as for signal management of control + c we need to give 2 parameters here. 

def my(x,y):
	print "\n\n bye bye tc see u soon.\n\n "
	exit()

# THIS 2 BELOW IS USED TO INDICATE THAT THERE ARE 2 PARAMEMTERS IN THE FUNCTION my()

signal.signal(2,my)

x=raw_input("hello enter your name :")
print x
