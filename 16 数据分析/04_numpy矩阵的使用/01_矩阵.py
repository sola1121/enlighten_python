import numpy as np

a = [[1, 2],
    [3, 4]]
mtx1 = np.matrix(a)
print(mtx1, type(mtx1))

mtx2 = np.mat(mtx1)
print(mtx2, type(mtx2))

mtx3 = mtx2 * 3
print(mtx1, mtx2, mtx3, sep="\n")

mtx4 = np.mat("1 2; 3 4")
print("\nmtx4\n", mtx4)

print("转置:\n", mtx4.T)
print("取逆:\n", mtx4.I)


