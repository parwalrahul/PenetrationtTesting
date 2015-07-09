#! /usr/bin/python2

import time
import os
import thread
import commands

while (2<3):
	l=commands.getoutput("tcpdump -i wlan0 -n icmp -c 100 -w /dev/null")
	os.system("\n\ngnome-terminal --window-with-profile='Rahul' --hide-menubar -t 'Alert' -x dialog --msgbox 'Somebody is trying something nasty on your system.\nCheck arp -a for attacker\nSetting Firewall Security.' 10 50 \n")
	os.system("iptables -I INPUT -p icmp -s DROP")
	time.sleep(5)

