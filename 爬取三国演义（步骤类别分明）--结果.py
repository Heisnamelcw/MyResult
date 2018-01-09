import sys,re,requests,time
from bs4 import BeautifulSoup
class dodo(object):
    
    def __init__(self):
        self.url='http://www.shicimingju.com/book/sanguoyanyi.html'
        self.top='http://www.shicimingju.com/'
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
        self.names=[]
        self.nums=0
        self.hrefs=[]
    
    def get_url(self):
        req=requests.get(url=self.url,headers=self.headers)
        req.encoding='utf-8'
        html=req.text
        soup0=BeautifulSoup(html,'lxml')
        mulu=soup0.find_all(id='mulu')
        soup1=BeautifulSoup(str(mulu))
        a=soup1.find_all('a')
        self.nums=len(a)
        for each in a:
            self.names.append(each.text)
            self.hrefs.append(self.top+each.get('href'))
    
    def get_content(self,url):
        req=requests.get(url=url)
        req.encoding='utf-8'
        html=req.text
        bf=BeautifulSoup(html,'lxml')
        texts=bf.find_all(id='con2')
        texts=texts[0].text.replace('\xa0'*4,'\n')
        return texts
    
    def www(self,name,path,text):
        write_flag=True
        with open(path,'a',encoding='utf-8')as f:
            f.write(name+'\n')
            f.writelines(text)
            f.write('\n\n')
            
if __name__=='__main__':
    dl=dodo()
    dl.get_url()
    print('start!')
    t1=time.time()
    for i in range(dl.nums):
        dl.www(dl.names[i],'sgyy.txt',dl.get_content(dl.hrefs[i]))
        sys.stdout.write('下载中：%.3f %%' % float((i/dl.nums)*100)+'\r')
        sys.stdout.flush()
    print('End!')
    t2=time.time()
    t3=t2-t1
    print('spend time:%d'%(t3))