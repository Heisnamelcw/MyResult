import requests
from requests.exceptions import RequestException
import re,json,csv
from multiprocessing import Pool
from bs4 import BeautifulSoup

def get_one_url(url):#检测网址是否响应成功
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
	try:
		response=requests.get(url=url,headers=headers)
		if response.status_code==200:
			return response.text  #响应成功返回text 结果赋值为html
		return None
	except RequestException:
		return None

def parse_one_page(html):#html其实是一些类字符串，正则匹配
	pattern=re.compile('<div class="info-panel">.*?href="(.*?)".*?region">(.*?)</span.*?span>(.*?)</span.*?meters">(.*?)</span><span>(.*?)</span.*?price.*?num">(.*?)</span>.*?num">(.*?)</span>(.*?)</div.*?col-look">(.*?)</div.*?</div>',re.S)
	items=re.findall(pattern,html)

	for item in items:
		yield {
		'链接':item[0],
		'名称':item[1].replace('&nbsp;',''),#去掉空格字符
		'户型':item[2].replace('&nbsp;',''),
		'大小':item[3].replace('&nbsp;',''),
		'朝向':item[4].replace('&nbsp;',''),
		'月租':item[5],
		'次数':item[6]+item[7]+item[8]
		}

def write_to_file(content):
	with open('链家p.txt','a',encoding='gbk')as f: #保存为txt格式
		f.write(json.dumps(content,ensure_ascii=False)+'\n')
		f.close()
# def write_to_file(content):
	with open('链家p.csv','a',encoding='gbk') as f:#保存为csv格式
		f.write(json.dumps(content, ensure_ascii=False) + '\n')
		f.close()

def main(nums):
	url='https://wh.lianjia.com/zufang/pg{}/'.format(nums)#网址格式
	html=get_one_url(url)   #函数关系
	for item in parse_one_page(html):#函数关系
		print(item) 
		write_to_file(item)#写入的内容在yield中迭代,此3个item可以任意替换
		#即写入的内容是与其相关函数所产生的值，值在yield中迭代以增加效率


if __name__=='__main__':
	pool=Pool()
	pool.map(main,[i for i in range(1,101)])#网页显示一共就100页，但网页提示有近3W条数据