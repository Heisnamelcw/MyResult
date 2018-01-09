#爬取所有页数版
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import csv,re


next_page='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&p=1&isadv=0'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

soup1_list=[]
soup2_list=[]
pages=1

while next_page:    
    req=requests.get(url=next_page,headers=headers)
    html1=req.text
    soup1=BeautifulSoup(html1,'lxml')

    for i in soup1('table',class_='newlist')[1:]:
        if 'jobs.zhaopin'in i.select_one('td.zwmc > div > a')['href']:
            
            zwmc=i.select('td.zwmc > div > a')[0].text
            # print(zwmc)
            uhref=i.select_one('td.zwmc > div > a')['href']
            # print(uhref)
            gsmc=i.select('td.gsmc')[0].text
            # print(gsmc)
            zwyx=i.select('td.zwyx')[0].text
            # print(zwyx)
            gzdd=i.select('td.gzdd')[0].text
            # print(gzdd)
            riqi=i.select('td.gxsj')[0].text
            # print(riqi)
        #数据加入列表中
            soup1_list.append([zwmc,uhref,gsmc,zwyx,gzdd,riqi])

            #获取，子一页网址,解析，优化，防封 
            html2=requests.get(uhref).text
            soup2=BeautifulSoup(html2,'lxml')

        for j in soup2.find_all('div',class_='terminalpage-left'):
            content1=j.select('ul.terminal-ul.clearfix')[0].text.strip()
            content1=''.join(content1.split())
            content1=re.sub(r'\s','',content1)
#             print(content1)
            content2=j.select('div.tab-inner-cont')[0].text.strip()
            content2=''.join(content2.split())
            content2=re.sub(r'\s','',content2)
#             print(content2)
            soup2_list.append([content1,content2])
    try:
        next_page=soup1.select_one('a.next-page')['href']   #尝试获取下一页链接
        pages+=1
        print('进入下一页：第{}页'.format(pages))
    except:
        next_page=None
        print('爬取完毕，总共爬取{}页'.format(pages))

    df1=pd.DataFrame(soup1_list)   #转为DataFrame
    df2=pd.DataFrame(soup2_list)
    df1['6']=df2[[0]]                #加入列
    df1['7']=df2[[1]]
    df1.columns=['职位名称','链接','公司名称','月薪','工作地点','发布日期','要求','职责']#修改全部列名；
    df1.to_csv('可翻页完整版11-22.csv')        #导出为csv文件