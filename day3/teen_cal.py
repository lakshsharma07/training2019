# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:39:40 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""
dict1={}
while True:
    user_input=input()
    user_input=user_input.split(',')
    print(user_input)
    
    if not user_input:
        break
    
def fix_teen(n):
    if n in range(13,19):
        if n in range(15,16):
            break
    else:
        n=0
        return n