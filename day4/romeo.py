# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:14:45 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""
text_file=open("romeo.txt")
list1=[]
while True:
    read=text_file.readline()
    
    if not read:
        break
    list1.append(read.split(' '))
    print(read)
dict1={}
for i in list1:
    for j in i:
        if j in dict1:
            dict1[j]=dict1[j]+1
        else:
            dict1[j]=1
text_file.close()
    