def get_biqu():
    import requests,re,csv,sys,time
    from bs4 import BeautifulSoup
    
    list_names=[]
    list_urls=[]
    list_contents=[]
    
    url='http://www.biqukan.com/1_1094/'
    top='http://www.biqukan.com/'
    url1='http://www.biqukan.com/1_1094/5403177.html'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

    req=requests.get(url,headers=headers)
    html=req.text
    soup=BeautifulSoup(html,'lxml')
    #print(soup.prettify())
    #分割线，以上全部为准备工作，把网页格式标准化

    name1=soup.select('div.listmain')#查找
    name2=BeautifulSoup(str(name1))#缩小范围，优化成标准格式
    name3=name2.find_all('a')[15:]#确定起点，获取长度
    nums=len(name3)
    #name3

    f=open('D:\\spython\一念永恒.txt','a',encoding='utf-8') #创建空txt文档
    print('开始！')
    t_s=time.time()#计时的起点
    for i in range(len(name3)):        #以获取的list长度为循环起点：这样可以保证内容与链接的一致性
        list_names.append(name3[i].string)
        list_urls.append(top+name3[i].get('href'))

    
    for j in range(len(list_urls)):  #同层for循环，但是保证了内容的一致性

        href=list_urls[j]    #获取链接，优化，查找到需要内容
        req2=requests.get(href,headers=headers)
        html2=req2.text
        soup2=BeautifulSoup(html2,'lxml')
        t1=soup2.select('div.showtxt')  #t1的长度必然大于1的
        
        f.write(list_names[j])  #开始写入第一部分
        for k in range(len(t1)):
            t2=t1[k].text.replace('\xa0'*8,'\n\n')
            list_contents.append(t2)  #这个是写给自己看的
            f.write(t2)    #开始写入第二部分
    
    #以下3行技术尚不成熟，待改进，可忽略；技术要求：要时时同步显示下载的进度
    for i in range(len(name3)):
        sys.stdout.write("进度%.3f%%" % float(i/len(name3))+'\r')
        sys.stdout.flush()
        
    t_e=time.time()#计时的终点
    t_spend=t_e-t_s
    print('结束，总计花费时间：{}'.format(t_spend))

    f.close()
    
#get_biqu()