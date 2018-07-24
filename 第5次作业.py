# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
weather(1,2)
weather(2,10)
weather(3,18) 
weather(4,26)
weather(5,34)

def chart(t):
    return '-'*int(data['list'][t]['main']['temp'])
print('温度折线图：')
print('1'+chart(2))
print('2'+chart(10))
print('3'+chart(18))
print('4'+chart(26))
print('5'+chart(34))