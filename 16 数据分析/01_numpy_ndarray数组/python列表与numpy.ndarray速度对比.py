import datetime as dt
import numpy as np

N = 100000

# 生成一个长列表, 该列表中的元素为另外两个列表的和, 另外的两个列表分别为N以内整数的平方和立方

# 使用Python生成一个长列表
def py_sum():
    # 记录开始时间
    start = dt.datetime.now()
    # 生成平方列表A, 立方列表B
    A, B = list(), list()
    for i in range(N):
        A.append(i**2)
        B.append(i**3)
    # 和列表C
    C = list()
    for a, b in zip(A, B):
        C.append(a+b)
    print("python实现的时间:", (dt.datetime.now()-start).microseconds)
    return C
    

# 使用numpy实现的长列表
def np_sum():
    # 记录开始时间
    start = dt.datetime.now()
    # 和列表C
    C = np.arange(N) ** 2 + np.arange(N) ** 3   # 矢量化, 不用编写循环便可对数组执行批量运算
    print("使用numpy的时间:", (dt.datetime.now()-start).microseconds)
    return C


if __name__ == "__main__":
    
    py_sum()
    np_sum()
