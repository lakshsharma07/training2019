# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:29:08 2019

@author: Lakshay
"""

"""
Challenge 1
    We are going to make a "Shopping List" app. 
    Run the script to start using it.
    Put new things into the list one at a time
    Enter the word DONE - in all CAPS - to QUIT the program
    And once i quit, I want the app to show me everything thats on my list.

Hint 1
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use the app

    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app with DONE

    Step 6: print out the list
"""
list1=[]
print('SHOPPING LIST')
print ("What should we pick up at the store ?")
print ("Enter 'DONE' to stop adding items.")
print('see what is currently in the list enter SHOW')
while True:
    user_input=input('>')
    if user_input == 'DONE':
        print("Here’s your list")
        for item in list1:
            print(item)
        break
    elif user_input == 'SHOW':
        for item in list1:
            print(item)
    elif user_input == 'HELP':
        print('Enter the word DONE - in all CAPS - to QUIT the program ')
        print('And once i quit, I want the app to show me everything thats on my list.')
        print('If I type SHOW, I should be able to see what is currently in the list')
    else:
        list1.append('-'+user_input)

