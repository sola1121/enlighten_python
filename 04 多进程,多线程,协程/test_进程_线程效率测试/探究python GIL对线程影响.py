import time
from threading import Thread
from multiprocessing import Process

# 计算密集型
x, y , z = 0, 0 ,0
def calculate():
    global x, y , z
    for _ in range(10000000):
        x += 1
        y += 1
        z += 1

# IO密集型
def write():
    f = open("test.txt", 'w')
    for x in range(10000000):
        f.write("hello_world%d\n" % x)
    f.close()

def read():
    f = open("test.txt", 'r')
    content = f.readlines()
    f.close()


def test_normal_time(*args):
    if len(args) == 2:
        start_time = time.time()
        args[0]()
        args[1]()
        return time.time() - start_time
    if len(args) == 1:
        start_time = time.time()
        args[0]()
        return time.time() - start_time


def test_thread_time():
    """"""
    jobs = list()
    start_time = time.time()
    for _ in range(4):
        th = Thread(target=calculate)
        jobs.append(th)
        th.start()
    for th in jobs:
        th.join()
    print("thread CPU:",time.time() - start_time)
    
    jobs = list()
    def IO_run():
        write()
        read()
    start_time = time.time()
    for _ in range(4):
        th = Thread(target=IO_run)
        jobs.append(th)
        th.start()
    for th in jobs:
        th.join()
    print("thread IO:",time.time() - start_time)


if __name__ == "__main__":

    print("计算密集", test_normal_time(calculate))
    print("IO密集",test_normal_time(write, read))

    test_thread_time()
