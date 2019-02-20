# os为系统相关模块, 不同的操作系统使用情况不同

import os

pid = os.fork()   # 子进程将从fork的下一步执行, 即赋值语句, 以免一直执行下去

if pid < 0:
    print("Fail to create new process.")
elif pid == 0:
    print("A new process is created.")
else:
    print("This is an intrinsic process.")

print("End")
