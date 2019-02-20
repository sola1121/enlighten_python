import os, sys
import time

pid = os.fork()

if pid < 0:
    print("Create process failed.")
elif pid == 0:
    print("New process created.")
    time.sleep(2)
    sys.exit(2)
else:
    # 设置为非阻塞状态, 循环处理查看子进程的状态
    while True:    
        print("The original process.")
        time.sleep(1)
        wait_pid, status = os.waitpid(-1, os.WNOHANG)
        print(wait_pid, status)
    while True:
        pass

