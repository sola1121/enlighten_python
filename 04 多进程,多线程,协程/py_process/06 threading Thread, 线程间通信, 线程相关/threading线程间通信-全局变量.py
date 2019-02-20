import time
from threading import Thread

# 通过全局变量在线程中进行通信
a = 1

def foo():
    global a
    a = 1000

def bar():
    time.sleep(1)   # 确保让foo先执行
    print("a=", a)

th1 = Thread(target=foo)
th2 = Thread(target=bar)

th1.start()
th2.start()

th1.join()
th2.join()
