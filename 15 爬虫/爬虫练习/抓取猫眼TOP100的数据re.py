import re
import time
import json
import random
import functools
from urllib import request
from multiprocessing import Process, Manager, Pool, Lock

user_agent = (
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
)

head = {"user-agent": random.choice(user_agent)}
link = "http://maoyan.com/board/4?offset=%s"
pattern = r'<p class="name"[\s\S]*?title="([\s\S]*?)"[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>'


def get_one_page(link, page):
    res = request.urlopen(request.Request(link % page, headers=head))
    res_text = res.read().decode("utf-8")
    time.sleep(random.randint(1, 3))
    if res:
        return res
    else:
        return None


def analyze_html(res_html, pattern):
    result = pattern.findall(res_html)
    for item in items:
            yield{
                "title":item[0].strip(),
                "actor":item[1].strip(),
                "time":item[2].strip()
            }


def crawl_page(lock, pattern, offset):
# 将下载页面，解析页面及保存信息放入一个函数中
    html = get_one_page(link, offset)    
    for item in analyze_html(html, pattern):
        lock.acquire() #加锁
        write_to_file(item) 
        lock.release() #释放锁
#    #url = "http://maoyan.com/board/4?offset="
#    for i in range(minPage,maxPage,step):
#        # 每次生成一个入口的URL
    time.sleep(1)
    

def write_to_file(info):
    with open("maoyanTop100.txt", 'a', encoding="utf-8") as f:
        f.write(json.dumps(info, ensure_ascii=False) + '\n')


minPage = 0        
maxPage = 100
step =  10

if __name__ == "__main__":
    # 使用进程池来抓取数据
    # 在进程池之间通信或者加锁使用manager.lock
    # manager = Manager()
    lock = Lock()
    # 产生一个新的包装函数
    new_crawl_page = functools.partial(crawl_page, lock, pattern)
    
    pool = Pool()
    pool.map(new_crawl_page, [i*10 for i in range(10)])
    pool.close()
    pool.join()
    






# <div class="board-item-content">
#   <div class="movie-item-info">
#       <p class="name"><a href="/films/4055" title="这个杀手不太冷" data-act="boarditem-click" data-val="{movieId:4055}">这个杀手不太冷</a></p>
#       <p class="star">主演：让·雷诺,加里·奥德曼,娜塔莉·波特曼</p>
#       <p class="releasetime">上映时间：1994-09-14(法国)</p>    
#   </div>
#   <div class="movie-item-number score-num">
#       <p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
#   </div>
# </div>