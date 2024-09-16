import inspect
import asyncio


async def fun_work1(val):
    describe = "协程函数" if inspect.iscoroutinefunction(fun_work1) else "非协程函数"
    print(f"运行{fun_work1.__name__}, 该函数是{describe}, 参数{val}")


async def fun_work2(val):
    describe = "协程函数" if inspect.iscoroutinefunction(fun_work2) else "非协程函数"
    print(f"运行{fun_work2.__name__}, 该函数是{describe}, 参数{val}")



# 方式1
# 使用另一个协程函数将要执行的协程闭包
async def run_coro():
    await fun_work1(1)   # 等待协程对象
    await fun_work2(2)

# 使用事件循环执行协程对象
# 获取事件循环
loop = asyncio.get_event_loop()
# 通过事件循环执行轮询事件, 直到所有的协程对象都完成
loop.run_until_complete(run_coro())   # 运行协程函数将会获得一个协程对象
# 关闭事件循环
loop.close()


# 方式2
# 使用另一个协程函数将要执行的协程闭包
async def do_coro2():
    tasks = [
        asyncio.create_task(fun_work1(11)),   # 将协程对象变成Task对象
        asyncio.create_task(fun_work2(12))
    ]
    await asyncio.wait(tasks)   # 异步等待, 等待所有的任务对象完成

# 使用run函数省略事件循环, 直接执行 协程对象, Task对象 或 Future对象
asyncio.run(do_coro2())


# 方式3
# 将要执行的协程写入一个列表
tasks = [
    fun_work1(101),
    fun_work2(102),
]

# 使用run函数省略事件循环, 直接执行 协程对象, Task对象 或 Future对象
asyncio.run(asyncio.wait(tasks))   # 等待所有协程对象完成

