import socket

client = socket.socket()

client.connect(('127.0.0.1', 12345))

file = open("recv_file", "wb")

# 每次从服务端接收一定大小
while True:
    data = client.recv(4096)
    if data == b"EOF":   # 当接收到的单个内容为EOF时, 结束接收
        break
    file.write(data)

file.close()
client.close()
