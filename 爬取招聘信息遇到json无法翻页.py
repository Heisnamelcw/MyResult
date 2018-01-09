import requests
from bs4 import BeautifulSoup
import re
import urllib
import csv

def get_wmhs():
    url="http://zhaopin.baidu.com/quanzhi?tid=4139&ie=utf8&oe=utf8&query=%E8%B4%A2%E5%8A%A1&city_sug=%E6%B7%B1%E5%9C%B3"
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

    html=requests.get(url,headers=headers)
    soup=BeautifulSoup(html.text,"lxml")
    a1=[]


    tp="http://zhaopin.baidu.com"
    for i in soup(name="a",class_="clearfix item line-bottom"): 
        s1=i.get_text(strip=True)
        s1=re.sub(r'\s+',' ',s1)
        print(s1)
        s2=tp+i.get("href")

        print("详情进入：",s2)          #主信息+对应网址（成功版for网址一一对应）

        html2=requests.get(tp+i.get("href"))
        soup2=BeautifulSoup(html2.text,"lxml")

        t1=soup2.find("div",class_="top border mb16")
        s3=t1.get_text(strip=True,separator="|")
        s3=re.sub(r'\s+',' ',s3)
        print(s3)#soup2.find("div",class_="top border mb16").get_text(strip=True,separator="|"))#子页第一部分信息
        t2=soup2.find("div",class_="abs")
        s4=t2.get_text(strip=True,separator="|")
        s4=re.sub(r'\s+',' ',s4)
        print(s4)#soup2.find("div",class_="abs").get_text(strip=True,separator="|"))#子页第二部分信息；一二部分可以放在一个print里
        print("\n")

        a1.append([s1,s2,s3,s4])
        with open('wmhs.csv','w')as ff:
            writer=csv.writer(ff)
            writer.writerow(['我','们','很','帅'])
            for row in a1:
                writer.writerow(row)

#get_wmhs()