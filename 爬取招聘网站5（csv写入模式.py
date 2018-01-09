import requests
import re,os,xlwt
import time
import pandas as pd
t1=time.time()
book=xlwt.Workbook()
sheet=book.add_sheet('sheet',cell_overwrite_ok=True)
path='D://JAVA'
os.chdir(path)

l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
for nums in range(1,91):   
    url='http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%e5%85%a8%e5%9b%bd&kw=%e6%95%b0%e6%8d%ae%e5%88%86%e6%9e%90%e5%b8%88&sm=0&isfilter=0&fl=489&isadv=0&sg=8dc19983b7db4e218c229744d7dd0766&p={}'.format(nums)
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
    req=requests.get(url=url,headers=headers)
    html=req.text
    # print(html)


    pat1='font-weight: bold.*?>(.*?)</a>'#职位名称
    pat2='gsmc"><a href.*?>(.*?)</a>'#公司名称
    pat3='<td class="zwyx">(.*?)</td>'#月薪
    pat4='<td class="gzdd">(.*?)</td>'#工作地点
    pat5='font-weight.*?href="(.*?)" target='#职位链接


    r1=re.compile(pat1).findall(html)
    r2=re.compile(pat2).findall(html)
    r3=re.compile(pat3).findall(html)
    r4=re.compile(pat4).findall(html)
    r5=re.compile(pat5).findall(html)
    l1.extend(r1)
    l2.extend(r2)
    l3.extend(r3)
    l4.extend(r4)
    l5.extend(r5)


    j=0
    for i in range(0,len(l1)):
        try:
            zhiwei=l1[i]
            gsmc=l2[i]
            yx=l3[i]
            dd=l4[i]
            zwurl=l5[i]

            sheet.write(i+1,j,zhiwei)#行，列，对应标签值 特意空一行
            sheet.write(i+1,j+1,gsmc)
            sheet.write(i+1,j+2,yx)
            sheet.write(i+1,j+3,dd)
            sheet.write(i+1,j+4,zwurl)
        except Exception as e:
            print('出现异常'+str(e))
            continue
            

t2=time.time()
book.save('D://JAVA/shujufenxi90.xls')
t3=t2-t1
print('ok搞定!spenttime:{}'.format(t3))#notebook--71.03s