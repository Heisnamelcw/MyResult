#-*- coding:utf-8 -*-
import requests, json, re, time
from bs4 import BeautifulSoup
import pandas as pd
from multiprocessing import Pool
from requests.exceptions import RequestException


def one(url):
    ua = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
    proxies = {'https': 'http://195.168.2.33'}
    try:
        req = requests.get(url=url, headers=ua,proxies=proxies,timeout=5)
        req.encoding = 'utf-8'
        htmls = json.loads(req.text, encoding='utf-8')
        html = htmls['message']
        if req.status_code == 200:
            return html
        return None
    except RequestException:
        return None

def two(html):
    pattern = re.compile('<div.*?con_info fll.*?<dl.*?<dt.*?<p>(.*?)</p>.*?label".*?<a.*?>(.*?)</a>', re.S)
    items = re.findall(pattern, html)
    #     print(items)
    for item in items:
        yield {
            '投诉时间': item[0],
            '投诉对象': item[1]
        }
# def two(html):
#     pattern = re.compile('<div.*?con_info fll.*?<dl.*?<dt.*?<p>(.*?)</p>.*?label".*?<a.*?>(.*?)</a>', re.S)
#     items = re.findall(pattern, html)
#     #     print(items)
#     for item in items:
#         yield[item[0],item[1]]
#         # yield{
#         # '时间':item[0],
#         # '对象':item[1]
#         # }

def three(content):
    write_flag = True
    with open('tsts8-15.txt', 'a', encoding='gbk')as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(nums):
    api = 'http://ts.21cn.com/front/api/includePage/indexPcMorePost.do?order=ctime&pageNo={}&pageSize=10'.format(nums)
    html = one(api)
    #     print(html)

    for item in two(html):  # two(html)
        print(item)
        three(item)


if __name__ == '__main__':  # 先来5页的
    # for i in range(1,50):
    #     main(i)
    pool = Pool()
    pool.map(main, [nums for nums in range(800,1500)])
    time.sleep(1)