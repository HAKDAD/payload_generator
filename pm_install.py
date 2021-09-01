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
os.system('clear')
os.system('mkdir /root/hakdad_generated_payloads')
print("\033[92m\nDIRECTORY CREATED AT /root/hakdad_generated_payloads")
print ("                          ")
print ("\033[93m----INSTALLING DEPENDENCIES----")
print ("                          ")
app = ("install")
subprocess.call(["apt", "update -y"])
subprocess.call(["apt", app, "python -y"])
subprocess.call(["apt", app, "python2 -y"])
subprocess.call(["apt", app, "toilet -y"])
subprocess.call(["apt", app, "lolcat -y"])
subprocess.call(["apt", app, "figlet -y"])
time.sleep(3)
print ("\033[91m\n---- RUN THIS ONLY ONCE ----")
print ("\033[91m\n---- YOU SHOULD HAVE METASPLOIT AND APK TOOL INSTALLED ----")
print ("\033[92m\n---- REQUIREMENTS INSTALLED \nNOW USE ' python pm_main.py ' TO USE THE TOOL ----")
##############################################
##############################################

