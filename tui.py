#! /usr/bin/python2

import os
import time

os.system("dialog --msgbox 'welcome to the python programming tui' 10 50")
os.system("dialog --infobox '    by rahul parwal' 20 80")
time.sleep(1)
#os.system("dialog --inputbox '  Enter your goodname ' 20 80 2>u.txt")
#os.system("dialog --passwordbox '  Enter your password ' 20 80 2>p.txt")

#os.system("dialog --menu 'SElect your choice' 20 80 4 A 'scan'  B 'virus detect' C 'poi' D 'hello'")
os.system("dialog --timebox ' Time is :' 10 30 23 03 52")
os.system("dialog --yesno ' Do you want to continue :' 10 30")
os.system("dialog --textbox /root/Desktop/myside.py 20 60")
os.system("dialog --form 'Dialog Sample Label and Values' 25 60 16 'Form Label 1:' 1 1 'Value 1' 1 25 25 30 'Form Label 1:' 1 1 'Value 111' 1 25 25 30  'Form Label 2:' 2 1 'Value 2' 2 25 25 30 'Form Label 3:' 3 1 'Value 3' 3 25 25 30 'Form Label 4:' 4 1 'Value 4' 4 25 25 30")


raw_input()

