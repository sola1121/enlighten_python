import socket, time

server = socket.socket()
server.bind(('127.0.0.1', 12345))
server.listen(20)

server.setblocking(False)   # 设置非阻塞, 之后accept就不会发生阻塞了

while True:
    print("WAITING...")
    try: 
        conn, addr = server.accept()
    except BlockingIOError:
        time.sleep(3)
        print(time.asctime(time.localtime()))
        continue
    print("CONNECT", addr)
    # recv变为非阻塞
    # server.setblocking(False)
    while True:
        data_recv = conn.recv(2048)
        print(data_recv.decode())
        if data_recv.decode() == "END":
            break
        conn.send(b"SECCESS LINK")

    conn.close()

server.close()
