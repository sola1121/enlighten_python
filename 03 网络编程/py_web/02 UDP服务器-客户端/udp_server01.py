#!/usr/bin/env python3

import sys
import time
import socket

if len(sys.argv) < 3:
    print("Didn't input host & port\nYou need input it as:\n   python3 filename host port")
try:
    host = sys.argv[1]
    port = sys.argv[2]
except:
    host = '127.0.0.1'
    port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
server.bind((host, int(port)))

while True:
    print("waiting...")
    client_data, addr = server.recvfrom(1024)
    print("Get Client %s:" % time.ctime(), client_data.decode(), addr)

    re_data = bytes("Server Got Message.", encoding='utf8')
    server.sendto(re_data, addr)

server.close()
