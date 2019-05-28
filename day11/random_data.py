# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:02:45 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""

import numpy as np

random_number=np.int_(15-10*np.random.random(40)) 
#or     np.random.randint( 5, 15, 40 )
#using bitcount
frequency=np.bincount(random_number).argmax()
print ( "The most Frequent Number is",frequency )


#method 2
from collections import Counter
count=(Counter(random_number).most_common())[0][0]