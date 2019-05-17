# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:03:58 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""
k=1
integer = input()
integer = integer.split()
for i in integer:
    if(int(i)<0):
        k=0
        break
    if((i == i[::-1])):
        continue
    else:
        k=0
        break
if k==1 :
    print("true")
else:
    print('false')
        
        
for i in integer:
    print(i)
    print(i[::-1])