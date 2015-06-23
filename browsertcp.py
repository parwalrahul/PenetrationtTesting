#! /usr/bin/python2

import socket

s=socket.socket()

#ip="192.168.81.134"
port=80


ip=raw_input("Enter Web Site name or IP address : ")
page=raw_input("Enter Page name :")
s.connect((ip,port))
s.send("GET /" +page+ " HTTP/1.1\nHost:"+ip+"\n\n")

print s.recv(5000)


