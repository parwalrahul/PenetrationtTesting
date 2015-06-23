#!/usr/bin/python2

import socket
import thread

ip="192.168.43.70"
port=123456
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)

def a():
	s.bind((ip,port))
	while True : 
		x=s.recv(20)
		print x

def b():
	while True :
		data=raw_input()
		s.sendto(data,(ip,port))
	

thread.start_new_thread(a,())
thread.start_new_thread(b,())
