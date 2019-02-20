import socket

# 创建数据报套接字
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

# 绑定服务端地址
server.bind(('127.0.0.1', 12345))

# 接收客户端消息
client_data, addr = server.recvfrom(1024)
print(client_data.decode(), addr)

# 向客户端发送消息
server.sendto("OJBK".encode(), addr)

# 关闭套接字
server.close()
