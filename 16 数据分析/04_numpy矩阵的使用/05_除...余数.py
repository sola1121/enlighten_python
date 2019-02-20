import numpy as np


a = np.array([5, 5, -5, -5])
b = np.array([2, -2, 2, -2])
print("a", a, "   b", b)

c = np.remainder(a, b)   # 地板除余数
d = np.mod(a, b)
e = a % b
print("c", c, "  d", d, "  e", e)

f = np.fmod(a, b)   # 截断除余数
print("f", f)
