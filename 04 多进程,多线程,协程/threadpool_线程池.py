import threadpool, time


def sayhello(words):
    print("hello", words)
    time.sleep(2)

start_time = time.time()

pl = threadpool.ThreadPool(4)
req = threadpool.makeRequests(sayhello, ("siro", "kizuna_ai", "luna"))

[pl.putRequest(r) for r in req]

pl.wait()

print("used time:", time.time() - start_time)
