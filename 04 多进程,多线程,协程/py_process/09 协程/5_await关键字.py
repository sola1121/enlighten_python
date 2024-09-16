import asyncio


async def work():
    await asyncio.sleep(1)
    return work.__name__


# 调用协程的闭包
async def do_coro():
    ret = await work()   # 等待协程对象, 并获取协程的返回值
    print("获得协程的返回值:", ret)


# 执行协程
asyncio.run(do_coro())

