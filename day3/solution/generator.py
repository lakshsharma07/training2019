"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""

# Enter comma separated numbers
user_list = input("Enter comma seperated numbers :").split(",")
new_list = []

for i in user_list:
    new_list.append(int(i))
    
# list to tuple conversion
user_tuple = tuple(user_list)

print ("List : "+str(user_list))
print ("Tuple : "+str(user_tuple))