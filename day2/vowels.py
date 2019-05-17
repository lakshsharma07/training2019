# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:25:51 2019

@author: Lakshay
"""
"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and while
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'clfrn', 'klhm', 'flrd']
    
"""

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowels = "aeiou"
final_list = []

for state in state_name:
    temp = []
    for letter in state.lower():
        if letter in vowels:
            continue
        temp.append(letter)
    final_list.append("".join(temp))

for state in state_name:
    state = list(state.lower())
    for letter in state:
        if letter in vowels:
            state.remove(letter)
    final_list.append("".join(state))

print(final_list)       