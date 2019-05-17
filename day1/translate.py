# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:07:39 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""
str1 = ('aeiou')
user_input = input()
final_list = []
def translate(user_input):
    temp =str[]
    for i in user_input:
        if i in str1:
            continue
        temp.append(i,i+'o'+i)
        final_list.append("".join(temp))
    print(final_list)
    

