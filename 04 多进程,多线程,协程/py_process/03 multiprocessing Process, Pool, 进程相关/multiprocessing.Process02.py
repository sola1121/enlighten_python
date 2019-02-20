import time, os
from multiprocessing import Process

x = 9

def worker(sec, msg):
    print("x", x)
    for i in range(3):
        time.sleep(sec)
        print("worker message:", msg)

# 位置传参
# p = Process(target=worker, args=(2, 'hello'))

# 位置传参和字典传参混合 
p = Process(target=worker, args=(2,), kwargs={"msg": "hello"})

p.start()
print("进程p的pid:", p.pid, "父进程", os.getppid())

p.join()
