import asyncio


# 协程函数
async def work1():
    for _ in range(0, 5):
        print("协程任务{}".format(work1.__name__))
        await asyncio.sleep(1)


async def work2():
    for _ in range(0, 5):
        print("协程任务{}".format(work2.__name__))
        await asyncio.sleep(1)



# 协程函数调用, 将得到一个协程对象
# 将当前协程函数转换为协程对象, 并把多个协程对象添加到一个列表中
tasks = [work1(), work2()]


# 获取一个事件循环对象
loop = asyncio.get_event_loop()


# 使用事件循环调度多个协程任务
loop.run_until_complete(asyncio.wait(tasks))


#--------------------------------------

# 使用Python3.7新增的run函数, 省略了事件循环的获取, 直接可以执行协程对象
asyncio.run(asyncio.wait(tasks))

