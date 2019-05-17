# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:50:05 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""
fp=open("absentee.txt","w+")
for i in range(0,25):
    user_input=input()
    
    if not user_input:
        break
    fp.writelines(user_input + "\n")
fp.seek(0,0)    
read=fp.read()
print(read)
fp.close()