# %%
# 判断输入的字符串后缀是否为python源码文件
filename = input("请输入文件名: ")

# 1. 使用字符串的split方法, 分割后判断列表最后的元素是否为py
lst = filename.split('.')
if lst[-1] == "py":
    print("为Python源码文件")
else:
    print("不是Python源码文件")

# 2. 使用索引切片, 判断所得是否为py
suffix = filename[-3:]
if suffix == ".py":
    print("为Python源码文件")
else:
    print("不是Python源码文件")

# 3. 使用endwith方法, 获取后缀, 判断所获得是否为py
if filename.endswith(".py"):
    print("为Python源码文件")
else:
    print("不是Python源码文件")


# %%
# 替换字符串中指定子串
# 需要注意的是, 字符串是不可更改的序列, 使用替换方法会生成新的字符串, 需要用变量重新获取
s = "aabbccddeeff"
if s.find('c') > 1:
    new_s = s.replace('c', 'CC')
    print(new_s)
else:
    print(s)


# %%
# 列表中的去重
lst = [1, 2, 3, 3, 3, 4, 4, 5, 6]
print("原始列表:", lst)

# 1. 使用count()计数, 然后使用remove()多次删除重复值
for num in lst:
    while lst.count(num) > 1:
        lst.remove(num)

print(lst)

lst = [1, 2, 3, 3, 3, 4, 4, 5, 6]
print("原始列表:", lst)

# 2. 使用copy()或者切片复制一个辅助列表, 使用clear()清空原列表, 将辅助列表中的元素依次加入原列表
sup_lst = lst[:]   # sup_lst = lst.copy()
lst.clear()
for num in sup_lst:
    if num not in lst:
        lst.append(num)

print(lst)


# %%
# 列表推导式的应用
# 变量1 = [要插入列表中的数据 for 临时变量 in 容器]  将迭代值插入列表
# 变量2 = [要插入列表中的数据 for 临时变量 in 容器 if 条件]  满足条件才插入列表

# 10以内的奇数
lst1 = ["奇数:" + str(num) for num in range(1, 10, 2)]
print(lst1)
# 10以内的偶数
lst2 = [f"偶数:{num}" for num in range(2, 10) if num%2==0]
print(lst2)
# 20以内非7的倍数且各个数位不含7的数
lst3 = [num for num in range(1, 21) if num%7!=0 and str(num).count('7')==0]  # [num for num in range(1, 51) if num%7!=0 if str(num).cont('7')==0]
print(lst3)


# %%
# 字典的推导式的应用
dit1 = {k: k**2 for k in range(1, 10)}
for k in dit1:
    print(k, ":", dit1[k])

dit2 = {k: k**2 for k in range(10, 20) if k%2==0}
for k, v in dit2.items():
    print(k, ":", v)

# 字典的操作
dit3 = dict()
dit3.update({1: "111"}, {2: "222"})
dit3.update(three="333", four="444")
for k in dit3.keys():
    print(k, ":", dit3[k])
# %%
