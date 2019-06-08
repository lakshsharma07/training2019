# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:29:40 2019

@author: Lakshay
"""
"""
Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.

"""
# Importing the libraries
import pandas as pd
from apyori import apriori

# Data Preprocessing
dataset = pd.read_csv('BreadBasket_DMS.csv')

import matplotlib.pyplot as plt
value=dataset['Item'].value_counts().head(15)
plt.pie(value,labels=value.index)

list1=[]
list2=[]

count=1
dataset = dataset[dataset['Item']!='NONE'] 
for i in range(0,20507):
    if dataset.iloc[i,2]==count:
        list1.append(str(dataset.iloc[i,3]))
    else:
        list2.append(list1)
        count=dataset.iloc[i,2]
        list1=[]
        list1.append(dataset.iloc[i,3])
        
rules = apriori(list2, min_support =0.0025, min_confidence = 0.2, min_lift = 3)
results = list(rules)




for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
    