import numpy as np


a = np.arange(1, 9)
print(a)

b = a.reshape(2, 4)   # 2行 4列
print(b)

c = b.reshape(2, 2, 2)   # 2元素 2行 2列
print(c)

d = c.ravel()   # 数组的一维
print(d)

e = c.flatten()   # 数组的一维副本
print(e)

a.shape = (2, 4)   # 直接将a变为2行4列
print(a)

a.T   # 转置
print(a)
a.transpose()   # 转置
print(a)

print("e++++++++++++++++e")
print(e)
# print(np.array([e].T))
print(e.reshape(-1, 1))   # 使用reshape的转置