# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:12:28 2019

@author: Lakshay
"""

"""
Code Challenge - 
 This is a pre-crawled dataset, taken as subset of a bigger dataset 
 (more than 4.7 million job listings) that was created by extracting data 
 from Monster.com, a leading job board.
 
 
 
 Remove location from Organization column?
 Remove organization from Location column?
 
 In Location column, instead of city name, zip code is given, deal with it?
 
 Seperate the salary column on hourly and yearly basis and after modification
 salary should not be in range form , handle the ranges with their average
 
 Which organization has highest, lowest, and average salary?
 
 which Sector has how many jobs?
 Which organization has how many jobs
 Which Location has how many jobs?
"""

import pandas as pd
import numpy as np

data=pd.read_csv("monster_com-job_sample.csv")
df_copy.isnull().any(axis=0)

loc1=data['salary'].value_counts()
list1=loc1.index.tolist()

loc2=data['organization'].value_counts()
list2=loc2.index.tolist()

data['organization']=list(map(lambda x:np.nan if x in list1 else x,data['organization']))

data['new_loc']=np.nan
data['new_org']=np.nan
import re       
def change_org(i):
     if re.findall(r'^[a-zA-Z\s]+[,][\s][a-zA-Z]{2}[\s][\d]{5}?$|^[a-zA-Z\s]+[,][\s][a-zA-Z]{2}$|^[a-zA-Z]{2}$',str(i)):
         data.iloc[i,14]=data.iloc[i,9]
     else:
         data.iloc[i,15]=data.iloc[i,9]
         
data['organization'].apply(change_org)
def change_loc
     if re.findall(r'^[a-zA-Z\s]+[,][\s][a-zA-Z]{2}[\s][\d]{5}?$|^[a-zA-Z\s]+[,][\s][a-zA-Z]{2}$|^[a-zA-Z]{2}$',str(i)):
         data.iloc[i,14]=data.iloc[i,8]
     else:
         data.iloc[i,15]=data.iloc[i,8]
         

df_copy = data.dropna(subset=['salary'])     

def salary1(i):
    if re.findall(r'year',str(i)):
        str1=str(i).replace(',','')
        result=np.array(re.findall(r'[\d]+[\.]?[\d]+',str1),dtype=float)
        return result.mean()
    if re.findall(r'hour',str(i)):
        str1=str(i).replace(',','')
        result=np.array(re.findall(r'[\d]+[\.]?[\d]+',str1),dtype=float)
        return (result.mean()*(24*365))
    if re.findall(r'[\d]',str(i)):
        result=np.array(re.findall(r'[\d]+[\.]?[\d]+',i),dtype=float)
        return (result.mean())
    else:
        return np.nan
         
df_copy['salary']=df_copy['salary'].apply(salary1) 


    
