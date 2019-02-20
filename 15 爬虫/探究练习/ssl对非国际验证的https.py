from urllib import request
import ssl

context = ssl._create_unverified_context()

url = "https://www.12306.cn/mormhweb/"

ua_headers = {"User-Agent": 
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3472.3 Safari/537.36"}

# http request
req = request.Request(url, headers=ua_headers)

# http response
res = request.urlopen(req, context=context)

with open("12306.html", 'wb') as html_file:
    html_file.write(res.read())
