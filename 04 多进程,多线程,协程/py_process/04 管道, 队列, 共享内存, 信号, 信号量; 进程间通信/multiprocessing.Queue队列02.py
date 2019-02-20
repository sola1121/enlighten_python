import time
from multiprocessing import Process, Queue


def fun1():
    time.sleep(1)
    qu.put("I'm fun1")

def fun2():
    time.sleep(2)   # 睡眠2s, 保证fun1执行完毕
    print("get from queue:", qu.get())


# 创建消息队列
qu = Queue()

# 创建两个子进程让其进行通信
p1 = Process(target=fun1)
p2 = Process(target=fun2)
p1.start()
p2.start()

p1.join()
p2.join()

