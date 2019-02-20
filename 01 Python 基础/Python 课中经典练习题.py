# 判断文字是否ABCCBA形式

in_str = input("输入文字: ")

count = 0
for i in range(len(in_str) // 2):
    x = len(in_str) - i - 1
    if in_str[i] == in_str[x]:
        count += 1

if count == len(in_str) // 2:
    print("所输入的字符是回文")
else:
    print("输入的子符不是回文")


# -------------------------------------
# if判断最大

a = int(input("num1: "))
b = int(input("num2: "))
c = int(input("num3: "))

if  a < b:
    a = b
if a < c:
    a = c
print("The bigest is", a)


# -------------------------------------
# 打印星号组成的箭头

num = int(input("Input a number: "))

for i in range(num * 2 + 1):
    if i % 2 == 0:
        continue
    print(("*"*i).center(num))

while num:
    print("*".center(num))
    num -= 1


# -------------------------------------
# 去掉序列中重复出现的
L1 = [2, 3, 3]
unique = list()
for x in L1:
    if x not in unique:
        unique.append(x)

# 判断出现了2次的元素
lst = [2, 3, 3]
result = set()
for x in lst:
    count = 0
    for y in lst:
        if x == y:
            count += 1
    else:
        if count == 2:
            result.add(x)

# 当然也可以使用functools.Counter
import functools
count_dict = functools.Counter(lst)


# -------------------------------------
# 求最大算法
def own_max(a, *arg):
    if len(arg) == 0:
        m = a[0]
        i = 1
        while i < len(a):
            if a[i] > m:
                m = a[i]
            i += 1
        return m
# 挨个挨个比较大小, 遇到大的就变成他



# -------------------------------------
# 尾递归, 解决递归溢出
def fac(num):
    return fac_iter(1, 1, num)

def fac_iter(res, count, max_value):
    if count > max_value:
        return res
    return fac_iter(res * count, count + 1, max_value)


# -------------------------------------
# 递归, 层层查看列表中每个元素
# L = [2, [3, 4, 5], [3, [4, 5, 6]], 10]
def print_list_re(lst):
    """递归方式, 可以自动判断层数"""
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            print_list_re(lst[i])
        else:
            return lst[i]


# -------------------------------------
# 装饰器, 帮助理解
import time

def run_time(fun):
    strat_time = time.time()
    fun(*arg)
    print(time.time() - strat_time)

@run_time
def theFunction():
    pass

theFunction()


# 装饰器应用, 模拟银行存金额

# 在不改变原函数的情况下添加权限验证机制
def authority_check(fn):
    def fx(name, x):   # 参数要符合被装饰函数的规则
        print("正在权限验证...")
        # if name == '...':...
        fn(name, x)
    return fx

def send_mesg(fn):
    def fy(name, x):   # 参数要符合被装饰函数的规则
        fn(name, x)
        print(name, "发生了", x,"元的操作, 余额: ...")
    return fn

@authority_check
def save_money(name, x):
    print(name, "存钱", x, "元")

@send_mesg
@authority_check
def withdraw(name, x):
    print(name, "正在办理取钱", x, "元的业务")

save_money("小张", 200)
save_money("小昭", 500)

withdraw("小李", 300)


# -------------------------------------
# 模拟复制文件
def copy_file(src, dst):
    try:
        with open(src, 'wb') as f_s, open(dst, 'rb') as f_d:
            while True:
                source = f_s.read(4096)   # 每次读取4096个字节即4GB, 防止文件过大对内存压力过大
                if not source:
                    break
                f_d.write(source)
    except:
        print("文件复制失败")
    else:
        print("文件复制成功")


# -------------------------------------
# 1
a = [100]
def test(x):
    x = x + x
    print(x)
test(a)
print(a)
# 输出
# [100, 100]
# [100]

# 2
a = [100]
def test(x):
    x += x
    print(x)
test(a)
print(a)
# 输出
# [100, 100]
# [100, 100]



# -------------------------------------
# 模拟zip函数
def myzip(iter1, iter2):
    it1 = iter(iter1)
    it2 = iter(iter2)
    try:
        while True:
            a = next(it1)
            b = next(it2)
            yield (a, b)
    except:
        pass


numbers = [10086, 10000, 10010, 95588]
name = ['中国移动', '中国电信', '中国联通']

for t in myzip(numbers, name):
    print(t)