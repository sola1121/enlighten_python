# coding: utf8
from multiprocessing import Queue

# 创建队列
qu = Queue(3)

qu.put(1)
print("is full?", qu.full())
qu.put(3)
qu.put(6, block=False)
print("is full?", qu.full())
qu.get()
qu.get()
qu.get(timeout=3)
print("is empty", qu.empty())
