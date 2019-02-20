import time
from multiprocessing import Array, Process

def fun(shm):
    for i in shm:
        print(i)
    else:
        print("-------------")
    shm[2] = 200

if  __name__ == "__main__":

    # 开辟共享内存空间, 可容纳6个整数
    # 初始值是[1, 2, 3, 4, 5, 6]
    # shm = Array('i', [1, 2, 3, 4, 5, 6])

    # 在共享内存中开辟一个包含6个整形的空间
    shm = Array('i', 6)   # 默认元素为0

    p = Process(target=fun, args=(shm,))
    p.start()
    p.join()

    for i in shm:
        print(i)

