import sys
import time
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


class TFTPclient():

    def __init__(self, client):
        self.client = client

    def do_list(self):
        self.client.send(b"list2server``")
        # 服务器回复 YES / NO
        repo = self.client.recv(1024).decode()
        if repo == "YES":
            repo_files = self.client.recv(1024).decode()
            repo_files = repo_files.split("``")
            for file in repo_files:
                print(file, end="   ")
            else:
                print()
        else:
            pass

    def do_get(self, filename):
        self.client.send(("get2server``%s" % filename).encode())
        repo = self.client.recv(1024).decode()
        if repo == "YES":
            file = open(filename, 'wb')
            while True:
                file_data = self.client.recv(1024)
                if file_data == b"``eof":
                    print(time.ctime(), "接收完成", filename)
                    file.close()
                    break
                file.write(file_data)
        else:
            print("Fail to get %s" % filename)


    def do_put(self, filename):
        try:
            file = open(filename, 'rb')        
        except:
            print(filename, "本地文件开启失败")
            return
        self.client.send(("put2server``%s" % filename).encode())
        repo = self.client.recv(1024).decode()
        if repo == "YES":
            while True:
                file_data = file.read(1024)
                if not file_data:
                    file.close()
                    time.sleep(0.1)
                    self.client.send(b"``eof")
                    print("本地传输完成.")
                    break
                self.client.send(file_data)
        else:
            print("服务器确认失败.")
                
    def do_quit(self):
        self.client.send(b"quit2server``")


def main():
    if len(sys.argv) != 3:
        HOST = ""
        PORT = 12345
    else:        
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)

    client = socket(AF_INET, SOCK_STREAM, 0)
    client.connect(ADDR)

    # 创建客户端请求对象
    tftp_client = TFTPclient(client)

    while True:
        print("\n\n========命令选项========")
        print("******** list *******")
        print("***** get file ******")
        print("***** put file ******")
        print("******** quit *******")

        comm = input("\ncommand>>> ")
        if comm.strip() == "list":
            tftp_client.do_list()
            print()
        elif comm[:3] == "get":
            filename = comm.split(" ")[-1]
            tftp_client.do_get(filename)
        elif comm[:3] == "put":
            filename = comm.split(" ")[-1]            
            tftp_client.do_put(filename)
        elif comm.strip() == "quit":
            tftp_client.do_quit()
            client.close()
            sys.exit(0)
        else:
            print("ERROR: 命令错误")


if __name__ == "__main__":

    main()

