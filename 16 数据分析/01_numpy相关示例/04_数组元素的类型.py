import numpy as np


# 给数组命名
a = np.array([("ABC", [1,2,3])], dtype="U3, 3i4")   # 使用紧凑格式, 3个字符的unicode, 3个数值的int32. 将元组中的类型区分开了, 形成了一个自定义的组合类型
print(a)
print(a[0])
print(a['f0'])
print(a['f0'][0])

b = np.array(
    [("ABC", [1,2,3])], 
    dtype=[("string", np.str, 3), ("number", np.int32, 3)]   # 添加了对列表中元组里的两个不同元素的描述, (名字, 类型, 个数)
    )
print(b[0]["string"])
print(b[0]["number"])

c = np.array(
    [("ABC", [1,2,3])], 
    dtype={"names": ["string", "number"], "formats": ["U3", "3i4"]}   # 功能同b, 结构更紧凑, 更可读
    )
# names, formats, titles, offsets 字典键固定
print(c[0]["string"])
print(c[0]["number"])

d = np.array(
    [("ABC", [1,2,3])], 
    dtype={"string": ("U3", 0), "number": ("3i4", 12)}
    )
print(d[0]["string"])
print(d[0]["number"][2])


print("使用大端字节序, 使用lo, hi 字段名取值")
e = np.array(
    [0x1a34], 
    dtype=(">u2", {"lo": ("u1", 0), "hi": ("u1", 1)})
    )
print("{:x}".format(e[0]))
print("{:x}{}{:x}".format(e["lo"][0], " 我是中间 ",e["hi"][0]))
