import sys, time
from multiprocessing import Process, Lock


# 创建一个Lock对象
lock = Lock()

# worker 共用一个资源, 谁先抢到谁先输出
# 要使用锁就都使用锁, 这样两者才会有锁
# sys.stdout为所有进程的共有资源
def worker1():
    lock.acquire()   # 上锁
    for _ in range(5):
        time.sleep(1)
        sys.stdout.write("worker1 输出\n")
    lock.release()   # 解锁


def worker2():
    with lock:   # 用with的方式上锁解锁
        for _ in range(5):
            time.sleep(1)
            sys.stdout.write("worker2 输出\n")


w1 = Process(target=worker1)
w2 = Process(target=worker2)

w1.start()
w2.start()

w1.join()
w2.join()
