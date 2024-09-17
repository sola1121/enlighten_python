import asyncio


# 协程的嵌套就是用一个协程函数包含其他协程函数, 可以理解为一个闭包


WORKTIME = 4


async def work(id):
    print(f"协程{work.__name__}{id}启动...")
    await asyncio.sleep(WORKTIME)
    print(f"协程{work.__name__}{id}完成...")
    return f"返回值哈希值{work.__hash__()}"


async def main(*args):
    count = 1
    for fun in args:
        print(f"将执行协程函数{count}:", fun.__name__)
        ret = await fun(count)   # 等待协程对象
        print("当前的返回值为:", ret)
        count += 1


if __name__ == "__main__":
    
    asyncio.run(main(work, work))



# 以上程序忽略了await在处理有返回值函数的时候, 会一直阻塞直到拿到函数的返回值
# 所以以上程序实际上是一个同步任务, 而不是异步的