from urllib.request import urlretrieve
import requests
import os

"""

函数之一*********说明:下载《王者荣耀盒子》中的英雄图片******可以独立拿出来运行
Parameters:
    url - GET请求地址，通过Fiddler抓包获取
    header - headers信息
Returns:
    无
Author:
    Jack Cui
Blog:
    http://blog.csdn.net/c406495762
Modify:
    2017-08-07
"""
def hero_imgs_download(url, header):  #参数：链接，代理
    req = requests.get(url = url, headers = header).json()#读取json格式
    hero_num = len(req['list'])              #通过json内容，统计英雄数量
    print('一共有%d个英雄' % hero_num)
    hero_images_path = 'hero_images'         #定义一个文件夹名字，可以不存在
    for each_hero in req['list']:            #在内容列表中循环
        hero_photo_url = each_hero['cover']   #找到英雄图片地址：‘xxx.png’
        hero_name = each_hero['name'] + '.jpg'     #找到英雄名字地址，另存时需要存为jpg格式，
        filename = hero_images_path + '/' + hero_name   #存放在文件夹之下，以及格式
        if hero_images_path not in os.listdir():       #检测文件夹是否存在，不存在则在当前目录下创建此文件夹
            os.makedirs(hero_images_path)
        urlretrieve(url = hero_photo_url, filename = filename)  #快速另存图片的函数：地址，名称格式
    hero_imgs_download(heros_url,headers)              #封装后运行的命令
"""
函数之二*********说明:打印所有英雄的名字和ID**********
Parameters:
    url - GET请求地址，通过Fiddler抓包获取
    header - headers信息
Returns:
    无
Author:
    Jack Cui
Blog:
    http://blog.csdn.net/c406495762
Modify:
    2017-08-07
"""
def hero_list(url, header):
    print('*' * 100)               #100个***
    print('\t\t\t\t欢迎使用《王者荣耀》出装小助手！')#4个tab
    print('*' * 100)
    req = requests.get(url = url, headers = header).json() #英雄所有信息均在req【‘list’】下
    flag = 0
    for each_hero in req['list']:   
        flag += 1
        print('%s的ID为:%-7s' % (each_hero['name'], each_hero['hero_id']), end = '\t\t')   #英雄名称：ID \t\t 英雄名称：ID \t\t  间隔俩tab
        if flag == 3:                  #一行最多显示3个，超过三个就换行，末尾以空格结束
            print('\n', end = '')
            flag = 0

"""
函数说明:根据equip_id查询武器名字和价格
Parameters:
    equip_id - 武器的ID
    weapon_info - 存储所有武器的字典
Returns:
    weapon_name - 武器的名字
    weapon_price - 武器的价格
Author:
    Jack Cui
Blog:
    http://blog.csdn.net/c406495762
Modify:
    2017-08-07
"""
def seek_weapon(equip_id, weapon_info):   #一个函数，通过第一个参数条件进行判定，第二个参数是链接的来源
    for each_weapon in weapon_info:
        if each_weapon['equip_id'] == str(equip_id):  #如果对应武器ID匹配，那么武器名字与价格必定一样
            weapon_name = each_weapon['name']    #于是赋值，将对应id 的武器名与武器价格赋值给参数
            weapon_price = each_weapon['price']
            return weapon_name, weapon_price    #判定结束后，满足条件返回两个下面需要用到的值


"""
函数说明:获取并打印出装信息
Parameters:
    url - GET请求地址，通过Fiddler抓包获取
    header - headers信息
    weapon_info - 存储所有武器的字典
Returns:
    无
Author:
    Jack Cui
Blog:
    http://blog.csdn.net/c406495762
Modify:
    2017-08-07
"""
def hero_info(url, header, weapon_info):  #参数：英雄地址链接，代理，武器库信息
    req = requests.get(url = url, headers = header).json()
    print('\n历史上的%s:\n    %s' % (req['info']['name'], req['info']['history_intro']))#打印对应英雄名字的相关历史
    for each_equip_choice in req['info']['equip_choice']:  #出装多样化，
#       print('\n%s:\n   %s' % (each_equip_choice['title'], each_equip_choice['description']))  #打印出装模式主题以及描述。如：进攻性装备：怎么怎么样
        total_price = 0
        flag = 0
        for each_weapon in each_equip_choice['list']:
            flag += 1                              #等号右边是一个函数，但是函数返回的两个值与等号左边可以匹配的上，判定条件在函数内进行了
            weapon_name, weapon_price = seek_weapon(each_weapon['equip_id'], weapon_info)   #武器名与武器价格通过匹配的武器id可以确定下来
            print('%s:%s' % (weapon_name, weapon_price), end = '\t')
            if flag == 3:                                  #最多显示三套出装推荐
                print('\n', end = '')                      #换行，空格结尾
                flag = 0
            total_price += int(weapon_price)              #总价为int型
        print('神装套件价格共计:%d金币' % total_price)


"""
函数说明:获取武器信息
Parameters:
    url - GET请求地址，通过Fiddler抓包获取
    header - headers信息
Returns:
    weapon_info_dict - 武器信息
Author:
    Jack Cui
Blog:
    http://blog.csdn.net/c406495762
Modify:
    2017-08-07
"""
def hero_weapon(url, header):#这里的url为weapon_url    即武器库的链接
    req = requests.get(url = url, headers = header).json()
    weapon_info_dict = req['list']   #获取武器库信息
    return weapon_info_dict   #返回武器库字典值


if __name__ == '__main__': #需要用到的就2个链接，英雄链接，武器库链接，
    headers = {'Accept-Charset': 'UTF-8',
            'Accept-Encoding': 'gzip,deflate',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI 5 MIUI/V8.1.6.0.MAACNDI)',  #代理json下有
            'X-Requested-With': 'XMLHttpRequest',
            'Content-type': 'application/x-www-form-urlencoded',
            'Connection': 'Keep-Alive',
            'Host': 'gamehelper.gm825.com'}
    weapon_url = "http://gamehelper.gm825.com/wzry/equip/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8"
    heros_url = "http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8"
    hero_list(heros_url, headers)
    hero_id = input("请输入要查询的英雄ID:")
    hero_url = "http://gamehelper.gm825.com/wzry/hero/detail?hero_id={}&channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8".format(hero_id)
    weapon_info_dict = hero_weapon(weapon_url, headers)  #武器字典来源的链接为武器库链接
    hero_info(hero_url, headers, weapon_info_dict)   #运行命令开端---三个参数