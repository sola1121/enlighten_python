# 在进行get网页时, 其url地址是浏览器能识别的格式
# 爬虫在使用get时, 也需要urlencode操作
# 使用urllib.parse.urlencode()

import re
import os
import random

from urllib import request
from urllib.parse import urlencode

user_agent = (
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
)
head = {"User-Agent": random.choice(user_agent)}
link = "https://www.baidu.com/s?"

keyword = input("输入要查询的信息: ").strip()

wd = {"wd": keyword}
wd = urlencode(wd)
full_url = link + wd
print(full_url)

req = request.Request(full_url, headers=head)
res = request.urlopen(req)
res_content = res.read()

with open(os.path.join(os.path.expanduser("~"), 'Desktop') + "/newHtml.html", 'wb') as html_file:
    html_file.write(res_content)

# 网页推荐内容推荐匹配
pattern = re.compile(r"""<div><a target="_blank" href='([\s\S]*)'>([\s\S]*)</a></div>""")

with open(os.path.join(os.path.expanduser("~"), 'Desktop') + "/newHtml.html", 'rb') as html_file:
    html_content = html_file.read()
    html_text = html_content.decode("utf-8", errors="ignore")
    items = pattern.findall(html_text)

for item in items:
    print(item)

