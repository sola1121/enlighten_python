import sys, os
from socket import socket, error, AF_UNIX, SOCK_STREAM

# 确定用哪个文件进行通信
server_address = './test'

# 判断文件存在性, 如果已经存在需要处理
if os.path.exists(server_address):
    os.remove(server_address)

# 创建本地套接字
server = socket(AF_UNIX, SOCK_STREAM, 0)  # unix套接字

# 绑定本地套接字文件
server.bind(server_address)   # 会自动创建文件

# 设置监听队列
server.listen(20)

# 收发消息
while True:
    conn, addr = server.accept ()
    print("CONNECTED:", addr)
    while True:
        data = conn.recv(1024)
        print("GET:", data.decode())
        if data:
            conn.sendall(b"GET MESSAGE")
        else:
            break
    conn.close()

server.close
