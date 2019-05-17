# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:20:50 2019

@author: Lakshay
"""
"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""

user_input = input()

def reverse(user_input):
    print(user_input[::-1])
