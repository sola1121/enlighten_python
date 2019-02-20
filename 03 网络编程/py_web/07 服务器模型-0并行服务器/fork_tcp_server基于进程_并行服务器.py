# 每连接一个客户端, 就会创建一个新进程
# 使用os.fork和signal, 只对linux或unix系统有用

import os
import sys
import time
import signal
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

HOST = ""
PORT = 12345


def client_handler(conn):
    try:
        print("子进程接收客户端的请求", conn.getpeername())
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(time.ctime(), data)
            conn.send(b"GOT MESSAGE")
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception as e:
        print(e)
    conn.close()
    sys.exit(1)


server = socket(AF_INET, SOCK_STREAM, 0)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(20)

print("父进程%d等待客户端连接" % os.getpid())

while True:
    try:
        conn, addr = server.accept()
    except KeyboardInterrupt:
        raise
    except Exception as e:
        continue
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)   # 处理了僵尸进程, 即忽略退出的子进程
    # 为新的客户端创建进程
    pid = os.fork()
    if pid < 0:
        print("Failed to create child process")
        conn.close()
        continue
    elif pid == 0:
        server.close()
        client_handler(conn)   # 处理客户端请求
        pass
    else:
        conn.close()
        continue   # 父进程继续接收客户端的请求
