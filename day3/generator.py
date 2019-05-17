# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:08:31 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""
numbers=input()
print("list1 > "+str(list(numbers.split(','))))
print("tuple > "+str(tuple(numbers.split(','))))

