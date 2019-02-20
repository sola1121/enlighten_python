import os
import sys
import time
import signal
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

# 文件库位置
FILE_PATH = "/home/tarena/桌面/"


class TFTPserver():

    def __init__(self, conn):
        self.conn = conn

    def do_list(self):
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.conn.send(b"NO")
            return
        else:
            self.conn.send(b"YES")
        time.sleep(0.1)   # 防止粘包
        filenames = str()
        for filename in file_list:
            if filename[0] != "." and os.path.isfile(FILE_PATH + filename):   # 排除隐藏.开头的文件和目录
                filenames += filename + "``"
        self.conn.send(filenames.encode())
        
    def do_get(self, filename):
        try:
            file = open(FILE_PATH+filename, 'rb')
        except:
            self.conn.send(b"NO")
            return
        self.conn.send(b"YES")
        time.sleep(0.1)
        while True:
            file_data = file.read(1024)
            if not file_data:
                file.close()
                time.sleep(0.1)
                self.conn.send(b"``eof")
                break
            self.conn.send(file_data)

    def do_put(self, filename):
        try:
            file = open(FILE_PATH+filename, 'wb')
        except:
            self.conn.send(b"NO")
            return
        self.conn.send(b"YES")
        while True:
            file_data = self.conn.recv(1024)
            if file_data == b'``eof':
                print(time.ctime(), "接收", filename)
                file.close()
                break
            file.write(file_data)

    def do_quit(self):
        print("客户端退出", time.ctime())
        sys.exit(1)


def main():
    if len(sys.argv) != 3:
        HOST = ""
        PORT = 12345
    else:        
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)
    BUFFERSIZE = 1024

    server = socket(AF_INET, SOCK_STREAM, 0)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind(ADDR)
    server.listen(20)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    while True:
        try:
            conn, addr = server.accept()
        except KeyboardInterrupt:
            server.close()
            sys.exit(0)
        except Exception:
            continue
        print("客户登入", time.ctime(), addr)

        pid = os.fork()
        if pid < 0:
            print("Failed to create child process")
            continue
        elif pid == 0:
            server.close()
            # 创建与客户端通讯对象
            tftp_server = TFTPserver(conn)
            while True:
                request = conn.recv(BUFFERSIZE).decode()
                request = request.split("``")
                if request[0] == "list2server":
                    tftp_server.do_list()
                elif request[0] == "get2server":
                    filename = request[-1]
                    tftp_server.do_get(filename)
                    print(conn.getpeername(), time.ctime() ,"try to download file %s" % filename)                    
                elif request[0] == "put2server":
                    filename = request[-1]
                    tftp_server.do_put(filename)
                    print(conn.getpeername(), time.ctime(), "try to upload file %s" % filename)
                elif request[0] == "quit2server":
                    tftp_server.do_quit()
        else:
            conn.close()
            continue


if __name__ == "__main__":

    main()

