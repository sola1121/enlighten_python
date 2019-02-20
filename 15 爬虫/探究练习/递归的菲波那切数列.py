import sys

sys.setrecursionlimit(20)

def fib1(num1=1, num2=1):
    result = num1 + num2
    print(result, end=", ")
    fib1(num2, result)

try:
    fib1()
except RecursionError:
    print("\n=====================")


def fab2(n):   # 第n位的斐波那契数
    index, x, y = 0, 1, 1
    while index < n-2:   # 扣除最开始1, 1
        x, y = y, x+y
        index += 1
    return y

print(fab2(20))
for i in range(1, 21):
    print(fab2(i), end=", ")
else:
    print()