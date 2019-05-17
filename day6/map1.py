# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:05:01 2019

@author: Lakshay
"""

"""
Code Challenge
  Filename: 
    map1.py
  Problem Statement:
import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

for i in range(len(names)):
    names[i] = random.choice(code_names)

print (names)

As you can see, this algorithm can potentially assign the same secret code name to multiple secret agents. 


Rewrite the above code using map and lambda.


"""

import random
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
names=list(map(lambda x: random.choice(code_names),['Mary', 'Isla', 'Sam']))
print(names)