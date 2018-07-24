# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 13:56:57 2018

@author: ASUS
"""

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
tb()

p=[]
def price():
    i=[]
    for i in range(0,36):
      p.append(float(data['mods']['itemlist']['data']['auctions'][i]['view_price']))
    return p
price()
c=list(reversed(sorted(p)))
print('价格排序为：')
print(c)

s=[]
def sales():
    i=[]
    for i in range(0,36):
      s.append((data['mods']['itemlist']['data']['auctions'][i]['view_sales']))
    return s
sales()
d=(sorted(s))
print('销量排序为：')
print(d)

def yf():
    for i in range (0,36):
        y=i    
        if float(data['mods']['itemlist']['data']['auctions'][y]['view_fee'])==0.0:
            print ('第'+str(i+1)+'件商品包邮')     
yf()









