from bs4 import BeautifulSoup
import requests,sys

class  doloader(object): #创建类对象，大工程 最后dl=doloader()
	def __init__(self):  #一些准备工作，代理啊，主页链接啊，存放的列表啊
	    self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
	    self.top='http://www.biqukan.com/'
	    self.url='http://www.biqukan.com/2_2714/'
	    self.names=[]
	    self.hrefs=[]
	    self.nums=0
	    
	    #目标：获取章节名，章节链接，需要的章节数目
	def get_download_url(self):#参数需要第一个里面的，故，参数一致
	 	req=requests.get(url=self.url,headers=self.headers)
	 	html=req.text
	 	soup0=BeautifulSoup(html,'lxml')
	 	soup1=soup0.find_all('div',class_='listmain')#第一次find
	 	soup2=BeautifulSoup(str(soup1))
	 	soup_a=soup2.find_all('a')[12:]#第二次find 获得：章节名称和章节链接
	 	self.nums=len(soup_a)#获得章节数目
	 	for each in soup_a:
	 		self.names.append(each.text)
	 		self.hrefs.append(self.top+each.get('href'))

	def get_contents(self,url):#获取每个章节内容，url为第一个的url，不是href
		req=requests.get(url=url)
		html=req.text
		bf=BeautifulSoup(html,'lxml')
		texts=bf.find_all('div',class_='showtxt')#第三次find
		texts=texts[0].text.replace('\xa0'*8,'\n\n')
		return texts

		#开始写入内容
	def www(self,name,path,text):#对应self.names[i],txt名称,path是当前目录略，在get——contents（href【i])
		write_flag=True
		with open(path,'a',encoding='utf-8')as f:
			f.write(name+'\n')
			f.writelines(text)
			f.write('\n\n')


if __name__=='__main__':
	dl=doloader() #综合命令
	dl.get_download_url()#开始/启动运行命令
	print('开始下载')
	for i in range(dl.nums):#开始写入，一一对应
		dl.www(dl.names[i],'爬取武炼巅峰--结果.txt',dl.get_contents(dl.hrefs[i]))#对应上面的4个
		sys.stdout.write('已下载：%.3f %%' % float((i/dl.nums)*100)+'\r')#两行装逼用
		sys.stdout.flush()
	print('《武炼巅峰》下载完成！')

#49 sys.stdout.write('已下载:{:.3f}%'。forma((i/dl.nums)*100)+'\r')