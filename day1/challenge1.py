# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:57:57 2019

@author: Lakshay
"""

import random
computer_guess= random.randint(0,10)
print( 'guess the number ')
player_guess=int(input())
if(player_guess == computer_guess):
    print('player wins')
else:
    print('computer wins '+'and the number is ' + str(computer_guess))

