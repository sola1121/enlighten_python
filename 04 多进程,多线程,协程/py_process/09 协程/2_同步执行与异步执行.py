import time

now = lambda: time.time()

# 同步程序, 程序将会按照顺序执行
start = now()

def fun_1s(i):
    time.sleep(1)
    print(i, end=" ")

# 执行
for i in range(0, 5):
    fun_1s(i)

print("同步程序花费的时间:", now()-start)



# 异步程序, 当遇到阻塞, 将会执行下一个任务
import asyncio

start = now()

async def fun2_1s(i):
    asyncio.sleep(1)
    print(i, end=" ")

# 执行
for i in range(0, 5):
    asyncio.run(fun2_1s(i))

print("异步程序花费时间:", now()-start)

