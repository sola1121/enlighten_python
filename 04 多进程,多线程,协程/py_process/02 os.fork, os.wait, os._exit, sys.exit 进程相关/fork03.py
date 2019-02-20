import os, time

pid = os.fork()

if pid < 0:
    print("进程创建失败.")
elif pid == 0:
    time.sleep(0.1)
    print("---子进程---")
    print("子进程", os.getpid(), "父进程", os.getppid())
elif pid > 0:
    print("---父进程---")
    print("本进程", os.getpid(), "子进程", pid)

