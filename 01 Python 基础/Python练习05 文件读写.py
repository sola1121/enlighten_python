# %%
# 写文件
fp = open("Python练习.txt", "wt", encoding="utf-8")
print("文件", fp.name)

# 写入内容, 使用write写入文本内容
fp.write("hello, world.\n")

# 写入内容, 使用writelines写入多行文本内容
fp.writelines(["C\n", "Golang\n", "Python\n", "JavaScript\n"])

# 关闭文件流
fp.close()

# 读文件
fp = open("Python练习.txt", "rt", encoding="utf-8")

# 读取内容, 使用readlines读取多行
for line in fp.readlines():
    print(line, end='')

# 使文件指针重新到文件开头
fp.seek(0)

# 读取内容, 使用readline读取一行
cot = fp.readline()
while cot:
    print(cot, end='')
    cot = fp.readline()

# 使文件指针重新到文件开头
fp.seek(0)

# 读取内容, 使用read指定读取长度
cot = fp.read(20)
print(cot)

# 关闭文件流
fp.close()


# %%
# 使用with关键字与open()函数配合使用
with open("Python练习.txt", "rt", encoding="utf-8") as fp:
    for line in fp.readlines():
        print(line.strip())


# %%
# 二进制模式读取文件, 以字节形式获取数据, 可以用来读取所有格式的文件
b_fp = open("Python练习.txt", "rb")
content = b_fp.read()
print("内容类型:", type(content))
print("获得的内容:", content)


# %%
