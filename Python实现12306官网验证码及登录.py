import requests
import ssl
import json
from urllib import request,parse
from http import cookiejar

c=cookiejar.CookieJar()
cookies=request.HTTPCookieProcessor(c)
opener=request.build_opener(cookies)
request.install_opener(opener)

ssl._create_default_https_context=ssl._create_unverified_context

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
}

def getCode():#登录的主界面，获取验证码图片，为验证做铺垫
    req=request.Request('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.8130287058531029')
    req.headers=headers
    codeFile=opener.open(req).read()
    with open('code.png','wb')as fn:
        fn.write(codeFile)

def login():
    getCode()#已经获取验证码，准备输入正确验证码坐标，然后检测账号密码，然后登录
    code=input('请输入验证码： ')
    req=request.Request('https://kyfw.12306.cn/passport/captcha/captcha-check')
    url2='https://kyfw.12306.cn/passport/captcha/captcha-check'
    req.headers=headers
    data={
    'answer':code,
    'login_site':'E',
    'rand':'sjrand'
    }
    data=parse.urlencode(data).encode('utf-8')
    req2=request.Request(url=url2,data=data,headers=headers)
    response2=opener.open(req2)
    html2=response2.read().decode('utf-8')
    print(html2)
    # html=opener.open(req,data=data).read()
    # print(html)
    result=json.loads(html2,encoding='utf-8')
    
    if result['result_code']=="4":
        print('验证成功you do it！')
        from user import pad
        url3='https://kyfw.12306.cn/passport/web/login'#登录的url
        data={
            'username': 'QQ694367819',
            'password': pad,
            'appid': 'otn',
        }#此data包含账号密码
        data=parse.urlencode(data).encode('utf-8')
        req3=request.Request(url=url3,data=data,headers=headers)
        response3=opener.open(req3)
        html3=response3.read().decode('utf-8')
        print(html3)
    else:
        print('验证失败 oh no you are field！')
        login()#再次执行验证操作


login()#首次启动次函数