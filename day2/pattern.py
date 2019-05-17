# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:37:37 2019

@author: Lakshay
"""


"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""

print("enter no of max stars")
x = input();
str1 = (" *"*int(x))
for i in range(1,int(x)+1):
    print('*'*i)
for i in range(1,int(x)):
    i=int(x)-i
    print('*'*i)