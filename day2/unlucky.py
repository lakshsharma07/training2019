# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:31:09 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
"""
array =[13, 1, 2, 13, 2, 1, 13]
j=0
sum = int() 
for i in array:
    if (i == 13) :
        j=1
        continue
    elif (j==1):
        j=0
        continue
    else:
        j=0
        sum = sum + i
print(sum)    
        
   
   
   
    
    