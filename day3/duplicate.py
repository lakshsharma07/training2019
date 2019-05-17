# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:54:34 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""
input_list=input()
input_list=input_list.split(',')
set(input_list)

list1=[]
for i in input_list:
    if i in list1:
        continue
    else:
        list1.append(i)