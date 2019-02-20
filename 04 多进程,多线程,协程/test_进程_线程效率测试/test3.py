from test import * 
import multiprocessing
import time 

counts = []

t = time.time()
for x in range(10):
    p = multiprocessing.Process\
    (target = count,args = (1,1))
    p.start()
    counts.append(p)
n = 10
while True:
    for i in counts:
        if not i.is_alive():
            n -= 1
    if n <= 0:
        break
print("Process cpu",time.time() - t)

