import os, time

def func1():
    time.sleep(6)
    print("The First Thing Done.")

def func2():
    time.sleep(4)
    print("The Second Thing Done.")


if __name__ == "__main__":
    pid = os.fork()
if pid < 0:
    print("Fail to create new process.")
elif pid == 0:
    print("创建的新进程.", pid)
    func1()
else:
    print("原来的进程.", pid)
    func2()

print("End")
