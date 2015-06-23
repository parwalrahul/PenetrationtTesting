#! /usr/bin/python2

import os
import time
os.system("tput setaf 3")
print "\n\t\t\tWelcome to Rahul Programming Practise"
print "\t\t\t_____________________________________"
time.sleep(1)
os.system("tput setaf 0")

def nmcmd() :
	a=os.system("rpm -q nmap > /dev/null")
	if a==0:
	 print "nmap is already installed. "	
	else :
	 print " Nmap is not installed, Installing Nmap... "
	 os.system("yum install nmap -y")
	ip=raw_input("enter your IP Address : ")
	mask=raw_input("enter your subnet mask : ")
	os.system("nmap -sP "+ip+mask)


def menu():
     while (1):
	os.system("tput bold")
	print "\nMenu Options \n"
	print "Press 1 for printing today's date."
	print "Press 2 for printing this month's calender."
	print "Press 3 to create a file. "
	print "Press 4 to create a user. "
	print "Press 5 to logout a user. "
	print "Press 6 to show all hosts on your network and their IP(s). "
	print "Press 7 to exit. "
	choice=raw_input()
	if choice=='1' :
	 os.system("date")
	elif choice=='2':
	 os.system("cal")
	elif choice=='3':
	 fname=raw_input("Enter File name  ")
	 os.system("touch  "+fname)
	 print "File Successfully created on the Desktop. "
	elif choice=='4':
	 uname=raw_input("Enter Username ")
	 os.system("adduser "+uname)
	 os.system("passwd "+uname)
	 print "User Successfully created"
	elif choice=='5':
	 uname=raw_input("Enter Username to logout ")
	 a=os.system("who | grep -w "+uname)
	 if a!=0 :
	  print "user is not logged in currrently"
	 else : 
	  os.system("skill -KILL -u "+uname)
	  print "User successfully logged out"
	elif choice=='6' :
	 nmcmd()
	elif choice=='7' :
	 exit(0)
	 
menu()
raw_input()
