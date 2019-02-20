import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

client.connect(('127.0.0.1', 12345))

for _ in range(5):
    client.send(b"Yes, Get")   # 快速发送5次, 会在服务器端看到粘连在一起的数据

data = client.recv(2048)
print(data.decode())


client.close()
