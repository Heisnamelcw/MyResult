#小黄人百度图片稍微改进版
import requests,re,os,time
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

if __name__=='__main__':
    j=0
    for i in range(3):
        nums=i*20
        url='http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E5%B0%8F%E9%BB%84%E4%BA%BA&pn={}&gsm=64&ct=&ic=0&lm=-1&width=0&height=0'.format(nums)
        
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
        
        req=requests.get(url=url,headers=headers)
        req.encoding='utf-8'
        html=req.text
        soup=BeautifulSoup(html,'html.parser') #查看源代码源代码而不是审查元素，即可看到相关jpg地址，后用正则表达式即可
        jpg_url=re.findall('"objURL":"(.*?)",',html,re.S)#只能用html，不能用soup代替,得到list许多jpg
        for each in jpg_url:
            print(each)
            try:
                #requests.get(each,timeout=10)
                if 'alex'not in os.listdir():#不存在且创立，不可更改
                    os.makedirs('alex')
                    
                urlretrieve(url=each,filename='alex/'+str(j)+'.jpg')
                j+=1
            except:continue
                
    print('Done!')



    # if 'alex'not in os.listdir():
    #     os.makedirs('alex')      
    # urlretrieve(url=each,filename='D:/Myresult/alex/'+str(j)+'.jpg')#已存在文件夹下

    # j+=1