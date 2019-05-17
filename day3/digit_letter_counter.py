# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:29:34 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""
user_input1=list(input())
dict={'letters':0,'digits':0}
for i in user_input1:
    if (i.isdigit()):
        dict['digits']=dict['digits']+1
    else:
        dict['letters']=dict['letters']+1
        
print('p'.isdigit)