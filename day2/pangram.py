# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:45:36 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Pangram
  Filename: 
    pangram.py
  Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
  Hint:
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.
  Input: 
    The five boxing wizards jumps.
  Output:
    NOT PANGRAM
"""
sentence = ("The quick brown fox jumps over the lazy dog")
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def check_pangram(sentence):
    k=1
    for i in alpha:
        if i in sentence :
            continue
        else:
            k=0
            break
    if k == 1 :
        print('PANGRAM')
    else:
      print('NOT PANAGRAM')      
        
            