import time
from multiprocessing import Event, Process

def wait_event():
    print("wait_event尝试使用临界区, 但是要阻塞等待主进程")
    et.wait()
    print("主进程操作完毕, wait_event开始", et.is_set())


def wait_event_timeout():
    print("wait_event_timeout尝试使用临界区, 但是要阻塞等待主进程")
    et.wait(2)   # 等两秒, 过了就算了
    print("wait_event_timeout不等待主进程, 开始执行其他", et.is_set())


et = Event()

p1 = Process(name="block", target=wait_event)
p2 = Process(name="non-block", target=wait_event_timeout)

p1.start()
p2.start()

print("正在忙碌的操作临界资源")
time.sleep(3)   # 主进程将会在三秒后对事件设置, 设置后有wait的进程就可以继续执行了
et.set()
print("主进程操作完了")

p1.join()
p2.join()
