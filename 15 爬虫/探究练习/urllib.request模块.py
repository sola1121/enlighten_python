from urllib import request
import random

print(request.urlopen("https://www.bilibili.com").read().decode("utf-8"))

user_agent_pool = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
                   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
                   "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
                   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
                   "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
)
head = {"User-Agent": random.choice(user_agent_pool)}

html_obj = request.urlopen(request.Request("http://www.acfun.cn", headers=head))
print(html_obj.read().decode("utf-8"))
