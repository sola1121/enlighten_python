import asyncio


# 协程的嵌套就是用一个协程函数包含其他协程函数, 可以理解为一个闭包


async def work():
    print(f"协程{work.__name__}启动...")
    await asyncio.sleep(2)
    print(f"协程{work.__name__}完成...")
    return f"返回值{work.__hash__()}"


async def main(*args):
    for fun in args:
        print("将执行协程函数:", fun.__name__)
        ret = await fun()
        print("当前的返回值为:", ret)


if __name__ == "__main__":
    
    asyncio.run(main((work(), work())))

