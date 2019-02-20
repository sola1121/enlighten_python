import asyncio
import functools

@asyncio.coroutine
def fab_coro(n):
    index, x, y = 0, 1, 1
    while index <= n-2:
        x, y = y, x+y
        index += 1
        print(y, end="   ")

loop = asyncio.get_event_loop()
partial_obj = functools.partial(fab_coro, 20)
loop.run_soon()
