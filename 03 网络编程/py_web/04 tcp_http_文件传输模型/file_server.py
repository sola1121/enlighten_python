import socket
import time

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 12345))
server.listen(20)

# 接受客户端, 建立连接
conn, addr = server.accept()
print("CONNECTED", addr)

file = open("test_send_file", 'rb')

#　向客户端每次发送一定大小
while True:
    bin_data = file.read(4096)
    if not bin_data:
        time.sleep(0.5)   # 防止粘连
        conn.send(b"EOF")   # 发送结束标志
        break
    conn.send(bin_data)

file.close()
conn.close()
server.close()
