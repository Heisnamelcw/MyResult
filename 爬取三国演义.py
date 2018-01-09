import requests
import urllib.request
import chardet
from bs4 import BeautifulSoup
url="http://www.shicimingju.com/book/sanguoyanyi.html" # 要爬取的网络地址
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
#menuCode=urllib.request.urlopen(url).read()  # 将网页源代码赋予menuCode
menuCode=requests.get(url,headers=headers)
menuCode.encoding='utf-8'
soup=BeautifulSoup(menuCode.text,'lxml')

menu=soup.find_all(id='mulu')#mmenu=soup.select('#mulu')
values=','.join(str(x)for x in menu)
soup2=BeautifulSoup(values,'lxml')
soup2=soup2.ul

f=open('我的三国演义.txt','a',encoding='utf-8')

# soup2.contents[1].string  #章节目录
# soup2.contents[1].a['href']#章节对应链接
bookMenu=[]
bookMenuUrl=[]
for i in range(1,len(soup2.contents)-1):
    bookMenu.append(soup2.contents[i].string)
    bookMenuUrl.append(soup2.contents[i].a['href'])    
top="http://www.shicimingju.com"#bookMenu,bookMenuUrl
#到此外层循环结束，即章节循环以及对应的子页网址循环，接着要循环子页网址内的内容
#len(bookMenuUrl)==120

#注意看注意看，这里的第二个for循环并不是子循环，是同时进行的，之前的爬取招聘类网址信息的时候是否可以参考
for i in range(0,len(bookMenuUrl)):         
    href=top+bookMenuUrl[i]
    html=requests.get(href,headers=headers)
    html.encoding='utf-8'
    soup3=BeautifulSoup(html.text,'html.parser')
    soup4=soup3.find_all(id='con2')
    soup4=','.join(str(x)for x in soup4)
    soup5=BeautifulSoup(soup4,'html.parser')
    soup5=soup5.br
    soup5
    #len(soup5)=20+
    f.write(bookMenu[i])
    for j in range(0,len(soup5)):
        ctext=soup5.contents[j].string
        f.write(ctext)
f.close()
