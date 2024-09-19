import numpy as np

a = np.array([
    [1+1j, 2+4j, 3+7j],
    [4+2j, 5+5j, 6+8j],
    [7+3j, 8+6j, 9+9j]
])

print("元素类型:", a.dtype, "字节序:", a.dtype.str, "字符描述简写:", a.dtype.char)
print("数组形状:", a.shape, "数组维度:", a.ndim, "元素数:", a.size, len(a), "数组元素字节大小:", a.itemsize, "数组元素总字节大小:", a.nbytes, sep="  ")
print("视图转置:", a.T, "实部:", a.real, "虚部:", a.imag, sep="\n")

for elem in a.flat:   # 使用扁平迭代器
    print(elem, end="\t")
else:
    print()
print(a.flat[[1,2,4]])
a.flat[[2,4,6]] = 0
print(a)


def fun(a, b):
    a.append(b)
    return a

x = np.array([10, 20, 30])
y = 40
x = np.array(fun(x.tolist(), y))
print(x)
x = np.append(x, 50)
print(x)

