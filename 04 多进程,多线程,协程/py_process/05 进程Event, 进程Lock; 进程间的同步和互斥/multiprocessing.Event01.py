
from multiprocessing import Event

et = Event()

print(et.is_set())

et.set()

a = et.wait(3)

print(et.is_set())

# 将设置清除, wait又将阻塞
et.clear()

et.wait(5)

print("wait等到set事件后的返回值", a)
