#计算密集

def count(x,y):
    c = 0 
    while c < 5000000:
        c += 1
        x += 1
        y += 1

#IO 密集
def write():
    f = open("test.txt",'w')
    for x in range(1000000):
        f.write("hello world\n")
    f.close()

def read():
    f = open("test.txt")
    lines = f.readlines()
    f.close()