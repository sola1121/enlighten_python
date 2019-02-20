#!/usr/bin/env python3

import socket

# 创建流式套接字
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

# 绑定IP和端口
server.bind(('127.0.0.1', 12345))

# 设置监听套接字, 创建监听队列
server.listen(20)

# 等待客户端连接
print("等待连接...")
conn, addr = server.accept()
print("连接到的客户:", addr)

# 收消息
data = conn.recv(1024)
print("收到的数据: ", data.decode())
# 发消息
msg = bytes("OJBK\n", encoding='utf8')
conn.send(msg)

# 关闭用户连接, 关闭服务器连接通道
conn.close()
server.close()
