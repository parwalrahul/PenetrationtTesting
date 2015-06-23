#! /usr/bin/python2

f=open('/root/Desktop/Project/h','r')
z=f.read()
print z
g=open('/root/Desktop/Project/uname.txt','r')
#g.write(z)
f.seek(0)
while True :
	if g.readline()==z:
		print "success"

