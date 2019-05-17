# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:04:03 2019

@author: Lakshay
"""

print("enter marks of assignment out of 100")
ass1 = float(input())
ass2 = float(input())
ass3 = float(input())

print("enter marks of exam out of 100")
exam1 = float(input())
exam2 = float(input())

weight = ((ass1 + ass2 + ass3)*.1) +(( exam1 + exam2)*.35)
print (weight)
