#%%
# 字符型数据
s = "你好, 世界!"
print("类型:", type(s), s)
# 字节型数据
b = b"abcdefg"
print("类型:", type(b), b)

# 将 字符串数据类型 转换为 字节型数据, 即进行解码
b1 = s.encode("utf-8")
print("转换后类型:", type(b1), b1)

b2 = s.encode("gbk")
print("转换后类型:", type(b2), b2)

print(f"不同字符集编码后, {b1}是否与{b2}相等:", b1==b2)

# 将 字节型数据 转换为 字符串数据类型, 即进行编码
s1 = b.decode("utf-8")
print("转换后类型:", type(s1), s1)

s2 = b.decode("gbk")
print("转换后类型:", type(s2), s2)
# %%
