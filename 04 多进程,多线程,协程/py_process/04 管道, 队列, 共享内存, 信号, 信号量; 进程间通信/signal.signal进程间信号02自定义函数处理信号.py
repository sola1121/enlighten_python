import signal, time

signal.alarm(7)

# 自定义处理函数, 固定格式要求
def handler(sig, frame):
    if sig == signal.SIGALRM:
        print("收到时钟信号")
    elif sig == signal.SIGINT:
        print("老子就不结束")

# 通过自定义方法处理信号
signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGINT, handler)

while True:
    time.sleep(2)
    print("等待时钟...")
