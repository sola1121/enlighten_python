import signal, time

signal.alarm(5)

# 使用默认的方法处理SIGALRM信号
# signal.signal(signal.SIGALRM, signal.SIG_DFL)

# 忽略信号, 异步执行, 不会造成阻塞
signal.signal(signal.SIGALRM, signal.SIG_IGN) 

while True:
    time.sleep(2)
    print("等待时钟...")
