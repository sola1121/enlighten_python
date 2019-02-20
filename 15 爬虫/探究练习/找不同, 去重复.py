# 找不同
lst1 = [1,2,3,4,5,6,7,8]
lst2 = [1,2,3,4,6,7,8]

# 1 求和相减...(略)

# 2


# 去重复
lst3 = [1,2,2,3,4,5,6,6,7,8,8,8]

# 1
import collections
import copy

ls = copy.deepcopy(lst3)
count = collections.Counter(lst3)

for c in count.keys():
    if count[c] > 1:
        for _ in range(count[c]-1):
            ls.pop(c)

print("使用collections.Counter的去重", ls)

# 2
ls = copy.deepcopy(lst3)
new_set = set(ls)
print("使用set不重复去重", new_set)

# 3
ls = copy.deepcopy(lst3)
dic = dict()
for e in ls:
    dic[e] = None
print("使用dict的键不重复去重", list(dic.keys()))

