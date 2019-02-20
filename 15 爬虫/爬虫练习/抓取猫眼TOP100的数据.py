import re
import time
import random
import requests
from bs4 import BeautifulSoup

user_agent = (
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
)
head = {"user-agent": random.choice(user_agent)}
link = "http://maoyan.com/board/4?offset=%d"

page_lst = list()

for page in range(0, 11, 10):
    res = requests.get(link%page, headers=head, timeout=10)
    if res.status_code != 200:
        print("网页", page, "时出错.")
        break
    soup = BeautifulSoup(res.text, 'lxml')
    root_divs = soup.find_all("div", class_="board-item-content")
    page_lst.append(root_divs)
    time.sleep(random.randint(2, 4))
    print(root_divs)


for root_div in page_lst:
    title = BeautifulSoup(str(root_div), "lxml").find("p", class_="name").text.strip()
    star = BeautifulSoup(str(root_div), "lxml").find("p", class_="star").text.strip()
    release_time = BeautifulSoup(str(root_div), "lxml").find("p", class_="releasetime").text.strip()
    point_integer = BeautifulSoup(str(root_div), "lxml").find("i", class_="integer").text.strip()
    point_fraction = BeautifulSoup(str(root_div), "lxml").find("i", class_="fraction").text.strip()
    point = str(point_integer) + str(point_fraction)
    print(title, star, release_time, point)



# <div class="board-item-content">
#     <div class="movie-item-info">
#         <p class="name"><a href="/films/4055" title="这个杀手不太冷" data-act="boarditem-click" data-val="{movieId:4055}">这个杀手不太冷</a></p>
#         <p class="star">主演：让·雷诺,加里·奥德曼,娜塔莉·波特曼</p>
#         <p class="releasetime">上映时间：1994-09-14(法国)</p>    
#     </div>
#     <div class="movie-item-number score-num">
#         <p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
#     </div>
# </div>
