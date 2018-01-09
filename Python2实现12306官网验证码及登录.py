#-*- coding:utf-8 -*-
#python2在pycharm运行时必须要有上面那一行


import urllib2,urllib
import ssl
import cookielib
from json import loads

if __name__=='__main__':

    #以下4行代码是为了将两个定义的函数统一为同一对象
    c=cookielib.LWPCookieJar()#存储cookie对象
    cookie=urllib2.HTTPCookieProcessor(c)
    opener=urllib2.build_opener(cookie)
    urllib2.install_opener(opener)

    #略过验证
    'https://kyfw.12306.cn/passport/web/login'

    ssl._create_default_https_context=ssl._create_unverified_context
    #请求头
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    def getCode():
        #url_png是图片验证码所对应的链接，鼠标右键可复制得到
        url_png='https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.7992913432645445'
        req=urllib2.Request(url=url_png,headers=headers)
        # req.headers=headers   //  req.add_header('','')
        codeFile=opener.open(req).read()
        with open('code.png','wb')as fn:
            fn.write(codeFile)
        #到此，图片已经实时存入当前目录下，且已经保存
    def login():
        getCode()#获取刚刚新鲜保存的图片
        code=raw_input('请输入验证码: ')  #py3是直接input

        data = {
            'answer': code,   # 坐标型验证码，输入正确验证码坐标
            'login_site': 'E',
            'rand': 'sjrand'
        }
        data = urllib.urlencode(data)   # 把字典转换成查询字符串
        url_check='https://kyfw.12306.cn/passport/captcha/captcha-check'   #检验验证码的链接

        req=urllib2.Request(url=url_check,data=data,headers=headers)#post类型,data不为空即为post类型
        html=opener.open(req,data=data).read()    #打开网址，提供至少一个参数：url/req
        print html
        result=loads(html)
        print result

        if result['result_code']=="4":
            print '验证码校验成功'
        #     #成功后开始着手登录
            from user import pad
            data={
                'username': 'QQ694367819',
                'password': pad,
                'appid': 'otn',
            }#此data包含账号密码
            data=urllib.urlencode(data)
            req = urllib2.Request('https://kyfw.12306.cn/passport/web/login',data=data,headers=headers)  # 登录的url
            htmls=opener.open(req,data=data).read()
            print htmls
        else:
            print '验证码校验失败'
            login()#失败就再次调用函数进行校验


    login()#首次调用函数校验

    #code（）和login（）两者之间是相互独立的，这个时候需要session来判定二者的为同一个