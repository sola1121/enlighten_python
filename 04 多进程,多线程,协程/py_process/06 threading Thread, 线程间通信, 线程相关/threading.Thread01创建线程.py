import time, threading

def music():
    while True:
        time.sleep(2)
        print("放音乐")

# 创建线程对象, 与music绑定
th = threading.Thread(target=music)

# 启动线程
th.start()

while True:
    time.sleep(1.5)
    print("听啥歌")

# 等待回收线程
th.join()

print("+++++++++++++++++++++++")
