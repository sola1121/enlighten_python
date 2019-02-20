import re  

pattern = r'\s+'

#获取正则表达式对象
obj = re.compile(pattern,flags = 0)
# l = obj.findall("abcdabcabab",6,9)

# l = re.findall(pattern,'abcdabcabab',flags = 0)

# print(l)

#匹配目标字符串进行切割
# l = obj.split('hello world  hello kitty  nihao china')
# print(l)

#替换目标字符串中匹配到的内容
# s = obj.sub('##','hello world nihao China',2)
# print(s)

s = obj.subn('##','hello world nihao China')
print(s)