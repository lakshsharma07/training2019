# -*- coding: utf-8 -*-
"""
Created on Fri May 10 00:38:54 2019

@author: Lakshay
"""
"""
Two words are anagrams if you can rearrange the letters of one to spell the second.  
For example, the following words are anagrams:

 ['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']

Hint: How can you tell quickly if two words are anagrams?  
Dictionaries allow you to find a key quickly.  

"""
user_input1=input()
user_input2=input()
od1={}
for i in user_input1:
    if i in od1:
        od1[i]=od1[i]+1
    else:
        od1[i]=1
od2={}
for i in user_input2:
    if i in od2:
        od2[i]=od2[i]+1
    else:
        od2[i]=1
if(od1 == od2):
    print("anagrams")
else:
    print("not anagram")