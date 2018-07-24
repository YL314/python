# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 20:18:50 2018

@author: ASUS
"""

url='http://api.openweathermap.org/data/2.5/forecast?q=hetian,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)

def weather(a,b):
    print('第'+str(a)+'天气情况')
    print('temperature'+str(data['list'][b]['main']['temp']))
    print('weather'+str(data['list'][b]['weather'][0]['description']))
    print('pressure'+str(data['list'][b]['main']['pressure']))
    print('Maximum temperature'+str(data['list'][b]['main']['temp_max']))
    print('Minimum temperature'+str(data['list'][b]['main']['temp_min']))
    a=str(data['list'][b]['weather'][0]['main'])
    if a=='Clear':
        print ('天气晴朗，注意防晒~')
    elif a=='Rain':
        print('下雨天记得带伞~')
    elif  a=='Clouds':
        print('多云的天气最适合郊游啦~')
weather(1,2)
weather(2,10)
weather(3,18) 
weather(4,26)
weather(5,34)




url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180718&ie=utf8&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)

def tb():
    for a in range(0,36):
        print ('第'+str(a+1)+'件商品：')
        print ('标题：'+str(data['mods']['itemlist']['data']['auctions'][a]['title']))
        print ('价格：'+str(data['mods']['itemlist']['data']['auctions'][a]['view_price'] ))
        print ('销量：'+str(data['mods']['itemlist']['data']['auctions'][a]['view_sales']))  
        if (a+1)%4==0:
            print(str('#')*50)
        if a==18:
            break
tb()

def yf():
    for i in range (0,36):
        y=i    
        if float(data['mods']['itemlist']['data']['auctions'][y]['view_fee'])==0.0:
            print ('第'+str(i+1)+'件商品包邮') 
        else:
            print('第'+str(i+1)+'件商品不包邮')
yf()
 