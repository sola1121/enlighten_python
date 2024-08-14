# %% 
# 装饰器, 使用闭包实现
# 这里的闭包函数outer_func就是装饰器函数
# comment将作为参数传入, 是被装饰的函数, 即将改变其原先的行为

is_loging = True

def comment():
    print("发表评论.")

def outer_func(fun):   # fun为作为参数传入的被装饰函数
    def inner_func():
        global is_loging
        if is_loging:
            fun()
        else:
            print("需要登录.")   # 添加的功能
    return inner_func  # 增加功能后, 闭包返回

decorator = outer_func(comment)
decorator()


# %%
# 装饰器, 使用语法糖@

@ outer_func
def comment2():
    print("发表评论.")

comment2()


# %%
# 装饰器装饰无参无返回值的函数
def prinfo(func):
    def inner_func():
        print("1.在此添加一些功能.")
        func()
    return inner_func

@ prinfo
def info():
    print("info函数调用.")

info()


# 装饰器装饰有参数无返回值的函数
def prinfo2(func):
    def inner_func(value):   # 将被装饰函数的参数作为内部函数的参数
        print("2.在此添加一些功能.")
        func(value)
    return inner_func

@ prinfo2
def info2(val):
    print("info2函数调用. 具有值%d." % (val,))

info2(22)
    

# 装饰器装饰无参数有返回值的函数
def prinfo3(func):
    def inner_func():
        print("3.在此添加一些功能.")
        return func()   # 将被装饰函数的返回值返回出来
    return inner_func

@ prinfo3
def info3():
    return 333

val = info3()
print("info3函数调用后, 返回值{}.".format(val))


# 装饰器装饰有参数有返回值的函数
def prinfo4(func):
    def inner_func(value):   # 将被装饰函数的参数作为内部函数的参数
        print("4.在此添加一些功能.")
        ret = func(value)
        return ret   # 将被装饰函数的返回值返回出来
    return inner_func

@ prinfo4
def info4(val):
    print(f"info4函数调用. 具有值{val}. 返回其二倍值")
    return val*2

val = info4(4444)
print(val)


# %%
# 多个装饰器修饰同一个函数
# 用户发表评论, 首先判断是否已经登录, 再判断是否有权限

account = {"is_loging": False, "is_pk": True}

def is_log(func):
    def inner_func(account):
        if account["is_loging"]:
            return func(account)
        else:
            print("当前用户没有登录.")
            return False
    return inner_func


def is_limit(func):
    def inner_func(account):
        if account["is_pk"]:
            return func(account)
        else:
            print("当前用户没有权限.")
            return False
    return inner_func


@ is_limit
@ is_log
def go_comment(val):
    print("评论成功.")
    return True

ret = go_comment(account)
print(ret)


# %%
# 带有参数的装饰器
# 因为装饰器函数只能给到一个参数, 所以在传递装饰器函数的参数的时候, 需要在外边在包装一层函数, 将参数带入
def caculate(sign):
    def inner_func1(func):
        def inner_func2(a, b):
            ret = 0
            if sign == "+":
                print("进行加法运算.")
                ret = func(a, b)
            elif sign == "-":
                print("进行减法运算.")
                ret = func(a, b)
            else:
                print("未知运算.")
            return ret
        return inner_func2
    return inner_func1
        

@ caculate("+")
def add(a, b):
    return a + b

@ caculate("-")
def sub(a, b):
    return a - b

print("计算%d + %d, 值为 %d." %(3, 4, add(3, 4)))
print("计算%d - %d, 值为 %d." %(8, 2, sub(8, 2)))
# %%

