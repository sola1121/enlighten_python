import sys

from socket import *
from select import select

server = socket()
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 12345))
server.listen(20)

# 将关注的IO放入rlist
rlist = [server]
wlist = []
xlist = [server]

while True:
    print("WAITING IO...")
    # wlist中有内容, select会立即返回
    rs, ws, xs = select(rlist, wlist, xlist, 5)   # 设置了超时5s, 5s后如果没有IO, 那就重新再执行while循环了

    for r in rs:
        # 表示服务器套接字准备就绪
        if r is server:
            conn, addr = r.accept()   # server.accept()
            print("CONNECTED", addr)
            # 将新的客户端用户套接字加入到关注列表
            rlist.append(conn)
        else:
            data = r.recv(2048)   # 这里的r是客户端套接字, 不是server
            if not data:
                # 客户端返回空消息, 退出连接的处理
                rlist.remove(r)
                r.colse()
            else:
                print("RECEIVED<<<", r.getpeername(), data.decode())
                wlist.append(r)   # 加入了wlist, select将会主动的去处理

    for w in ws:
        w.send("_WELCOME_".encode())
        wlist.remove(w)

    for x in xs:
        if x is server:
            server.close()
            sys.exit(1)

# 理解, rlist读列表相当于IO的Input, 它获取输入, wlist写列表相当于IO的Output, 它输出消息
# selec下的三个循环执行的顺序可以这样理解, 首先从selec中阻塞的Input中获取输入, 在将要把输出的传递给Output

