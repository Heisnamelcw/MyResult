

import requests
from requests.exceptions import RequestException
import re,json,csv
from multiprocessing import Pool
from bs4 import BeautifulSoup


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
    try:
        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            #             print(response.text)
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile(
        '</tr>.*?<td class="zwmc".*?href="(.*?)".*?<b>(.*?)</b>(.*?)</a>.*?class="zwyx">(.*?)</td>.*?gzdd">(.*?)</td>.*?</tr>',
        re.S)
    pattern22 = re.compile(
        '</tr>.*?<td class="zwmc".*?href="(.*?)".*?blank"><b>(.*?)</b>(.*?)</a>.*?class="zwyx">(.*?)</td>.*?"gzdd">(.*?)</td>.*?</tr>',
        re.S)

    items = re.findall(pattern22, html)
    for item in items:
        yield {
            '链接': item[0],
            '岗位': item[1] + item[2],
            '月薪': item[3],
            '地点': item[4]
        }


def write_to_file(content):
    with open('resresult.txt', 'a', encoding='utf-8')as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(nums):
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&p={}&isadv=0'.format(nums)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


# print(html)

if __name__=='__main__':
	pool=Pool()
	pool.map(main,[i for i in range(1,4)])
# if __name__ == '__main__':
#     for i in range(1,4):
#         main(i)
