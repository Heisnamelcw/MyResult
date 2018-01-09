

import requests
import json
from bs4 import BeautifulSoup
import time
import pandas as pd
if __name__=='__main__':
    l1=[]
    
    for nums in range(3001,3501):
        api='http://ts.21cn.com/front/api/includePage/indexPcMorePost.do?order=ctime&pageNo={}&pageSize=10'.format(nums)
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
        req=requests.get(url=api,headers=headers)
        req.encoding='utf-8'
        htmls=json.loads(req.text,encoding='utf-8')
        html=htmls['message']
        soup=BeautifulSoup(html,'lxml')
        try:
            for na in soup.find_all('div',class_='ind_list_all'):
                t1=na.select('dl dt p')[0].text.strip()#投诉时间及人物
                # t2=na.select('dd.desc')[0].text.strip()#投诉具体内容。此部分会有空白情况出现
                t3=na.select('span.label a')[0].text#投诉标签/对象
                l1.append([t1,t3])
                print(t1,t3)
            time.sleep(0.5)
        except:continue

    
    df=pd.DataFrame(l1)
    df.columns=['time','label']
    df.to_csv('tsww.csv')