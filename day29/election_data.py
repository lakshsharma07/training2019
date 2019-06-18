# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 12:47:50 2019

@author: Lakshay
"""
"""

Q2. Code Challenge
code challenge - election data

1. Fetch the top parties of each state within each constituency with their vote %.

2. Visualize the top parties vote % in each constituency for Rajasthan.

3. Visualize the total seats gained by each party in each states.

4. Visualize the total seats won by the parties in the whole country
"""
import pandas as pd

data=pd.read_csv("election.csv")
data.columns

#1. Fetch the top parties of each state within each constituency with their vote %
df=data.groupby(['State','Constituency'])[['Party','Total Votes','%']]
df.size()
x=df.count()
dict1={} 
for i in df:
   dict1[i[0]]=i[1][i[1]['%'] == i[1]['%'].max()]


#2. Visualize the top parties vote % in each constituency for Rajasthan.   
df=data[data['State']=='Rajasthan']

df1=df.groupby(['Constituency'])
dict2={} 
list1=[]
for i in df1:
   list1.append(i[1]['%'].max())
   dict2[i[0]]=i[1][i[1]['%'] == i[1]['%'].max()]
   
list2=list(dict2.keys())  
import matplotlib.pyplot as plt

plt.bar(list2,list1)
plt.xticks(list2,list2,Rotation=90)

#3. Visualize the total seats gained by each party in each states.
data_set=data.sort_values('%').drop_duplicates(['State','Constituency'],keep='last')
df1=data_set.groupby(['State'])

for i in df1:
    print(i[0])
    list1=i[1]['Party'].value_counts()
    plt.bar(list1.index,list1)
    plt.xticks(list1.index,list1.index,Rotation=90)   
   
#4. Visualize the total seats won by the parties in the whole country
"""
import numpy as np
df1=data.groupby(['State'])
for i in df1:
    list1=[]
    print(i[0])
    df2=i[1].groupby(['Constituency'])
    for j in df2:
        list1.append(j[1]['Party'][j[1]['%'] == j[1]['%'].max()])
    party_list=np.array(list1)
    party_list=party_list.iloc[:,0].value_counts()
    plt.bar(party_list.index,party_list)
    plt.xticks(party_list.index,party_list.index,Rotation=90)
dict1={} 
for i in df1:
   dict1[i[0]]=i[1]['Total Votes'].sum()
   
"""