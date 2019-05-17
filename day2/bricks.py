# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:04:00 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""
briks_inf = list(input())

x = briks_inf[0]*1
y = briks_inf[1]*5
target=briks_inf[2]

if((x+y)<=target):
    print('true')
else:
    print('false')
