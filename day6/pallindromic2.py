# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:23:55 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic2.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      You need to develop using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""
s = [int(i)for i in input().split(',')] 
if (all(list(map(lambda x:True if x>0 else False,s)))):
     s = [str(i)for i in s]
     if(any(list(map(lambda x:True if x[::-1]==x else False,s)))):
         print('true')
     else:
         print('false')
else:
    print('false')