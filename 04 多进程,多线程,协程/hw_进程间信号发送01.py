import signal, os, time
import threading

SIGUSER1 = 60
SIGUSER2 = 61

def saler():
    while True:
        signal.signal(signal.SIGINT, send_drive)
        signal.signal(signal.SIGQUIT, send_drive)
        signal.signal(SIGUSER1, send_drive)


def send_drive(sig, frame):
    if sig == signal.SIGINT:
        os.kill(os.getppid(), SIGUSER1)
    elif sig == signal.SIGQUIT:
        os.kill(os.getppid(), SIGUSER2)
    elif sig == SIGUSER1:
        print("到站了, 请下车.")
        os._exit(1)


def driver():
    while True:
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        signal.signal(signal.SIGQUIT, signal.SIG_IGN)
        signal.signal(SIGUSER1, handel)
        signal.signal(SIGUSER2, handel)
        signal.signal(signal.SIGTSTP, handel)


def handel(sig, frame):
    if sig == SIGUSER1:
        print("老司机开车了.")
    elif sig == SIGUSER2:
        print("系好安全带, 车速有点快")
    elif sig == signal.SIGTSTP:
        os.kill(pid, SIGUSER1)



print("-------等待信号发生------")

pid = os.fork()

if pid < 0:
    print("Failed to create child process.")
elif pid == 0:
    saler()
else:
    th = threading.Thread(target=os.wait)
    th.start()
    driver()
    th.join()
    
