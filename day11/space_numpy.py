# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:19:08 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""

input1=input("enter space seprated data :>")
import numpy as np

input1=input1.split(" ")
x = np.array(input1,int) 
print (type(x))
x=x.reshape(3,3)
print (x)
