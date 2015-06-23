#! /usr/bin/python2

import signal
import os


def handler(signum, frame):
	os.system("dialog --infobox 'The internet bloccking has been stopped. \n Thank You. ' 20 50")    

signal.signal(signal.SIGTSTP, handler)


x=raw_input("hello enter your name :")
print x


