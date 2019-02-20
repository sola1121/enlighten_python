import sys

from socket import *
from select import *

server = socket()
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 12345))
server.listen(20)

# 创建IO事件地图
fdmap = {server.fileno(): server}
# 创建poll对象
po = poll()
# 将套接字加入到关注
po.register(server, (POLLIN | POLLERR))   # 关注server的POLLIN或POLLERR

while True:
    # 进行检测
    events = po.poll()   # 这是poll对象中的poll方法, 是一个阻塞函数
    for fd, event in events:   # 取准备好的序列号和事件
        if fd == server.fileno():
            conn, addr = fdmap[fd].accept()
            print("CONNECTED", addr)
            po.register(conn, POLLIN)
            fdmap[conn.fileno()] = conn
        elif event & POLLIN:
            data = fdmap[fd].recv(2048)
            if not data:
                po.unregister(fd)
                fdmap[fd].close()
                del fdmap[fdmap]
            else:
                print(data.decode())
                fdmap[fd].send("WELCOME".decode())


