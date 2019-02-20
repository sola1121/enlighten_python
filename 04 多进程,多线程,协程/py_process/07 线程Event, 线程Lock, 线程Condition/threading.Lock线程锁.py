import threading, time

a = 0
b = 0

def value():
    lock.acquire()
    while True:
        if a != b:
            print("a=%d, b=%d" % (a,b))
    lock.release()

# 创建线程锁
lock = threading.Lock()

th = threading.Thread(target=value)

th.start()

#lock.acquire()
while True:
    # time.sleep(3)
    a += 1
    b += 1
#lock.release()

th.join()

