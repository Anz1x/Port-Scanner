# A port scanner developed with Python 3.10.2. 
# Made by Anz
# Github: https://github.com/Anz1x

import socket
import os
import logging
from IPy import IP
import colorama
from colorama import Fore
import time

colorama.init(autoreset=True)

os.system("cls; clear")

print(Fore.GREEN + """

 ▒█▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ 　 ▒█▀▀▀█ █▀▀ █▀▀█ █▀▀▄ █▀▀▄ █▀▀ █▀▀█ 
 ▒█▄▄█ █░░█ █▄▄▀ ░░█░░ 　 ░▀▀▀▄▄ █░░ █▄▄█ █░░█ █░░█ █▀▀ █▄▄▀ 
 ▒█░░░ ▀▀▀▀ ▀░▀▀ ░░▀░░ 　 ▒█▄▄▄█ ▀▀▀ ▀░░▀ ▀░░▀ ▀░░▀ ▀▀▀ ▀░▀▀

[>] Port Scanner made by Anz
[>] Github: https://github.com/Anz1x
[>] When scanning multiple targets make sure to split the targets with a ','
""" + Fore.RESET +
"""
_________________________________________________________________________
""")
time.sleep(0.75)

logging.basicConfig(level=logging.INFO, format="%(message)s %(asctime)s", 
                    datefmt=time.strftime("%a, %d-%b-%Y %H:%M"))

def scan(target):
    converted_ip = check_ip(target)

    print(Fore.RESET + "_________________________________________________________________________")
    logging.info(Fore.RED + "\n" + "[-] Starting the scan on " + str(target) + " at")
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
            print(Fore.GREEN + "\n[+] Open Port: %s | Banner Results: %s" % (port, banner.decode().strip("\n")))
        except:
            print(Fore.GREEN + "\n[+] Open Port: %s" % (port))
    except:
        pass

targets = str(input(Fore.RED + "[+] Target(s): " + Fore.YELLOW))
if "," in targets:
    for ip_addr in targets.split(","):
        scan(ip_addr.strip(""))
else:
    scan(targets)

print("_________________________________________________________________________")
logging.info(Fore.RED + "\n[-] Scan completed for %s at" % (targets))
