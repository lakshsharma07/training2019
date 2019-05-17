# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:35:57 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""

file_name=input()
fp=open(file_name)
print(fp.readlines()[-1])
fp.close()


