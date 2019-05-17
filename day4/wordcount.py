# -*- coding: utf-8 -*-
"""
Created on Fri May 10 19:13:35 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""
file_name=input()
fp=open(file_name)
def word_count(fp):
    x,y=0,0
    fp=open(file_name)
    list1=fp.read()
    for i in list1:
        x=x+1
    list1=list1.split()
    for i in list1:
        y=y+1
    z=0
    fp.seek(0,0)
    list1=fp.read()
    list1=list1.split('\n')
    for i in list1:
        z=z+1
    fp.seek(0,0)
    list1=fp.read()
    list1=list1.split()
    dict1={}
    for i in list1:
        if i in dict1:
            dict1[i]=dict1[i]+1
        else:
            dict1[i]=1
        c=0
        for i in dict1:
            if (dict1[i]==1):
                c=c+1
    return (x,y,z-1,c)
    fp.close()

    
