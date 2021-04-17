#!/bin/python3

import sys
import socket
import threading
import concurrent.futures
from datetime import datetime

name = """\u001b[31m
______                                    
| ___ \                                   
| |_/ /__  ___ __ _ _ __  _ __   ___ _ __ 
|  __/ __|/ __/ _` | '_ \| '_ \ / _ \ '__|
| |  \__ \ (_| (_| | | | | | | |  __/ |   
\_|  |___/\___\__,_|_| |_|_| |_|\___|_| v1.0
                               \u001b[0m 
           
               \u001b[3m -  small port scanner by <CyborJ                        
     """


print(name)


print_lock = threading.Lock()

ip = input("Enter the IP or Domain to scan: ")

print("\u001B[34m-" * 50)
print("\u001B[34mScanning Target " + ip)
print("\u001B[34mTime started: "+str(datetime.now()))
print("-" * 50)

def scan(ip,port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
       scanner.connect((ip,port))
       scanner.close()
       with print_lock:
            print( f"\u001b[32m Port {port} is Open")

    except KeyboardInterrupt:
           print("\nQuit")
           sys.exit()
    
        
try:
       with concurrent.futures.ThreadPoolExecutor (max_workers=100) as executor:
             for port in range(1,1000):
                 executor.submit(scan, ip, port)

    
except KeyboardInterrupt:
      print("\u001B[6m\nExit once Again.")
      sys.exit()
