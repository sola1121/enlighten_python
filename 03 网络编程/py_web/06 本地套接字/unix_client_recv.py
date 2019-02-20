import sys
from socket import socket, error, AF_UNIX, SOCK_STREAM

# 文件已经被创建
# 需要和另一端使用同一个socket文件
server_address="./test"

try :
    client = socket(AF_UNIX, SOCK_STREAM, 0)
    client.connect(server_address)
except error as e:
    print(e)
    sys.exit(1)

while True:
    msg = input(">>>")
    if msg:
        client.sendall(msg.encode())
        data = client .recv(1024)
        print(data.decode())
    else:
        break

client.close()