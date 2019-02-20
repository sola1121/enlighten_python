import numpy as np


a = np.array([5, 5, -5, -5])
b = np.array([2, -2, 2, -2])
print("a", a, "   b", b)

c = np.true_divide(a, b)
d = np.divide(a, b)
print("c", c, "  d", d, "  a/b", a/b)

f = np.floor_divide(a, b)
print("f", f, "   a//b", a//b)

h = np.ceil(a/b).astype(int)   # 天花板除
print(h)
i = np.trunc(a/b).astype(int)   # 截断除
print(i)
j = (a/b).astype(int)   # 和截断trunc一样
print(j)