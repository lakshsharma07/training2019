# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:02:30 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""
user_input=list(input())
od={}
for i in user_input:
    if i in od:
        od[i]=od[i]+1
    else:
        od[i]=1
od=sorted(od)
    
    

from collections import OrderedDict 
od=OrderedDict()
type(od)