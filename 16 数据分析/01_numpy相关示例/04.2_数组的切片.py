import numpy as np

a = np.arange(1, 10)
print(a)   # [1 2 3 4 5 6 7 8 9]
print(a[:3])   # [1 2 3]
print(a[3:6])   # [4 5 6]
print(a[6:])   # [7 8 9]
print(a[::-1])   # 逆序输出
print(a[:-4:-1])   # [9 8 7]
print(a[-4:-7:-1])   # [6 5 4]
print(a[-7::-1])   # [3 2 1]
print(a[::])   # 整个输出 print(a[...])   print(a[:])
print(a[::3])   # [1 4 7]
print(a[2::3])   # [3 6 9]

print("\n====================\n")

b = np.arange(1, 25).reshape(2, 3, 4)   # 更改形状, 2个元素, 3行4列
print(b)
print(b[:, 0, 0])   # [1 13]   # 所有元素, 下标0行, 下标0列
print(b[0, :, :])  # 下标0元素, 行所有, 列所有  
print(b[0, ...])   # 下标0元素, 行所有, 列所有 

print(b[0, 1, ::2])   # [5 7]
print(b[..., 1])   # 所有元素, 列1
print(b[:, 1])   # 所有元素, 下标1行