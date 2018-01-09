# 完整可翻页版，但是右侧信息有漏，疑问待解决
def get_zhaopin_news():
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import numpy as np
    import csv,re

    soup1_list=[]
    soup2_list=[]
    next_page='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&p=1&isadv=0'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

    while next_page:
        html1=requests.get(next_page,headers=headers).text
        soup1=BeautifulSoup(html1,'html.parser')

        try:
            for i in soup1('table',class_='newlist')[1:]: 
                zwmc=i.select('td.zwmc > div > a')[0].text
                print(zwmc)
                uhref=i.select_one('td.zwmc > div > a')['href']
                print(uhref)
                gsmc=i.select('td.gsmc')[0].text
                print(gsmc)
                zwyx=i.select('td.zwyx')[0].text
                print(zwyx)
                gzdd=i.select('td.gzdd')[0].text
                print(gzdd)
                riqi=i.select('td.gxsj')[0].text
                print(riqi)
            #数据加入列表中
                soup1_list.append([zwmc,uhref,gsmc,zwyx,gzdd,riqi])

                #获取，子一页网址,解析，优化，防封 
                html2=requests.get(uhref).text
                soup2=BeautifulSoup(html2,'lxml')

                for j in soup2.find_all('div',class_='terminalpage-left'):
                        content1=j.select('ul.terminal-ul.clearfix')[0].text.strip()
                        conten1=''.join(content1.split())
                        content1=re.sub(r'\s','',content1)
                        print(content1)
                        content2=j.select('div.tab-inner-cont')[0].text.strip()
                        conten2=''.join(content2.split())
                        content2=re.sub(r'\s','',content2)
                        print(content2)
                        soup2_list.append([conten1,content2])


        except:
            continue


    #     df1=pd.DataFrame(soup1_list)   #转为DataFrame
    #     df2=pd.DataFrame(soup2_list)
    #     df1['6']=df2[[0]]                #加入列
    #     df1['7']=df2[[1]]
    #     df1.columns=['职位名称','链接','公司名称','月薪','工作地点','发布日期','要求','职责']#修改全部列名；
    #     df1.to_csv('y1.csv') 


        try:
            next_page=soup1.select_one('li.pagesDown-pos > a')['href']   #尝试获取下一页链接
            print('前往下一页！！！！！！！！！！！！！')
        except:
            next_page=None

        df1=pd.DataFrame(soup1_list)   #转为DataFrame
        df2=pd.DataFrame(soup2_list)
        df1['6']=df2[[0]]                #加入列
        df1['7']=df2[[1]]
        df1.columns=['职位名称','链接','公司名称','月薪','工作地点','发布日期','要求','职责']#修改全部列名；
        df1.to_csv('可翻页完整版.csv')        #导出为csv文件
