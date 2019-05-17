# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:05:50 2019

@author: Lakshay
"""

i=0
while i<=100 :
    if((i%3 == 0) and ( i%5 == 0)):
        print('fizzbuzz')
    elif(i%3 == 0 ):
        print('fizz')
    elif(i%5 == 0):
        print('buzz')
    else:
        print(i)
    i=i+1