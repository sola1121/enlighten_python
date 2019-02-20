import os, sys, time

pid = os.fork()

if pid < 0:
    print("Failed to create process.")
elif pid == 0:
    print("Child process.", os.getpid())
    time.sleep(3)
    sys.exit(3)   # 退出返回 3 * 256
else:
    ex_pid, status = os.wait()
    print("退出子进程: %s, 退出状态: %s" % (ex_pid, status))
    print(os.WEXITSTATUS(status))
