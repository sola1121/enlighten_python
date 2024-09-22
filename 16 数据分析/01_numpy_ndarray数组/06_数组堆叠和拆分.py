import numpy as np

a = np.arange(11, 20).reshape(3, 3)
b = np.arange(21, 30).reshape(3, 3)
print(a, "\n", b, sep="")

c = np.vstack((a, b))   # 上下组合
print(c)
x, y = np.vsplit(c, 2)   # 上下拆分两份
print(x, "\n", y, sep="")

c = np.hstack((x, y))   # 左后组合
print(c)
x, y = np.hsplit(c, 2)   # 左右拆分两份
print(x, "\n", y)

c = np.dstack((x, y))
print(c)
x, y = np.dsplit(c, 2)
print(x, "\n", y)
x = a.T
y = b.T

c_row = np.row_stack((a, b))
c_colum = np.column_stack((a, b))
print(c_row, c_row.ndim)
print(c_colum)
