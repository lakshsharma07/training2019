"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters
    (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""

# accetping string from user and parsing it into List.
user_input = input("Enter String: ")

character_frequency = {}       # initialising the Dict.

# loop to access every element of the list individually.
for alphabet in user_input:

    # adding every element as a 'key' and its frequency of occurance
    #as 'value' in the Dict.
    character_frequency[alphabet] = character_frequency.get(alphabet,0) + 1
    
print (character_frequency)


########## Pythonic Code ##########
'''
from collections import Counter

print (dict(Counter(user_input)))'''