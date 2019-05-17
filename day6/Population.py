# -*- coding: utf-8 -*-
"""
Created on Mon May 13 23:24:53 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Population Counting
  Filename: 
    Population.py
  Problem Statement:
      
      The given input has a number of rows, each with four fields from a table, containing:

          Rank,City,Population,State or union territory
          1,Mumbai,"12,442,373",Maharashtra


    You are required to output:

        Country, State, Population of the state (obtained by summing up the population of each city in that state)  


    Sample Input

    1,Mumbai,"12,442,373",Maharashtra
    9,Pune,"3,124,458",Maharashtra
    13,Nagpur,"2,405,665",Maharashtra
    6,Chennai,"4,646,732",Tamil Nadu
    59,Salem,"831,038",Tamil Nadu


    Sample Output

    {"key":"India,Tamil Nadu","value":5477770}
    {"key":"India,Maharashtra","value":17972496}


    Explanation

    The population of India,Tamil Nadu is obtained by adding the population of 
    Chennai and Salem. 
    This process is repeated for India,Maharashtra and India,Maharashtra. 


    Refer to population.csv


"""
import csv
list1=[]
with open('population.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")
    next(csv_reader)
    dict1={}
    for x in csv_reader:
        x[2]=x[2].replace(',','')
    #    z=dict(map(lambda y:dict1[y[3]] = (dict1[y[3]]+y[2]) if y[3] in dict1 else (dict1[y[3]]=y[2]),x))
        if ('India,'+x[3] in dict1):
            dict1['India,'+x[3]] = (dict1['India,'+x[3]])+int(x[2])
        else:
            dict1['India,'+x[3]]=int(x[2])
          
          
        
        
        
        
        
        
        
        