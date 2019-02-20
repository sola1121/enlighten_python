import datetime as dt
import numpy as np

n = 100000
start = dt.datetime.now()

A, B = list(), list()
for i in range(n):
    A.append(i**2)
    B.append(i**3)

C = list()
for a, b in zip(A, B):
    C.append(a+b)
print("python实现的时间:", (dt.datetime.now()-start).microseconds)
start = dt.datetime.now()
C = np.arange(n) ** 2 + np.arange(n) ** 3
print("使用numpy的时间:", (dt.datetime.now()-start).microseconds)
