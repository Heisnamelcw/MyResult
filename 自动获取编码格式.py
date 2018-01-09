from urllib import request
import chardet

if __name__=='__main__':
	response=request.urlopen('https://www.zhihu.com/')
	html=response.read()
	charset=chardet.detect(html)
	print(charset)