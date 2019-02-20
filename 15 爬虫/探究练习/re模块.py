import re

url_pattern = re.compile(r"https{0,1}://[a-zA-Z0-9\.\?=&]*")
email_pattern = re.compile(r"[a-zA-Z0-9_-]+@([\w\d_-]+)[\.\w]+")   # 加了分组, 只返回邮箱服务商的域名了
IDcard_pattern = re.compile(r"\d{17}[0-9Xx]")

urls = ("https://www.baidu.com", "https://hao.360.cn", "http://pypy.org/")
emails = ("12345678901@qq.com", " meiyuan@0757info.com", "tony@erene.com.com", "meiya@cn-meiya.com", "kevintian126@126.com")
idcards = ("23230219820414500X", "640203197901146885", "410204199002016174")

for url in urls:
    result = url_pattern.findall(url)
    print(result)

for email in emails:
    result = email_pattern.findall(email)
    print(result)

for idcard in idcards:
    result = IDcard_pattern.findall(idcard)
    print(result)


