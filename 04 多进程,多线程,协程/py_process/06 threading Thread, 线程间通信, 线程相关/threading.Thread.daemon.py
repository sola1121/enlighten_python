# daemon属性

import time
from threading import Thread, currentThread


def fun(sec):
    print("线程属性测试")
    time.sleep(sec)
    print("线程结束")


th = Thread(name="th_1", target=fun, args=(3,))

print("Daemon:",th.isDaemon())
th.daemon = True
print("Daemon:",th.isDaemon())

th.start()

print("thread name:", th.name)
print("alive:", th.is_alive())
print(currentThread().getName())
th.join(4)

print("========主线程结束=========")

