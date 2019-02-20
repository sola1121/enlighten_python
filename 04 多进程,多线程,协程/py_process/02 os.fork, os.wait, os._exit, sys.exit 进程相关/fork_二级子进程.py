import os, sys, time

# 创建一级子进程
pid_1 = os.fork()

if pid_1 < 0:
    print("一级子进程创建失败")
elif pid_1 == 0:
    print("一级子进程创建完毕")
    pid_2 = os.fork()   # 创建二级子进程
    if pid_2 < 0:
        print("二级子进程创建失败")
    elif pid_2 == 0:
        print("二级子进程创建完毕")
        print("开始二级子进程的工作")
    else:
        print("一级子进程将退出")
        os._exit(0)
else:
    print("根进程.")
    os.wait()   # 等待一级子进程退出
    print("一级子进程退出完毕")
    print("开始根进程的工作")
