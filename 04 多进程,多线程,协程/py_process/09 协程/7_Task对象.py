import asyncio


# 来自于文件 6_协程的嵌套.py 中的代码
# 其中因为执行await便将协程对象提交给事件循环, 并一直等待其返回值, 所以, 原代码是顺序执行的
# 现在使用Task对象, 将任务变为异步执行

WORKTIME = 4


async def work(id):
    print(f"协程{work.__name__}{id}启动...")
    await asyncio.sleep(WORKTIME)
    print(f"协程{work.__name__}{id}完成...")
    return f"返回值哈希值{work.__hash__()}"


async def main(*args):
    task1 = asyncio.create_task(args[0](1))
    task2 = asyncio.create_task(args[1](2))

    ret1 = await task1   # task不是耗时任务, 将不会阻塞等待返回值
    ret2 = await task2

    print(ret1)
    print(ret2)


if __name__ == "__main__":
    
    asyncio.run(main(work, work))