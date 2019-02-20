import os, time
import multiprocessing as multip

def th1():
    print("吃饭")
    time.sleep(1)
    print("睡觉")
    time.sleep(2)
    print("打豆豆")
    time.sleep(3)

def th2():
    print("小明")
    time.sleep(2)
    print("小红")
    time.sleep(3)

def th3():
    print("阿猫")
    time.sleep(2)
    print("阿狗")
    time.sleep(2)

# 当需创建进程较多时, 可以用列表一次创建和回收 
things = [th1, th2, th3]
p_ls = list()

for th in things:
    p = multip.Process(target=th, daemon=True)
    p_ls.append(p)
    p.start()

for p in p_ls:
    p.join()

print("+++++++++++++++++++")

