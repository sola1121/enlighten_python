import time
from multiprocessing import Semaphore, Process, current_process

# 创建信号量初始为3 
sem = Semaphore(3)


def fun():
    print("进程%s等待信号量" % current_process())
    # 第四个进程无信号资源会阻塞
    sem.acquire()
    print("进程%s消耗信号量" % current_process())
    time.sleep(3)
    print("进程%s添加信号量" % current_process())
    sem.release()


jobs = list()
for _ in range(4):   # 会创建四个进程, 每个进程都会对信号量操作, 但是信号量为3
    p = Process(target=fun)
    p.start()
    jobs.append(p)

for p in jobs:
    p.join()
