# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:22:53 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Mondy', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""
tuple1= ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
tuple2=input()
tuple2=tuple(tuple2.split(','))
for i in tuple1:
    if i in tuple2:
        continue
    else:
        tuple2=tuple2+tuple(i.split(','))
       
        
            
    