import requests
from requests.exceptions import RequestException
import time
from multiprocessing import Pool
from bs4 import BeautifulSoup


def get_one_url(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
	try:
		response=requests.get(url=url,headers=headers)
		response.encoding='gbk'
		html=response.text
		soup=BeautifulSoup(html,'lxml')
		soup1=soup.find_all('table',class_='tbspan')
		if response.status_code==200:
			return soup1
		return None
	except RequestException:
		return None

def parse_one_page(soup1):
	l1=[]
	l2=[]
	for i in soup1:
		name=i.select('a.ulink')[0].text
		href='http://www.dy2018.com'+i.select_one('a.ulink')['href']
		pat=i.select('a.ulink')[0].text+'\t'+('http://www.dy2018.com'+i.select_one('a.ulink')['href'])
		l1.append(pat)
		l2.append([name,href])
        # print(pat)
	for item in l2:
		yield {
		'a':item[0],
		'b':item[1]
		}

def write_to_file(content):
	# with open('dytt3.csv','w') as f:
	# 	writer=csv.writer(f)
	# 	for row in item:
	# 		writer.writerow(row)
	with open('dytt.csv', 'a', encoding='gbk')as f:
		f.write(json.dumps(content,ensure_ascii=False)+'\n')
		f.close()

def main(nums):
	url='http://www.dy2018.com/html/gndy/dyzz/index_{}.html'.format(nums)
	soup1=get_one_url(url)
	for item in parse_one_page(soup1):
		print(item)
		# print(l1)
		write_to_file(item)



if __name__=='__main__':
	pool=Pool()
	pool.map(main,[i for i in range(2,297)])
	time.sleep(0.5)