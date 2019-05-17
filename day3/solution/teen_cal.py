"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""

def fix_teen(number):
    teen_list = [13,14,17,18,19]
    if number in teen_list:
        return 0
    else:
        return number
def no_teen_sum ( dictionary ):
    list_of_numbers = dictionary.values()
    Sum = 0
    for number in list_of_numbers:
        Sum += fix_teen ( number )
    return Sum


user_input = input("Enter the dictionary input")

splitted_string = user_input.split(',')


splitted_string[0] = splitted_string[0][1:]
splitted_string[len(splitted_string)-1] =splitted_string[len(splitted_string)-1][0:-1] 

dictionary = {}
for i in splitted_string:
    i = i.split(':')
    i[0] = i[0].replace('"','')
    i[1] = int(i[1])
    dictionary[i[0]] = i[1]

print("Sum = " + str(no_teen_sum ( dictionary )))

