import re

s = """Hello World\nChina taday News\nBeijing."""
pattern = """(?P=<t1>hello) # t1组
\s+ # 空字符
(world) # 第二组用来匹配world
"""


result1 = re.findall('hello', s)
result2 = re.findall('h\w+', s, re.IGNORECASE)   # 忽略大写
print(result1)
print(result2)

print("---------------------")

result3 = re.findall("[wW]orld$", s, re.MULTILINE)   # 可以匹配每一行的开头结尾位置
print(result3)

print("---------------------")

result4 = re.findall(pattern, s, re.X)
print(result4)
