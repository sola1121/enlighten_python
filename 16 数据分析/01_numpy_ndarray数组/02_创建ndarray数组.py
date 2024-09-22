import numpy as np

a = np.arange(10)
print("a", a)

b = np.arange(1, 10)
print("b", b)

c = np.arange(1, 10, 3)
print("c", c)

d = np.array([])
print("d", d)

e = np.array([1, 2 ,3, 4, 5])
print("e", e)

f = np.array([
    [1,2,3],
    [4,5,6]
])
print("f", f)
print("type f", type(f))
print("f 0 0", type(f[0][0]))
print("f.dtype", f.dtype)

g = np.array(["one", "two", "three"], dtype=np.str_)   # 指定类型
print("g[0]", g[0])
print("g data type", g.dtype)

h = g.astype(np.str_)   # 以字符的形式拷贝
print("h", h)

i = np.array([
    [np.arange(1, 5), np.arange(5, 9), np.arange(9, 13)],
    [np.arange(13, 17), np.arange(17, 21), np.arange(21, 25)]
])
print("i.shape:", i.shape)
print("i value:\n", i)