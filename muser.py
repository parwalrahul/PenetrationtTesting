#! /usr/bin/python2

import os


def a():"""
	print "\n\t\t\tWelcome to Account Management Portal\n\n"
	print "Menu Options: \n"
	print "Press 1 to Add User Accout. "
	print "Press 2 to switch to an user. "
	print "Press 3 to logout an user. "
	print "Press 4 to Remove a User Account "
	print "Press 5 to Create a group "
	print "Press 6 to add multiple users to a group"
	print "Press 7 to exit "
	choice=raw_input()
	"""
	os.system("dialog --infobox '	  Welcome to the User Account Mangement ' 10 40") 
	time.sleep(2)
	os.system("dialog --menu 'Select Your Choice : ' 20 100 7 1 'Add User Account. ' 2 ' To switch to an user. ' 3 'To logout an user.' 4 'Remove User Account ' 5 'Create a group.' 6 'Add multiple users to a group. ' 7 'Exit'  2> /root/Desktop/Project/choice.txt")
	f=open('/root/Desktop/Project/choice.txt','r')
	c=f.read()
	if choice=='1':
	 os.system("dialog --inputbox 'Enter Username : ' 10 50 2> /root/Desktop/Project/uname.txt")
	 os.system("adduser "+uname)
	 os.system("passwd "+uname)
	elif choice=='2':
	 uname=raw_input("Enter Username : ")
	 os.system("su - "+uname)
	elif choice=='3':
	 uname=raw_input("Enter Username to logout ")
	 a=os.system("who | grep -w "+uname)
	 if a!=0 :
	  print "user is not logged in currrently"
	 else : 
	  os.system("skill -KILL -u "+uname)
	  print "User successfully logged out"
	elif choice=='4':
	 uname=raw_input("Enter Username : ")
	 a=os.system("userdel "+uname)
	 if a==0 :
	  print "The Account Deleted Successfully. "
	elif choice=='5' :
	 gname=raw_input("Enter Group Name:  ")
	 os.system("groupadd "+gname)
	 print("Group successfully created. ")
	elif choice=='6':
	 gname=raw_input("Enter Group Name ")
	 a=os.system("cat /etc/group | grep -w "+gname)
	 if a!=0 :
	  print "Group does not exist so please create a group first. "
	 else :
	  n=int(raw_input("Enter Number of Users that you want to add "))
	  while n>0 :
	   name=os.system("Enter the user name")
	   b=os.system("cat /etc/passwd | grep -w "+name)
	   if b!=0 :
	    print "There is no such user so create this user first."
	   else :	
	    os.system("usermod -G "+gname)
	    print "User added to the group."
	   n=n-1
	elif choice=='7':
	 exit(0)

	raw_input()
