import time
from threading import Thread, currentThread

def fun(sec):
    print("线程属性测试")
    time.sleep(sec)
    print("线程结束")

jobs = list()
for i in range(3):
    th = Thread(name="th_%d" % i, target=fun, args=(3,))
    th.start()
    jobs.append(th)

for th in jobs:
    print("thread name:", th.name)
    print("alive: ", th.is_alive())
    print(currentThread().getName())
    th.join()
