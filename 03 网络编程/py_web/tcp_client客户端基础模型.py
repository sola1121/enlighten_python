#!/usr/bin/env python3

import socket

# 创建套接字
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 发起连接
client.connect(('127.0.0.1', 12345))

# 发送消息
client.send(b'hello world.')

# 接收消息
data = client.recv(1024)
print("服务器消息返回:", data.decode())

# 关闭客户端套接字
client.close()
