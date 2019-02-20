import os, signal

print(os.getpid())

# 自己干自己
os.kill(os.getpid(), signal.SIGKILL)
