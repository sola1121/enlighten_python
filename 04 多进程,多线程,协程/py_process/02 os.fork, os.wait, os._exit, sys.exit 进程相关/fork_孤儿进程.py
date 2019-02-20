import os, time

pid = os.fork()

if pid < 0:
    print("Create process failed.")
elif pid == 0:
    time.sleep(2)   # 保证创建孤儿
    print("Child process.\n", "Parent PID is", os.getppid())
elif pid > 0:
    print("Origianl process.", os.getpid())
