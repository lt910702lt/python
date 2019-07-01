'''
爬取网页：
requests：单独安装，好用些
urllib：自带，不用独立安装
'''
import requests
import gevent
import time

# 爬取网页,10个，用协程发起10个网页的爬取任务
url_list = [
    'https://www.baidu.com',
    'http://183.232.34.67:8086/zabbix',
    'http://www.gdyzzd.com:8081/GDYY/',
    'https://www4.bing.com/',
    'https://github.com',
    'https://blog.csdn.net',
    'https://mikanani.me/',
    'http://msdn.itellyou.cn/',
    'https://i.youku.com/',
    'https://www.jd.com'
]


def get_url(url):
    res = requests.get(url)
    print(url, res.status_code, len(res.text))

# 协程的时间
g_lst = []
start = time.time()
for url in url_list:
    g = gevent.spawn(get_url, url)
    g_lst.append(g)
gevent.joinall(g_lst)
print(time.time()-start)    # 7.9282567501068115

# 正常运行的时间
start = time.time()
for url in url_list:
    get_url(url)
print(time.time()-start)    # 12.18007493019104