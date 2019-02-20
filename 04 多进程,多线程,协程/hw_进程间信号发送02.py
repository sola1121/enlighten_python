import os, time, signal
import multiprocessing as mp

# 信号是异步运行
# 使用键盘是向所有站终端中运行的进程发送信号

SIGUSER1 = 60
SIGUSER2 = 61

def saler():
    signal.signal(signal.SIGTSTP, signal.SIG_IGN)    
    signal.signal(signal.SIGINT, saler_handler)
    signal.signal(signal.SIGQUIT, saler_handler)
    signal.signal(SIGUSER1, saler_handler)
    while True:
        time.sleep(3)
        print("等待信号")


def saler_handler(sig, frame):
    if sig == signal.SIGINT:
        os.kill(os.getppid(), SIGUSER1)
    if sig == signal.SIGQUIT:
        os.kill(os.getppid(), SIGUSER2)
    if sig == SIGUSER1:
        print("到站了, 下车.")
        os._exit()
        

def driver():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGQUIT, signal.SIG_IGN)
    signal.signal(SIGUSER1, driver_handle)
    signal.signal(SIGUSER2, driver_handle)
    signal.signal(signal.SIGTSTP, driver_handle)


def driver_handle(sig, frame):
    if sig == SIGUSER1:
        print("老司机开车了.")
    if sig == SIGUSER2:
        print("车速有点快, 请记好安全带.")
    if sig == signal.SIGTSTP:
        os.kill(child.pid, SIGUSER1)


child = mp.Process(target=saler)
child.start()
child.join()

driver()
