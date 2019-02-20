import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 12345))
server.listen(20)

while True:
    print("waiting for connecting...")
    conn, addr = server.accept()
    print("One use connected", addr)
    
    while True:
        re_data = conn.recv(2048)
        print(re_data.decode())
        
        if not re_data:
            break

        conn.send(b"GOT YOUR MESSAGE.")

    conn.close()

server.close()
