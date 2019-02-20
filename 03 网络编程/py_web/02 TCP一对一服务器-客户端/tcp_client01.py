import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

client.connect(('127.0.0.1', 12346))

while True:
    msg = input("Client Input Message: ")
    if msg == 'quit':
        break
    client.send(bytes(msg, encoding="utf8"))

    server_data = client.recv(1024)
    print("server returned: ", server_data.decode())

client.close()
