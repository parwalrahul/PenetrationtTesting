#! /usr/bin/python2

import os
import time

b=1
a=0
while a == 0 :
	c=str(b)
	a=os.system("fallocate -l "+c+"G  /root/hell"+c+" 2> /dev/null") 
	b=2*b


