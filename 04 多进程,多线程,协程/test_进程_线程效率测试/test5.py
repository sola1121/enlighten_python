from test import * 
import multiprocessing 
import time 

def io():
    write()
    read()

counts = []

t = time.time()
for x in range(10):
    p = multiprocessing.Process(target = io)
    p.start()
    counts.append(p)
n = 10
while True:
    for i in counts:
        if not i.is_alive():
            n -= 1
    if n <= 0:
        break
print("Process IO",time.time() - t)

