import sys

import socket

old = sys.stdout
sys.stdout = open("socket_doc.txt", 'w')

help(socket)

sys.stdout.close()
sys.stdout = old
