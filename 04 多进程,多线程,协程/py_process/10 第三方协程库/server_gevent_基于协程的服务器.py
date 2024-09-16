import gevent
from gevent import monkey
# 在导入socket前执行, 改变socket的阻塞形态
monkey.patch_all()

import time
from socket import socket, SOL_SOCKET, SO_REUSEADDR

def tcp_server(port):
    server = socket()
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind("0.0.0.0", port)
    server.listen(5)

    while True:
        conn, addr = server.accept()
        gevent.spawn(handler, conn)

def handler(conn):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("recv: ", data)
        conn.send(time.ctime().decode())
    conn.close()


if __name__ == "__main__":

    tcp_server(12345)
