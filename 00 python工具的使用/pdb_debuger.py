import pdb
import sys

def add(num1=0, num2=0):
    return int(num1) + int(num2)

def sub(num1=0, num2=0):
    return int(num1) - int(num2)

def main():
    print(sys.argv)
    # 设置断点
    pdb.set_trace()
    addition = add(sys.argv[1], sys.argv[2])
    print(addition)
    subtraction = sub(sys.argv[1], sys.argv[2])
    print(subtraction)

main()

# 在断点时使用pdb中的命令来对程序的运行进行操作
