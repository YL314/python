# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:10:44 2018

@author: ASUS
"""
#湖南  裙子数据
import urllib.request as r
f=open('湖南数据.txt','w',encoding='utf-8')

for i in range(0,100):
    url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E6%B9%96%E5%8D%97&s=?(i*44)&ajax=true'
    data=r.urlopen(url).read().decode('utf-8','igore')
    f.write(data+'\n')
    print('完成'+str(i+1)+'页')
f.close()
print ('爬取完成')