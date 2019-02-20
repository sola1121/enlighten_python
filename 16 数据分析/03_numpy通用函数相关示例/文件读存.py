import numpy as np

a = np.arange(1, 10).reshape(3, 3)
print(a)

np.savetxt("./test.csv", a, delimiter=",", fmt="%d")

b = np.loadtxt("./test.csv", delimiter=",", usecols=(0, 2), dtype="i4")   # 以int32提取第一列和第三列的数据
print(b)

c, d = np.loadtxt("./test.csv", delimiter=",", usecols=(0, 2), unpack=True, dtype="i4, f8")
print("c:\n", c, "\n", "d:\n", d)