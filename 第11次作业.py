# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 11:01:39 2018

@author: ASUS
"""

#可视化
#学校
view=open('黑吉上分析数据.txt',encoding='gbk').readlines()
school=[]
for line in view:            
    school.append(line.split(',')[0].split('(')[1])
print(school)
#人数
view1=open('黑吉上分析数据.txt',encoding='gbk').readlines()
people=[]
for line in view1:            
    people.append(int(line.split(',')[1].split(')')[0]))
print(people)