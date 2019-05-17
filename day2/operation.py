# -*- coding: utf-8 -*-
"""
Created on Thu May  9 00:02:49 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""
list1 = [5,2,6,2,3]
def add(list1):
    s=0
    for i in list1:
        s = s + i
    return s
def multi(list1):
    multiple =1
    for i in list1:
        multiple = multiple*i
    return multiple
def largest(list1):
    list1.sort()
    return list1[-1]
def smallest(list1):
    list1.sort()
    return list1[0]
def sorting(list1):
    list2 = ()
    list2 = sorted(list1)
    return list2
def remove_dup(list1):
    for i in list1:
        pass
def print_all(list1):
    print('sum= '+str(add(list1)))
    print('multiply = '+str(multi(list1)))
    print('large = '+str(largest(list1)))
    print('small = '+str(smallest(list1)))
    print('sort = '+str(sorting(list1)))
    
