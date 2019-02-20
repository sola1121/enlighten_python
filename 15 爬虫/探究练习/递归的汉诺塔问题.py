def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)   # 将n-1个圆盘移动到b
        hanoi(1    , a, b, c)   # 将a的最后一个圆盘移动到c
        hanoi(n - 1, b, a, c)   # 将b的n-1个圆盘移动到c
# 调用
hanoi(5, 'A', 'B', 'C')
