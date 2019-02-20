import socket, time, traceback

server = socket.socket()
server.bind(('127.0.0.1', 12345))
server.listen(20)

server.settimeout(5)   # 设置超时检测, 等待5秒, 过了5秒没有其下属的阻塞函数没有得到响应, 结束阻塞

while True:
    print("WAITING...")
    try: 
        conn, addr = server.accept()   # 第一个阻塞函数, 被设置超时
    except Exception:
        traceback.print_exc()
        continue
    print("CONNECT", addr)
    # recv设置超时等待
    # conn.settimeout(5)
    while True:
        data_recv = conn.recv(2048)
        if data_recv.decode() == "END":
            break
        print(data_recv.decode())
        conn.send(b"SECCESS LINK")

    conn.close()

server.close()
