# -*- coding: utf-8 -*-

# 题0 谜题
s = (1, 2, [9, 6])
s[2] += [3, 3]

# 会发生什么?
# 因为s是tuple, 其不可改变, 使用自增会试图改变元组的绑定关系, 会报错
# 但是查看s的值时, s变为了 (1, 2, [9, 6, 3, 3])
# 这是因为s[2]是列表, 其可以使用自增减
# 避免这样的错误可以 s[2].extend([3, 3]), 单独改变列表是允许的, 他没有影响到元组


#--------------------------------------


# 题1:
lst = [1, 2, 3]
def f1(x):
    x = [4 ,5 ,6]
print(lst)   # [1, 2, 3]
f1(lst)
print(lst)   # [1, 2, 3]
def f2(x):
    x.append(x)
f2(lst)
print(lst)   # [1, 2, 3, 4, 5 , 6] 改变了列表的值,而不是变量

# 说明: 赋值语句会创建变量或改变变量的绑定关系



# -------------------------------------
# 题2:
lst = [1, 2, 3]
def f(n=0, lst=[]):
    lst.append(n)
    print(lst)
fn(4, L)   # [1, 2, 3, 4]
fn(5, L)   # [1, 2, 3, 4, 5]
fn(200)   # [200]
fn(300)   # [200, 300]

# 说明: 函数的默认参数属于函数, 他不会因函数的调用结束而销毁
# 以上函数可以写成, 避免形参参数留存
def f(n=0, lst=None):
    if lst is not None:
        lst = []
    lst.append(n)
    print(lst)



#--------------------------------------
# 题3, 函数递归训练
# 1! + 2! + 3! + ... + n!
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

n = int(input())

sum(map(factorial, range(1, n)))



#--------------------------------------
#题4, 函数递归训练
# 模拟学生管理, 输入输出实现
stu_lst = list()
fmt = "|%13s|%6s|%8s|"

def input_student():
    """录入学生信息"""
    name = input("Student name: ")
    if not name:
        return stu_lst
    age = input("Student age: ")
    score = input("Student score: ")
    info_dic = {"name": name, "age": int(age), "score": int(score)}
    stu_lst.append(info_dic)
    input_student()

def table_title():
    """打印表头"""
    print("+-------------+------+--------+")
    print(fmt %("Name", "Age", "Score"))
    print("+-------------+------+--------+")

def output_student(lst):
    """输出学生信息"""
    if not lst:
        return 1
    lst = lst
    last = lst.pop()
    print(fmt %(last["name"], last["age"], last["score"]))
    output_student(lst)

input_student()
print("info list:\n", stu_lst)
table_title()
output_student(stu_lst)



# -------------------------------------
# 题5,迭代器,生成器,yield 语句
# 1.生成素数
def isprime(x):
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
            continue
    else:
        return True

def primes1(begin, stop):
    if begin <= 0 or begin >= stop:
        raise ValueError("the number is not right.")
    print("Primes2 between %d-%d: "%(begin, stop),end="")
    for i in (x for x in range(begin, stop+1, 1) if isprime(x)):   # 生成器表达式
        print(i, end="  ")
    print("\n")

primes2(10, 20)

# 2.生成素数
def primes2(begin, stop):
    if begin <= 0 or begin >= stop:
        raise ValueError("the number is not right.")
    limit = begin // 2 + 1
    while begin <= stop:
        for i in range(2, limit):
            if begin % i==0:
                break
        else:
            yield begin   # 有yield 事生成器函数,可以通过迭代直接使用
        begin += 1


# 斐波那契数列
def fibonacci(n):
    if n < 1:
        raise ValueError("should be a integer larger than 0")
    yield 1
    x = 0; y = 1
    for _ in range(0, n, 1):
        res = x + y
        x , y = y, res
        yield res

print("fibonacci: ", end="")
for i in fibonacci(20):
    print(i, end="  ")
print()


# 经典的python风格的斐波那契数列
x, y = 0, 1
for _ in range(20):
    x, y = y, x+y
    print(y, end=" ")
else:
    print()


#--------------------------------------
#题6, with open
# 实现文件的复制
def copy_file(src_file, dist_file):
    with open(src_file, 'rb') as fr:
        with open(dist_file, 'wb') as fw:   # with open(src_file, 'rb') as fr, open(dist_file, 'wb') as fw: 
            b2 = fr.read()   # 这样不好,遇到大文件会耗内存
            fw.write(b2)
            # while True:
            #     b2 = fr.read(4096)   # 每次读取一个块内的字节, 避免内存占用
            #     if not b2:
            #         break
            #     fw.write(b2)
    return True

def main():
    src = input("source file directory: ")
    dist = input("target file directory: ")
    if copy_file(src, dist):
        print("sucess.")
    else:
        print("fail")
    

#--------------------------------------
#题7, __iter__, __next__
# 迭代器方法返回素数
def isprime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True
    
class Prime:
    def __init__(self, be, en):
        self.beg = be
        self.end = en

    def __iter__(self, beg, end):
        return PrimeIterator(self.beg, self.end)   # return 迭代器对象    

class PrimeIterator:
    """此类为实现迭代器协议"""
    def __init__(self, be, en):
        self.beg = be; self.end = en
        self.cur = be   # 设定迭代器的当前位置

    def __next__(self):
        while self.cur < self.end:   # 判断当前走过的值是否直达终点, 若果没有到达终点,则继续
            res = self.cur   # 先保存当前值到
            self.cur += 1   # 让迭代位置向后走一步
            if isprime(res):   # 判断素数
                return res
        raise StopIteration   # self.cur < self.end 不成立时,返回异常

# -----------------
# 写成一个类

class PrimeIterator2:
    """此类为实现迭代器协议"""
    def __init__(self, be, en):
        self.beg = be; self.end = en
        self.cur = be   # 设定迭代器的当前位置

    @staticmethod
    def isprime(x):
        for i in range(2, x):
            if x % i == 0:
                return False
        else:
            return True

    def __iter__(self):
        return self   # return 迭代器对象    

    def __next__(self):
        while self.cur < self.end:   # 判断当前走过的值是否直达终点, 若果没有到达终点,则继续
            res = self.cur   # 先保存当前值到
            self.cur += 1   # 让迭代位置向后走一步
            if isprime(res):   # 判断素数
                return res
        raise StopIteration   # self.cur < self.end 不成立时,返回异常

for x in prime(1, 100):
    print(x, end="  ")


