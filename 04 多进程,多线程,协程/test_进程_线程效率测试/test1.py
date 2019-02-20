from test import *
import time 

# t = time.time() 
# for i in range(10):
#     count(1,1)
# print("Line cpu:",time.time() - t)

t = time.time()
for i in range(10):
    write()
    read()
print("Line IO:",time.time() - t)