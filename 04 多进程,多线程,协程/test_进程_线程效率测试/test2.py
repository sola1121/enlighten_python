from test import * 
import threading 
import time 

counts = []

t = time.time()
for x in range(10):
    th = threading.Thread\
    (target = count,args = (1,1))
    th.start()
    counts.append(th)
n = 10
while True:
    for i in counts:
        if not i.is_alive():
            n -= 1
    if n <= 0:
        break
print("Thread cpu",time.time() - t)

