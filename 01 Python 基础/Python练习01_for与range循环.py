#%%
# 打印7行棱形, 注意, 行数必须是奇数
print("打印棱形")
row = 7
# 打印棱形的上半部分
for rw in range(1, row//2+2):
    # 打印空格部分
    for _ in range(row//2-rw+1):
        print(' ', end='')
    # 打印星部分
    for _ in range(2*rw-1):
        print('*', end='')
    print()
# 打印棱形的下半部分
for rw in range(row//2, 0, -1):
    # 打印空格部分
    for _ in range(row//2-rw+1):
        print(' ', end='')
    # 打印星部分
    for _ in range(2*rw-1):
        print('*', end='')
    print()


#%%
# 打印上三角
print("\n打印上三角")
row = 6
for rw in range(0, row):
    # 打印空格
    for _ in range(rw):
        print(' ', end='')
    # 打印星
    for _ in range(0, row-rw):
        print('*', end='')
    print()

# 打印下三角
print("\n打印下三角")
row = 4
for rw in range(0, row):
    # 打印星
    for _ in range(rw+1):
        print('*', end='')
    # 打印空格
    for _ in range(0, row-rw):
        print(' ', end='')
    print()


#%%
# 九九乘法
print("\n九九乘法表")
# 下三角形状的乘法表, 从1开始
for num1 in range(1, 10):
    for num2 in range(1, 10):
        # 保证下三角区域
        if num1>=num2:
            print(f"{num1}*{num2}={num1*num2}", end=' ')
    print()
