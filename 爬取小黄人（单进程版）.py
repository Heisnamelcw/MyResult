def get_xhmen():  #完整版可实现自动翻页，不足：是否每一页都可创个文件夹？ 是否能更快？是否能封装成一个py文件
    import re
    import requests
    from bs4 import BeautifulSoup

    next_page = 'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1460997499750_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=UTF-8&word=%E5%B0%8F%E9%BB%84%E4%BA%BA'
    headers={'Remote Address':'14.215.177.185:80'}

    #只会显示一页的图片，因为每次翻页后，i被覆盖从0开始。
    i=0
    while next_page:
        top='http://image.baidu.com'
        html = requests.get(url,headers=headers).text

        soup=BeautifulSoup(html,'lxml')
        pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
        #i = 0
        for each in pic_url:
            print (each)
            try:
                pic= requests.get(each, timeout=10)#响应超时就报错
            except requests.exceptions.ConnectionError:
                print ('【错误】当前图片无法下载')
                continue
            string=('D:\R\picture'+str(i) + '.jpg')
            fp = open(string,'wb')
            fp.write(pic.content)
            fp.close()
            i += 1
        try:
            next_page=top+soup.select_one('a.n')['href']

            print('前往下一页！！！')
        except:
            next_page=None
