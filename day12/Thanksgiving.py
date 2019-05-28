# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:52:32 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Thanks giving Analysis
  Filename: 
    Thanksgiving.py
  Problem Statement:
    Read the thanksgiving-2015-poll-data.csv file and 
    perform the following task :

    Discover regional and income-based patterns in what Americans eat for 
    Thanksgiving dinner

    Convert the column name to single word names
    
    Using the apply method to Gender column to convert Male & Female
    Using the apply method to clean up income
    (Range to a average number, X and up to X, Prefer not to answer to NaN)
    
    compare income between people who tend to eat homemade cranberry sauce for
    Thanksgiving vs people who eat canned cranberry sauce?
    
    find the average income for people who served each type of cranberry sauce
    for Thanksgiving (Canned, Homemade, None, etc).
    
    Plotting the results of aggregation
    
    Do people in Suburban areas eat more Tofurkey than people in Rural areas?
    Where do people go to Black Friday sales most often?
    Is there a correlation between praying on Thanksgiving and income?
    What income groups are most likely to have homemade cranberry sauce?

    Verify a pattern:
        People who have Turducken and Homemade cranberry sauce seem to have 
        high household incomes.
        People who eat Canned cranberry sauce tend to have lower incomes, 
        but those who also have Roast Beef have the lowest incomes
        
    Find the number of people who live in each area type (Rural, Suburban, etc)
    who eat different kinds of main dishes for Thanksgiving:
        
  Hint:

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file=pd.read_csv("thanksgiving.csv",encoding='latin-1')
dict1={}
column_names=file.columns.tolist()
for index,step in enumerate(column_names):
    dict1['{}'.format(index)]=( "{} ". format (step))
# Convert the column name to single word names    
file.columns=dict1.keys()

#Using the apply method to Gender column to convert Male & Female
file[file["62"].isnull()]
def gender_code(gender_string):  
    if (gender_string == "Male") :
        return 0
    elif (gender_string == "Female"):
        return 1   
    
file["62"] = file["62"].apply(gender_code)
file["63"].value_counts(dropna=False)

#Using the apply method to clean up income
income_range="$25,000 to $49,999"
def income_cleaner(income_range):  
    if (income_range == "Prefer not to answer"):
        return np.nan
    elif (income_range == "NaN"):
        pass
    else :
        income_range=np.array(((income_range.replace("$","")).replace(",","")).split(" "))
        for i in income_range:
            if i.isnumeric :
                print("numeric")
            else:
                print("text")


x=file[(file['60']=="Suburban") & (file["2"]=="Tofurkey")]
y=file[(file["60"]=="Rural") & (file["2"]=="Tofurkey")]
x=file["57"].value_counts
plt.bar(file["57"])



