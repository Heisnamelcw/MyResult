#bilibili某房间弹幕
#post在msg下，form在post下

import requests,time

up='https://api.live.bilibili.com/ajax/msg'
form={'roomid':5441,
'token':'',
'csrf_token':''}

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

html=requests.post(up,data=form)
#html.json()['data']['room'][0/1/2..]['text'] 弹幕存放在text里
while True:
    html=requests.post(up,data=form)
    texts=list(map(lambda ii:html.json()['data']['room'][ii]['text'],range(10))) #源代码里长度9个，所以range（10）
    time.sleep(0.5)
    html2=requests.post(up,data=form)
    texts2=list(map(lambda ii:html2.json()['data']['room'][ii]['text'],range(10)))
    ret_list=[print(item)for item in texts2 if item not in texts] #去重！