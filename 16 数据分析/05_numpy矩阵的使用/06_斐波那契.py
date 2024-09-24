import numpy as np

"""
 1 1    1 1    1 1
        1 0    1 0    1 0
1 1   2 1   3 2     5 3
1 0   1 1   2 1     3 2   ... 
f1f2 f3     f4       f5         fn
       F^2     3       4         n-1
"""

n = 30

# 1
def fibo(n):
    return 1 if n < 3 else fibo(n-1) + fibo(n-2)
print(fibo(n))

# 2
f1, f2 = 0, 1
for i in range(n):
    fn = f1 + f2
    f1, f2 = fn, f1
print(fn)

# 3
print(int((
    np.mat("1. 1.; 1. 0.") ** (n-1))[0, 0]))

# 4
r = np.sqrt(5)
print(int((((1 + r) / 2) ** n -
           ((1 - r) / 2) ** n) / r))
