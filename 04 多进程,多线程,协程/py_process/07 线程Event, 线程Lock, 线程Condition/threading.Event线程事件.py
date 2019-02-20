import threading, time

s = None

def bar():
    et.set()
    global s
    print("bar: 呼叫foo")
    s = "天王盖地虎"

def foo():
    print("foo: 等待对暗号")
    time.sleep(2)
    if s == "天王盖地虎":
        print("foo: foo收到, 天王盖地虎")
    else:
        print("foo: 不是自己人")

def fun():
    global s
    time.sleep(1)
    print("fun: 呵呵~, 改你暗号")
    s = "小鸡炖蘑菇"
    et.wait()

# 创建事件
et = threading.Event()

th1 = threading.Thread(name="bar", target=bar)
th2 = threading.Thread(name="foo", target=foo)
th3 = threading.Thread(name="fun", target=fun)

th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()
