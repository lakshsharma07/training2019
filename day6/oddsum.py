# -*- coding: utf-8 -*-
"""
Created on Tue May 14 00:11:17 2019

@author: Lakshay
"""

"""
This Python function accepts a list of numbers and computes the product of all the odd numbers:

def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result
    
Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))

    
"""
from functools import reduce
def productOfOdds(list):
    return reduce(lambda x,y:x+y, filter(lambda x: x%2 == 1, list))


[2,18,9,22,17,24,8,12,27]