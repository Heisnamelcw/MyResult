import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
import time

if __name__=='__main__':

    nums=1
    url='http://www.hshfy.sh.cn/shfy/gweb2017/flws_list_content.jsp'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

    data={'fydm':'',
    'ah':'',
    'ay':'',
    'ajlb':'%E6%B5%B7%E4%BA%8B',
    'wslb':'',
    'title':'',
    'jarqks':'',
    'jarqjs':'',
    'qwjs':'',
    'wssj':'',
    'yg':'',
    'bg':'',
    'spzz':'',
    'flyj':'',
    'pagesnum':nums,
    'zbah':''}
    list1=[]
    while nums<401:
        req=requests.get(url=url,headers=headers,params=data)
        req.encoding='gbk'
        html=req.text
        soup=BeautifulSoup(html,'lxml')

        change1=soup.find('table')
        soup1=BeautifulSoup(str(change1),'lxml')
        # soup1

        
        for i in soup1.find_all('tr')[1:]:
            a0=i.select('td')[0].text
            a1=i.select('td')[1].text
            a2=i.select('td')[2].text
            a3=i.select('td')[3].text
            a4=i.select('td')[4].text
            a5=i.select('td')[6].text
            a6=i.select('td')[6].text
            list1.append([a0,a1,a2,a3,a4,a5,a6])
            print(a0,a1,a6)
        
        df=pd.DataFrame(list1)
        nums+=1
        time.sleep(2)
        print(nums)

    df.to_csv('shfy3.csv')

# #单页
# import requests
# from bs4 import BeautifulSoup
# import re
# import numpy as np
# import pandas as pd
# url='http://www.hshfy.sh.cn/shfy/gweb2017/flws_list_content.jsp'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
# nums=1
# data={'fydm':'',
# 'ah':'',
# 'ay':'',
# 'ajlb':'%E6%B5%B7%E4%BA%8B',
# 'wslb':'',
# 'title':'',
# 'jarqks':'',
# 'jarqjs':'',
# 'qwjs':'',
# 'wssj':'',
# 'yg':'',
# 'bg':'',
# 'spzz':'',
# 'flyj':'',
# 'pagesnum':nums,
# 'zbah':''}


# req=requests.get(url=url,headers=headers,params=data)
# req.encoding='gbk'
# html=req.text
# soup=BeautifulSoup(html,'lxml')

# change1=soup.find('table')
# soup1=BeautifulSoup(str(change1),'lxml')
# # soup1

# list1=[]
# for i in soup1.find_all('tr')[1:]:
#     a0=i.select('td')[0].text
#     a1=i.select('td')[1].text
#     a2=i.select('td')[2].text
#     a3=i.select('td')[3].text
#     a4=i.select('td')[4].text
#     a5=i.select('td')[6].text
#     a6=i.select('td')[6].text
#     list1.append([a0,a1,a2,a3,a4,a5,a6])
#     print(a0,a1,a2,a3,a4,a5,a6)

# df=pd.DataFrame(list1)
# df