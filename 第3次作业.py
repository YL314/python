# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:24:27 2018

@author: ASUS
"""

import urllib.request as r
data=r.urlopen('http://api.openweathermap.org/data/2.5/weather?q=hetian&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','igore')
import json
data=json.loads(data)
data['main']['temp']
data['weather'][0]['description']
data['main']['pressure']
