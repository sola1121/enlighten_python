import os, time
from multiprocessing import Pool

def worker(msg, info):
    time.sleep(2)
    print(msg, "进程%s" % info)
    return msg + " over"

if __name__ == "__main__":

    result = list()

    # 创建进程池
    pl = Pool(processes = 4)

    # 放入事件
    for i in range(10):
        msg = "hello %d" % i
        # 加入事件后进程就会立即操作运行
        # apply_async函数返回一个返回对象, 该对象可以获取池中函数的返回值
        res = pl.apply_async(worker, (msg, os.getpid()))   
        result.append(res)

    # 关闭进程池, 不能在加入事件
    pl.close()

    # 阻塞等待回收
    pl.join()

    print("================================")

    # 通过apply_async()返回对象的get方法获取返回值
    for res in result:
        print(res.get())
