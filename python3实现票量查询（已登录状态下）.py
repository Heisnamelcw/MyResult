import requests
import ssl
import json

#车次为深圳--赣州 共计20趟
ssl._create_default_https_context=ssl._create_unverified_context

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

def getTrainList():
    url="https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2018-01-10&leftTicketDTO.from_station=SZQ&leftTicketDTO.to_station=GZG&purpose_codes=ADULT"
    
    req=requests.get(url=url,headers=headers)
    #   req.encoding='utf-8'
    html=json.loads(req.text,encoding='utf-8')
    result=html['data']['result']
    return result
    #   print(result)
c=0
for i in getTrainList():
    #【23】==软卧
    #【28】==硬卧
    tmp_list=i.split('|')
#     for n in tmp_list:
#         print('[{}]{}'.format(c,n))
#         c+=1
    if tmp_list[23]==u'有':
        print('软卧有票且充足')
    elif tmp_list[23]==u'无' or tmp_list[23]=='':
        print('软卧无票无法出售')
    elif int(tmp_list[23])>0:
        print('软卧有票,余票{}张'.format(int(tmp_list[23])))
    else:
        print('软卧无票刚卖完')#int([23]==0)
        
    if tmp_list[28]==u'有':
        print('硬卧有票且充足')
    elif tmp_list[28]==u'无'or tmp_list[28]=='':
        print('硬卧无票无法出售')
    elif int(tmp_list[28])>0:
        print('硬卧有票，余票{}.张'.format(int(tmp_list[28])))
    else:
        print('硬卧无票刚卖完')
#     break