"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values
    with original order reserved  
"""

# given list
given_list =  [12,24,35,24,88,120,155,88,120,155]

# parsing given list into set to remove duplicate entries
# then again parsing it back to list
output_list = list(set(given_list))

# reversing the new list
output_list.reverse()

print(output_list)