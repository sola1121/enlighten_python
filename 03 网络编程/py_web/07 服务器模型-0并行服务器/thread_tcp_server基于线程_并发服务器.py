import os
import sys
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


HOST = "127.0.0.1"
PORT = 12345
thread_lists = list()

# 处理具体的客户端请求
def handler(conn):
    print(conn.getpeername(), "link into server.")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(data)
        conn.send(b"Got Your Message.")
    conn.close()
        

# 创建套接字
server = socket(AF_INET, SOCK_STREAM, 0)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(20)


while True:
    try:
        conn, addr = server.accept()
    except Exception as e:
        print(e)
        continue
    th = Thread(target=handler, args=(conn,))
    th.daemon = True   # 主线程结束后, 回收分支线程
    th.start()

server.close()
