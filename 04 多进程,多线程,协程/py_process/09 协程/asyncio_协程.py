import asyncio


async def work1(x, y):
    print("work1调用, 获得结果:", x*y)
    await asyncio.sleep(1)
    return x*y


async def work2(a, b):
    print("work2调用, 获得结果:", a+b)
    await asyncio.sleep(0.5)
    return a+b


if __name__ == "__main__":
    
    # 获取事件循环
    loop = asyncio.get_event_loop()

    # 执行事件循环, 直到完成
    loop.run_until_complete(work1(3, 4))
    loop.run_until_complete(work2(1, 2))

    # 关闭事件循环
    loop.close()
