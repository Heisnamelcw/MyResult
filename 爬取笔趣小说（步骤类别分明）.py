from bs4 import BeautifulSoup
import requests,sys

# """类说明，下载小说一念永恒"""
#二话不先创建一个硕大的工程，工程名自定义
class downloader(object):
    #开始自定义各种方法，每个方法都有不同目的
    
    #这个目的：可理解为全局变量所需要：链接缺失的头部，主页链接，存放章节名列表，存放链接列表，章节数量
    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
        self.top='http://www.biqukan.com/'
        self.url='http://www.biqukan.com/1_1094/'
        self.names=[]
        self.hrefs=[]
        self.nums=0
    
    #目标：获取章节名；章节链接；统计章节数
    
    def get_download_url(self):   #参数为什么是self呢，因为self内带有需要的全局变量
        req=requests.get(url=self.url,headers=self.headers) #没有代理？？
        html=req.text
        div_bf=BeautifulSoup(html)
        div=div_bf.find_all('div', class_ = 'listmain')
        a_bf=BeautifulSoup(str(div[0]))
        a=a_bf.find_all('a')  #有章节名和链接
        self.nums=len(a[15:])
        for each in a[15:]:             #剔除前15章重复的
            self.names.append(each.text)
            self.hrefs.append(self.top+each.get('href'))
       
    #目标：由上面的章节名对应的链接，获取章节内容
    def get_contents(self,url):   #需要的函数有：self，url
        req=requests.get(url=url)
        html=req.text
        bf=BeautifulSoup(html)
        texts=bf.find_all('div',class_='showtxt')
        texts=texts[0].text.replace('\xa0'*4,'\n')
        return texts
    
    #开始将需要的内容写入
    def writer(self,name,path,text):  #self，name类自带，path:默认当前目录下，text？？
        write_flag=True
        #path='D:/JAVA/'
        with open(path,'a',encoding='utf-8')as f:
            f.write(name+'\n')
            f.writelines(text)
            f.write('\n\n')

#固定结构来了,末尾显示下载的百分比进度，
if __name__=='__main__':
    dl=downloader()
    dl.get_download_url()
    print('《一念永恒》开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i],'一念永111.txt',dl.get_contents(dl.hrefs[i]))
        sys.stdout.write('已下载：%.3f %%' % float((i/dl.nums)*100)+'\r')
        sys.stdout.flush()
    print('《一年永恒》下载完成！')