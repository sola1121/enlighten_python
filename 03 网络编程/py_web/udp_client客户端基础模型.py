import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

addr = ('127.0.0.1', 12345)

# 向服务端发送消息
client.sendto("SEND FROM CLIENT.".encode(), addr)

# 从服务端接收消息
data, addr = client.recvfrom(1024)
print(data.decode(), addr)

# 关闭套接字
client.close()
