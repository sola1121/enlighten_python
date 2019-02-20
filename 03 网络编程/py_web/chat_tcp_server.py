#!/usr/bin/env python3

# 使用 telnet 连接就可以

import socket

friend_name = None
my_name = 'limili'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
server.bind(('176.209.103.59', 12345))   # 176.209.103.59
server.listen(20)

print("等待连接...")
conn, addr = server.accept()
print("连接到的客户:", addr)

while True:
    if friend_name is None:
        conn.send(bytes("设置你的名字:", encoding='utf8'))
        friend_name = conn.recv(1024)
        friend_name = str(friend_name.decode()).replace("\r", "").strip()
        print(friend_name, "seted.")

    msg = input("%s 回复消息: " % my_name)
    if msg == 'quit':
        break
    msg = bytes("%s 回复消息: " % my_name + msg + '\n', encoding='utf8')
    conn.send(msg)

    data = conn.recv(1024)
    print("%s 说: " % friend_name, data.decode())
    
conn.close()
server.close()
