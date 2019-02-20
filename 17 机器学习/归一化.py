import numpy


A = numpy.mat('3 2000; 2 3000; 4 5000; 5 8000; 1 2000')
print("A=\n", A, end="\n\n")

# 均值为0, 极差为1
mu = A.mean(axis=0)
s = A.max(axis=0) - A.min(axis=0)
X = (A - mu) / s
print("X=\n", X, end="\n\n")

# 协方差矩阵
SIGMA = X.T * X

# 奇异值分解
U, S, V = numpy.linalg.svd(SIGMA)
print("U =\n", U, end="\n\n")

# 主成分特征矩阵
U_reduce = U[:, 0]
print("U_reduce =\n", U_reduce, end="\n\n")

# 降维样本
Z = X * U_reduce
print("Z =", Z, end="\n\n")


print("===进行数据恢复, 但是恢复后的数据是近似的.===\n")

# 恢复到均值极差转换之前
X_approx = Z * U_reduce.T
print("X_approx =\n", X_approx, end="\n\n")

# 恢复到原始样本
A_approx = numpy.multiply(X_approx, s) + mu
print("A_approx =\n", A_approx, end="\n\n")

