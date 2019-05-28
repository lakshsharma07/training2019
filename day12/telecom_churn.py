# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:42:29 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
        
To perfrom analysis on the Telecom industry churn dataset -

1. Predict the count of Churned customer availing both voice mail plan and international plan schema
2. Total charges for international calls made by churned and non-churned customer and visualize it
3. Predict the state having highest night call minutes for churned customer
4. Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
5. Which category of customer having maximum account lenght? Predict and print it
6. Predict a relation between the customer and customer care service that whether churned customer have shown their concern to inform the customer care service about their problem or not
7. In which area code the international plan is most availed?
    
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
df3=pd.read_csv('Telecom_churn.csv')

ms=df3['international plan'][(df3['voice mail plan'] == 'yes') & (df3['churn'] == True)].value_counts()['yes']

x=df3['total intl charge'].sum()
new_df = df3['total intl charge'][df3['churn'] == True]
new_df.hist(bins=10,grid=True)

dfinitial=df3[df3['churn'] == True]
dfinitial['state'][dfinitial["total night minutes"]==dfinitial['total night minutes'].max()]


vis3 =  plt.pie([df3['total day calls'], df3['total eve calls'],df3['total night calls'],df3['total intl calls']], explode=[0, 0,0,0], labels=['day','eve','night','intl'], autopct="%0f%%")
plt.axis('equal')
plt.show(vis3)


df_rank=df3.groupby(['area code'])
df_rank.groups

