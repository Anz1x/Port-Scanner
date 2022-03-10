# A port scanner developed with Python 3.10.2. 
# Made by Anz
# Github: https://github.com/Anz1x

import socket
import time
from threading import Lock, Thread
import os
import logging
from IPy import IP

print("""
░█████╗░███╗░░██╗███████╗██╗░██████╗  ██████╗░░█████╗░██████╗░████████╗
██╔══██╗████╗░██║╚════██║╚█║██╔════╝  ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
███████║██╔██╗██║░░███╔═╝░╚╝╚█████╗░  ██████╔╝██║░░██║██████╔╝░░░██║░░░
██╔══██║██║╚████║██╔══╝░░░░░░╚═══██╗  ██╔═══╝░██║░░██║██╔══██╗░░░██║░░░
██║░░██║██║░╚███║███████╗░░░██████╔╝  ██║░░░░░╚█████╔╝██║░░██║░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝░░░╚═════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
      ░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
      ██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
      ╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
      ░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
      ██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
      ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
      
      
Port Scanner developed by Anz
Github: https://github.com/Anz1x
When scanning multiple targets make sure to split the targets with a ','
_________________________________________________________________________
""")
time.sleep(0.75)

logging.basicConfig(level=logging.INFO, format="%(message)s %(asctime)s", 
                    datefmt=time.strftime("%a, %d-%b-%Y %H:%M"))

def scan(target):
    converted_ip = check_ip(target)
    try:
        os.system("cls")
    except:
        pass
    try:
        os.system("clear")
    except:
        pass
    print("""
   _____                       _               _   _            _                       _   
  / ____|                     (_)             | | | |          | |                     | |  
 | (___   ___ __ _ _ __  _ __  _ _ __   __ _  | |_| |__   ___  | |_ __ _ _ __ __ _  ___| |_ 
  \___ \ / __/ _` | '_ \| '_ \| | '_ \ / _` | | __| '_ \ / _ \ | __/ _` | '__/ _` |/ _ \ __|
  ____) | (_| (_| | | | | | | | | | | | (_| | | |_| | | |  __/ | || (_| | | | (_| |  __/ |_ 
 |_____/ \___\__,_|_| |_|_| |_|_|_| |_|\__, |  \__|_| |_|\___|  \__\__,_|_|  \__, |\___|\__|
                                        __/ |                                 __/ |         
                                       |___/                                 |___/          
Port Scanner developed by Anz
Github: https://github.com/Anz1x
_________________________________________________________________________
    """)
    logging.info("\n" + "[-] Starting the scan on " + str(target) + " at")
    for port in range(4, 100):
        port_scan(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def port_scan(ip_address, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ip_address, port))
        try:
            banner = get_banner(s)
            print("\n[+] Open Port: %s | Banner Results: %s" % (port, banner.decode().strip("\n")))
        except:
            print("\n[+] Open Port: %s" % (port))
    except:
        pass

targets = str(input("[+] Target(s): "))
if "," in targets:
    for ip_addr in targets.split(","):
        scan(ip_addr.strip(""))
else:
    scan(targets)

print("_________________________________________________________________________")
logging.info("\n[-] Scan Completed for %s at" % (targets))
