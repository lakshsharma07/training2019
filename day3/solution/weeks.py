"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""

given_tuple = ('Monday', 'Wednesday', 'Thursday', 'Saturday')

new_tuple = (given_tuple[0],) + ('Tuesday',) + given_tuple[1:3] + ('Friday',) + (given_tuple[-1],) + ('Sunday',)

print (new_tuple)