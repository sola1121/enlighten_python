import time, signal

# 3秒后向自己发送个SIGALRM信号
signal.alarm(3)

while True:
    time.sleep(1)
    print("等待时钟...")
