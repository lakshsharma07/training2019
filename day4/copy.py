# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:37:43 2019

@author: Lakshay
"""


"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""

file1 = open("copy.txt", "wt")
file2=open("words.txt", "rt")

for line in file2:
    file1.write(line)
file1.close()
file2.close()