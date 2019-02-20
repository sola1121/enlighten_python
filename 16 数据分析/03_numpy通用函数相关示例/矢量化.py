import numpy as np


def fun(a, b):
    return a+b, a-b, a*b

A = np.array([10, 20, 30])
B = np.array([100, 200, 300])

fun_vec = np.vectorize(fun)

C = fun_vec(A, B)
print(C)
