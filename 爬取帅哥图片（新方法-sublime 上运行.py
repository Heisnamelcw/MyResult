#part1，爬取单页目标连接，仅包括对应图片名字[0]和对应链接[1]
# from bs4 import BeautifulSoup
# import requests
# import time
# time_start=time.time()
# if __name__=='__main__':
# 	url='http://www.shuaia.net/index.html'
# 	headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
# }
# 	html=requests.get(url,headers=headers)
# 	html.encoding='utf-8'
# 	soup=BeautifulSoup(html.text,'lxml')
# 	#print(soup)
# 	tar_url=soup.find_all(class_='item-img')
# 	list_url=[]
# 	for each in tar_url:
# 		list_url.append(each.img.get('alt')+'='+each.get('href'))
	#print(list_url) #到此结束,以下7行纯属恶搞
# 		for each_img in list_url:
# 			img_info=each_img.split('=')
# 			filename=img_info[0]+'.jpg'
# 		print(filename)
# time_end=time.time()
# time_spend=(time_end)-(time_start)
# print(time_spend)

#part2，爬取多页目标，也仅包括图片名字[0]和对应链接[1]
#发现翻页的规律很简单，仅仅是后缀数字不一样

# from bs4 import BeautifulSoup
# import requests
# if __name__=='__main__':
# 	list_url=[]
# 	for num in range(1,11):  #看，第一行特殊，其余翻页仅与数字有关
# 		if num==1:
# 			url='http://www.shuaia.net/index.html'
# 		else:
# 			url='http://www.shuaia.net/index_%d.html' %num
# 		headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
# }
# 		req=requests.get(url,headers=headers)
# 		req.encoding='utf-8'
# 		html=req.text

# 		soup=BeautifulSoup(html,'lxml')
# 		tar_url=soup.find_all(class_='item-img')
# 		for each in tar_url:
# 			list_url.append(each.img.get('alt')+'='+each.get('href'))
	#print(list_url)#到此结束，以下几行为恶搞
			# for each_img in list_url:
			# 				img_info=each_img.split('=')
			# 				filename=img_info[0]+'.jpg'
			# 			print(filename)

#part3，爬取进入图片链接后的高清大图片
# from urllib.request import urlretrieve
# from bs4 import BeautifulSoup
# import requests
# import os,time
# target_url = 'http://www.shuaia.net/mote/2017-09-01/14900.html'
# filename = '张根硕拍摄机车型男写真帅气十足' + '.jpg'
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
#     }
# img_req = requests.get(url = target_url,headers = headers)
# img_req.encoding = 'utf-8'
# img_html = img_req.text
# img_bf_1 = BeautifulSoup(img_html, 'lxml')
# img_url = img_bf_1.find_all('div', class_='wr-single-content-list')
# img_bf_2 = BeautifulSoup(str(img_url), 'lxml')
# top='http://www.shuaia.net'
# img_url2 = top + img_bf_2.div.img.get('src')
# if 'images' not in os.listdir():
#     os.makedirs('images')
# urlretrieve(url = img_url2,filename = 'images/' + filename)
# print('下载完成！')

#part4，完整版代码
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests,os,time

time_start=time.time()#定义开始运行时的时间
if __name__=='__main__':
	
	list_url=[]
	for num in range(1,3):#就翻4页
		if num ==1:
			url='http://www.shuaia.net/index.html'
		else:
			url='http://www.shuaia.net/index_%d.html' %num	
		headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

		#这里的部分格式与我之前的风格略有一丢丢不同，在3,4行处
		req=requests.get(url=url,headers=headers)
		req.encoding='utf-8'
		html=req.text
		soup=BeautifulSoup(html,'lxml')
		targets_url=soup.find_all(class_='item-img')
		#这里是part1的结果，获取了图片[0]名字和对应进入的链接[1]
		for each in targets_url:
			list_url.append(each.img.get('alt')+'='+each.get('href'))

	print('连接采集完成')
	#进入到part2，3，翻页已经实现
	for each_img in list_url:
		img_info=each_img.split('=')
		filename=img_info[0]+'.jpg'
		target_url=img_info[1]
		print('下载：'+filename)
		#进入每一页图片的链接，get 优化等
		headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
		img_req=requests.get(url=target_url,headers=headers)
		img_req.encoding='utf-8'
		html2=img_req.text
		soup2=BeautifulSoup(html2,'lxml')
		#找到对应图片的标签部分，再次优化下，
		img_url=soup2.find_all('div',class_='wr-single-content-list')
		soup3=BeautifulSoup(str(img_url),'lxml')
		#找到要下载的图片发现缺失头部，补充
		top='http://www.shuaia.net'
		img_url2=top+soup3.div.img.get('src')
		#如果在运行的磁盘下不存在这个文件夹，则新建
		if 'pmages' not in os.listdir():
			os.makedirs('pmages')
		#urlretrieve() 方法直接将远程数据下载到本地。
		#url为下载的链接，此出链接为图片，filename指定保存路径
		urlretrieve(url=img_url2,filename='pmages/'+filename)
		time.sleep(1)#设置休眠1s时间，防封
	print('下载完成')
time_end=time.time()
time_spend=(time_end)-(time_start)
print(time_spend)

#128行遇到中文格式时会报错，可用二进制写入图片：
#    with open(filename,'wb')as f:
#        response=requests.get(url=imgurl)
#        for aaa in response.iter_content(1024):
#           if aaa:
#              f.write(aaa)
#			   f.close()     