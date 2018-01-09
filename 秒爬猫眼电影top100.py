import requests
from requests.exceptions import RequestException
import re,json
from multiprocessing import Pool  #多进程！

def get_one_page(url):#检测网址是响应成功
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(\d+).*?data-src="(.*?)".*?name"><a'
              +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
              +'.*?integer">(.*?)</i>.*?fraction">(.*?).*?</dd>',re.S)#re.S是为了匹配换行符
"""一共7个（），分别对应内容为:排名，图片链接png，电影名称，演员表，上映时间，评分个位数+十分位数--9.6"""

    items=re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'cator':item[3].strip()[3:],#去掉多余空格，切片，去掉开头的几个字如：“主演：”
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }
        
#     print(items)
def write_to_file(content):#写入txt中
    with open('result.txt','a')as f:#encoding='utf-8/gbk'
        f.write(json.dumps(content,ensure_ascii=False)+'\n')#因为content是字典形式，所以转为字符串形式需要导入json.dumps
        f.close()

def main(nums):
    url='http://maoyan.com/board/4?offset='+str(nums)
    
    html=get_one_page(url)
#     parse_one_page(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)
    
if __name__=='__main__':
    pool=Pool()
    pool.map(main,[i*10 for i in range(10)])