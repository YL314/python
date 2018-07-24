# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 21:42:48 2018

@author: ASUS
"""

f1=open('all_school.txt',encoding='utf-8').readlines()
print ('学校的编号为：\n')
for i in range(len(f1)):
    print (f1[i].split('-jianjie-')[1].split('.')[0])

f2=open('all_city.txt',encoding='utf-8').readlines()
print ('城市对应的编号为：\n')
for k in range(1,32):
    print(f2[k].split('<li data-val=')[1].split('data-id')[0]+f2[k].split('claimCity')[1].split(')">')[0])