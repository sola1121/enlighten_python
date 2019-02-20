import time, random
from multiprocessing import Value, Process

# 向共享内存存钱
def deposite(money):
    for i in range(100):
        time.sleep(0.03)
        money.value += random.randint(1, 200)

# 向共享内存取钱
def withdraw(money):
    for i in range(100):
        time.sleep(0.02)
        money.value -= random.randint(1, 150)

if __name__ == "__main__":

    # 创建共享内存对象, 初始值为2000
    money = Value('i', 2000)

    d = Process(target=deposite, args=(money,))
    w = Process(target=withdraw, args=(money,))

    d.start()
    w.start()

    d.join()
    w.join()

    print(money.value)
