#%%
# lambda表达式, 又称匿名函数
# 格式为 lambda 参数列表: 返回值
fun1 = lambda num1, num2: num1+num2

def fun2(num1, num2):
    return num1+num2

print("计算两个数的和:", fun1(3, 4), fun2(3, 4))


# %%
# 直接调用匿名函数, 只能使用一次
print("计算两数和:", (lambda num1, num2: num1+num2)(3, 4))


# %%
# 传入多个参数, 计算累加和
fun3 = lambda *args: sum(args)

print("多个数相加:", fun3(*list(range(1, 11))))


#%%
# 判断两数中较大的值
print("%d与%d中谁更大: %d" % (5, 8, (lambda a, b: a if a>b else b)(5, 8)))   # 这里也可以使用max()函数


# %%
# 应用, 将列表以其元素的第二个值进行排序
lst = [(3, 4), (5, 2), (7, 6), (8, 9)]
print("排序前的列表:", lst)

lst = sorted(lst, key=lambda tp: tp[1])

print("排序后的列表:", lst)
