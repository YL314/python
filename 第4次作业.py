# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:25:39 2018

@author: ASUS
"""

url='http://api.openweathermap.org/data/2.5/forecast?q=hetian,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)

print('day1')
print('temperature'+str(data['list'][2]['main']['temp']))
print('weather'+str(data['list'][2]['weather'][0]['description']))
print('pressure'+str(data['list'][2]['main']['pressure']))
print('Maximum temperature'+str(data['list'][2]['main']['temp_max']))
print('Minimum temperature'+str(data['list'][2]['main']['temp_min']))
print('~~~~~~~~~~~')
print('day2')
print('temperature'+str(data['list'][10]['main']['temp']))
print('weather'+str(data['list'][10]['weather'][0]['description']))
print('pressure'+str(data['list'][10]['main']['pressure']))
print('Maximum temperature'+str(data['list'][10]['main']['temp_max']))
print('Minimum temperature'+str(data['list'][10]['main']['temp_min']))
print('~~~~~~~~~~~')

print('day3')
print('temperature'+str(data['list'][18]['main']['temp']))
print('weather'+data['list'][18]['weather'][0]['description'])
print('pressure'+str(data['list'][18]['main']['pressure']))
print('Maximum temperature'+str(data['list'][18]['main']['temp_max']))
print('Minimum temperature'+str(data['list'][18]['main']['temp_min']))
print('~~~~~~~~~~~')

print('day4')
print('temperature'+str(data['list'][26]['main']['temp']))
print('weather:'+data['list'][26]['weather'][0]['description'])
print('pressure:'+str(data['list'][26]['main']['pressure']))
print('Maximum temperature:'+str(data['list'][26]['main']['temp_max']))
print('Minimum temperature:'+str(data['list'][26]['main']['temp_min']))
print('~~~~~~~~~~~')

print('day5')
print('temperature:'+str(data['list'][34]['main']['temp']))
print('weather:'+str(data['list'][34]['weather'][0]['description']))
print('pressure:'+str(data['list'][34]['main']['pressure']))
print('Maximum temperature:'+str(data['list'][34]['main']['temp_max']))
print('Minimum temperature:'+str(data['list'][34]['main']['temp_min']))
print('~~~~~~~~~~~')

#气温折线图
print('温度折线图如下')
print('day1'+'-'*int(data['list'][0]['main']['temp']))
print('day2'+'-'*int(data['list'][10]['main']['temp']))
print('day3'+'-'*int(data['list'][18]['main']['temp']))
print('day4'+'-'*int(data['list'][26]['main']['temp']))
print('day5'+'-'*int(data['list'][34]['main']['temp']))
print('~~~~~~~~~~~')

#排序
print('排序如下')
temper=[data['list'][0]['main']['temp'],
             data['list'][10]['main']['temp'],
             data['list'][18]['main']['temp'],
             data['list'][26]['main']['temp'],
             data['list'][34]['main']['temp']]
print(sorted(temper))


