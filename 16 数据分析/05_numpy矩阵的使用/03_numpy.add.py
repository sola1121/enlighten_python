import numpy as np


arr = np.arange(1, 7)
print(arr)

b = np.add.reduce(arr)
print(b)

c = np.add.accumulate(arr)
print(c)

d = np.add.reduceat(arr, [0, 3, 5])
print(arr[0], arr[3], arr[5], d)

e = np.add.outer([10, 20, 30], arr)   # 外和
print(e)

e = np.outer([10, 20, 30], arr)   # 外积
print(e)
