#!/usr/bin/env python3

import sys
import socket

if len(sys.argv) < 3:
    print("Didn't input host & port\nYou need input it as:\n   python3 filename host port")
try:
    host = sys.argv[1]
    port = sys.argv[2]
except:
    host = '127.0.0.1'
    port = 12345 

ADDR = (host, int(port))

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

while True:
    data = input("Client Input: ")
    if not data:
        break

    client.sendto(data.encode(), ADDR)
    data, addr = client.recvfrom(1024)
    print("Server Returned Message: ", data.decode())

client.close()
