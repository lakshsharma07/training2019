# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:26:01 2019

@author: Lakshay
"""

# HAND ON 1
list1 = list(range(0,20))
list2 = []
list3 = []
for number in list1:
    if(number%2 == 0):
        print(str(number) + 'even')
        list2.append(number)
    else:
        print(str(number) + 'odd')
        list3.append(number)
    
#Hand on 2
year = input()
def leap_func(year):
    if((year%4 ==0) and (year %100 !=0)):
        print('TRUE')
    elif((year %400 ==0) and(year %100 !=0)):
        print('TRUE')
    else:
        print('FALSE')
        
#Hand on 3
list1 = ['jan','mar','may','july','aug','octo','dec']
list2 = ['april','june','sept','nov']
list3 = ['feb']
 month = input()       
def days_in_month(month):
    if(month in list1):
        print('31 days')
    elif(month in list2):
        print('30 days')
    if(month in list3):
        print('28 days')

