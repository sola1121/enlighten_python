import socket

client = socket.socket()

client.connect(('127.0.0.1', 12345))

while True:
    msg = input("to send message:" )
    if not msg:
        break
    client.send(msg.encode())

    data = client.recv(2048)
    print("receive:", data.decode())
