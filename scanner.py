#!/bin/python3

import sys
import socket
from datetime import datetime
#import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
	#target = sys.argv[1:]  # Store all IP addresses

else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
	#sys.exit()  # Exit the program if the argument is not correct
			
#Add a pretty banner
print("-" * 50)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85) :
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(2)
		print(f"scanning port {port} on {target}")
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open")
	
	    
    
		else:
			print(f"port {port} is closed")

		s.close()
		
except KeyboardInterrupt:
	print("\nExiting program.")
				
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
				
	
except socket.error:
		print("Could not connect to server.")
		sys.exit()
		
