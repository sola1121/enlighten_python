import os, time
import multiprocessing as multip

def th1():
    print(os.getppid(), "-->", os.getpid())
    print("吃饭")
    time.sleep(1)
    print("睡觉")
    time.sleep(2)
    print("打豆豆")
    time.sleep(3)

def th2():
    print(os.getppid(), "-->", os.getpid())
    print("小明")
    time.sleep(2)
    print("小红")
    time.sleep(3)

def th3():
    print(os.getppid(), "-->", os.getpid())
    print("阿猫")
    time.sleep(2)
    print("阿狗")
    time.sleep(2)

# 创建三个新的进程, 关联上面三个事件
# 生成了进程对象分别表示这三个进程
p1 = multip.Process(target=th1)
p2 = multip.Process(target=th2)
p3 = multip.Process(target=th3)

# 通过生成的进程对象启动子进程
# 子进程有父进程的代码段, 只不过只执行对应的函数
p1.start()
p2.start()
p3.start()

print("Parent PID", os.getpid())

# 阻塞等待回收
p1.join()
p2.join()
p3.join()

print("+++++++++++++++++++")

# 其会运行在主进程上
th1()
th2()
th3()
