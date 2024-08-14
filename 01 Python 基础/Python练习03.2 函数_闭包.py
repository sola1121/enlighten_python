# %%
# 标准的闭包
# 实现指数函数y = a**x, a>0且a!=1
def outer_func(a:float):  # 规定指数函数中底数a的大小
    if a < 0 or a == 1: 
        raise ValueError(f"底数a={a}, 不满足指数函数定义.")
    def inner_func(x:int) -> float:  # 规定指数函数中指数x的大小
        if isinstance(x, int):
            y = a ** x
            return y
        else:
            raise ValueError(f"指数x={x}, 不是整数.")
    return inner_func   # 返回闭包


ex_fun = outer_func(4)   # 底数设置为4, 相当于缓存了4
print(f"当前绑定的底数为{ex_fun.__closure__}")
# y = 4**3
print(ex_fun(3))
# y = 4**6
print(ex_fun(6))


# %%
# 修改外部函数中的缓存值, 使用nolocal关键字
# 使用闭包完成递加
def start_outer(num1: int):
    def inner_func(num2: int):
        nonlocal num1   # 使用外部函数的参数
        num1 = num1 + num2
        print("num1 =", num1)
    return inner_func


so_fun = start_outer(1)   # 将从1开始
so_fun(1)   # 增1, 打印2
so_fun(3)   # 增3, 打印5
# %%
