import time

def fun_a():
    while True:
        print(f"{fun_a.__name__}调用")
        yield
        time.sleep(1)

def fun_b(gen):
    while True:
        print(f"{fun_b.__name__}调用")
        gen.__next__()   # next(gen)

# a 为fun_a函数的生成器, 将其给fun_b函数
# fun_b函数将先执行, 打印fun_b调用, 然后获取生成器中的一个对象, 该对象调用, 将打印fun_a调用
# 以上, 将会不断的交替执行, 这就是任务的切换
a = fun_a()
fun_b(a)
