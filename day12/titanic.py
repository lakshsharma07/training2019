# -*- coding: utf-8 -*-
"""
Created on Tue May 21 10:49:34 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Titanic Analysis
  Filename: 
    titanic.py
  Dataset:
    training_titanic.csv
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
"""
import pandas as pd
df = pd.read_csv("training_titanic.csv")
list1 = (df['Survived'].value_counts().tolist())
print("people survived {} people died {}".format(list1[1],list1[0]))


list2=(df['Survived'].value_counts(normalize=True).tolist())
print("people survived perc {} people died perc {}".format(list2[1],list2[0]))

#df_1=df.groupby(['Survived','Sex'])
#df_1.groups


ms=df["Sex"][(df['Survived'] == 1) & (df['Sex'] == 'male')].value_counts()
md=df["Sex"][(df['Survived'] == 0) & (df['Sex'] == 'male')].value_counts()
print("male survived vs male died ={}:{}".format(ms[0],md[0]))
fs=df["Sex"][(df['Survived'] == 1) & (df['Sex'] == 'female')].value_counts()
fd=df["Sex"][(df['Survived'] == 0) & (df['Sex'] == 'female')].value_counts()
print("female survived vs female died ={}:{}".format(fs[0],fd[0]))

df['child']=df['Age'].map(lambda x: 0 if x >=18 else 1)
sr18l=df["child"][(df['Survived'] == 1) & (df['child'] == 1)].value_counts()
sr18m=df["child"][(df['Survived'] == 1) & (df['child'] == 0)].value_counts()




