import re
import sys


def get_address(port_name):
    file = open(r"E:\达内学习文件\06 正则表达式\test_file.txt", "r")
    while True:
        data = str()
        for line in file:
            if line != "\n":
                data += line
            else:
                break
        if not data:
            break
        pattern = r"^\S+"
        PORT = re.match(pattern, data).group()
        if port_name == PORT:
            pattern = r"address is (\S+)"
            addr = re.search(pattern, data).group(1)
            return addr
        else:
            continue


if __name__ == "__main__":

    port = sys.argv[1]
    result = get_address(port)
    print(result)