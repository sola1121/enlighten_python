import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
server.bind(('127.0.0.1', 12345))
server.listen(20)

while True:
    print("waiting for connecting...")
    conn, addr = server.accept()
    print("One use connected", addr)
    
    while True:
        re_data = conn.recv(1024)
        print("Client Returned:", re_data.decode())

        msg = input("Server Input message: ")
        if msg == 'quit':
            conn.close()
            break
        msg = bytes(msg, encoding='utf8')
        conn.send(msg)

    conn.close()

server.close()


# 写两个while是为了当客户端退出后, 服务端也不会终止, 保证第一层管道连接