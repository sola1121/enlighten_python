import numpy as np


a = np.arange(1, 6)
print("a:", a)
b = np.arange(6, 9)
print("b:", b)

c = np.convolve(a, b, "full")
print("完全卷积:", c)

c = np.convolve(a, b, "same")
print("同维卷积", c)

c = np.convolve(a, b, "valid")
print("有效卷积:", c)


