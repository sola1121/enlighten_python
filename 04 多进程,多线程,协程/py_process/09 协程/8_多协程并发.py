import asyncio


async def coro_work(val):
    if not isinstance(val, int):
        raise ValueError("所给参数不为整数.")
    print(f"{coro_work.__name__}{val}将执行: {val}s.")
    await asyncio.sleep(val)
    return "已经执行{}s".format(val) 


# 方式1
# 多协程并发, 使用await asyncio.wait(协程对象列表)的方式
async def main1():
    # 创建10个任务并将10个任务提交到事件循环
    tasks = [asyncio.create_task(coro_work(i)) for i in range(1, 11)]

    # asyncio.wait返回两个值, 第一个为Task对象的返回, 第二个为Task对象的执行的状态
    # asyncio.wait返回的任务返回值是没有顺序的
    # 使用await asyncio.wait将不会触发await等待返回值而阻塞程序
    done, pending = await asyncio.wait(tasks)

    # print("任务执行的状态:\n", pending)
    # print("任务执行完毕后:\n", done)

    # 获取任务执行的返回结果
    print("获得执行的结果.")
    for ret in done:
        print(ret.result())


# 方式2
# 多协程并发, 使用await asyncio.gather(协程对象1, 协程对象2, ...)的方式
async def main2():
    # 创建10个任务并将10个任务提交到事件循环
    tasks = [asyncio.create_task(coro_work(i)) for i in range(1, 11)]

    # asyncio.gather用来收集所有已完成的任务的返回值, 并且获取到的任务的返回值是有顺序的
    # asyncio.gather返回所有协程对象返回结果的一个列表
    rets = await asyncio.gather(*tasks)

    # print("任务执行完毕后:\n", ret)

    # 获取任务执行的返回结果
    print("获得执行的结果.")
    for ret in rets:
        print(ret)


asyncio.run(main2())