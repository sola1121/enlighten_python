"""
实验一些常用的socket属性, 方法
"""

import socket

so = socket()

so.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)   # 设置端口立即重用
so.getsockopt(SOL_SOCKET, SO_REUSEADDR)   # 获取socket对应设置的值


so.fileno()   # 获取套接字的功能描述符

so.type   # 套接字类型

so.bind(('127.0.0.1', 12345))
so.getsockname()   # 获取绑定的地址

so.listen(20)
conn, addr= so.accept(2048)
conn.getpeername()   # 获取客户端的地址



