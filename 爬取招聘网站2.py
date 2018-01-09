def get_newway():
    import requests,csv,re
    import pandas as pd
    import numpy as np
    from bs4 import BeautifulSoup

    next_page='http://sou.zhaopin.com/jobs/searchresult.ashx?pd=30&jl=%E6%B7%B1%E5%9C%B3&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&sm=0&p=1&sf=0&st=99999&isadv=1'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
    while next_page:
        menuCode=requests.get(next_page,headers=headers)
        menuCode.encoding='utf-8'
        soup=BeautifulSoup(menuCode.text,'lxml')

        #ss[59]

        f=open('wewill.txt','a',encoding='utf-8')#准备个空的txt用来最终写入的


        list1=[]#三个列表中间要用的
        list2=[]
        list3=[]
        
        menu=soup.find('div',id='newlist_list_div')#找到需要部分，缩小，转为beautifulsoup，更方便下步查询
        values=','.join(str(x)for x in menu)
        soup2=BeautifulSoup(values,'lxml')
        ss=soup2.select('td.zwmc div a') #但凡列表，均有长度，以此为循环入口

        for i in range(0,len(ss)):      #已存在的长度为前提，获取的内容必将一一对应
            list1.append(ss[i].text)
            list2.append(ss[i].get('href'))

        for i in range(0,len(list2)):  #此长度又与上部分保持了一致
            href=list2[i]               #找到对应第i个链接，获取，优化等
            html2=requests.get(href,headers=headers)
            html2.encoding='utf-8'
            soup3=BeautifulSoup(html2.text,'lxml')
            soup4=soup3('div',class_='tab-inner-cont')
            soup4=','.join(str(x)for x in soup4)     #缩小范围的常用手段，二者表面上没区别，其实是兄弟节点
            soup5=BeautifulSoup(soup4,'lxml')
            soup5=soup5.select('div.tab-inner-cont') #找到合适的内容，一般其长度大于1，为下个做铺垫
            soup5
            f.write(list1[i])                               #开始写入第一部分：即主页简略信息
            for j in range(0,len(soup5)-2):               
                ctext=soup5[j].text
                list3.append(soup5[j].text)              #没有写入，只是装入到一个list自己看
                f.write(ctext)                            #开始写入第二部分：即子页详细信息

        try:
            next_page=soup.select_one('a.next-page').get('href')
            print('前往下一页！！！')
        except:
            next_page=None
    f.close()
    df=pd.DataFrame([list1,list2,list3])#并列读入，按列了，需要转置

get_newway()
