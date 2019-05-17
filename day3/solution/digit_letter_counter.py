"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the Letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""

from collections import OrderedDict 
# accepting input from user, expected input to be combionation of
#lettters and numbers.
user_input = input("Enter string : ")

# initialising the counter for letter and digit
dict1 = OrderedDict() 
dict1["Digits"] = 0
dict1["Letters"] = 0


# loop to access every element of string individually.
for character in user_input:    
    if character.isalpha():    # conditionto check for Letter.
        # if found increase counter variable by 1.
        dict1["Letters"] = dict1["Letters"] + 1 
    elif character.isdigit():      # conditiion to check for digit.
        # if found increase counter variable by 1.       
        dict1["Digits"] = dict1["Digits"] + 1 
            
for key, value in dict1.items() :
  print ( key, value )