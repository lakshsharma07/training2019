# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:49:55 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    SSA Analysis
  Filename: 
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available 
    data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip from Resources)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     
"""

import os
import pandas as pd

file_name=os.listdir('baby_names')
df=pd.DataFrame()

list1=[]
year=1879
os.chdir("E:/training/day13/baby_names")
for file1 in file_name[0:131]:
    year+=1
    with open(file1,'r') as fp:
        df2="dataframe"+str(year)
        df2=pd.DataFrame(fp.readlines(),columns=[year])
    list1.append(df2)
df= pd.concat(list1,axis=1)
        
        
df2=df[2010]
list1=[]
for i in df2:
    list1.append(str(i).split(','))
df3=pd.DataFrame(list1,columns=['Name','sex','birth'])

df3[df3['sex']=='F'].head()
df3[df3['sex']=='M'].head()

        