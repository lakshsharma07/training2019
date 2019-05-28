# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:58:12 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""
import numpy as np
import pandas as pd
df1=pd.read_csv("Automobile.csv")

df1['price'] = df1['price'].fillna(df1['price'].mean())

x=np.array(df1['price'])

df1['price'].min()
df1['price'].max()
df1['price'].mean()
df1['price'].std()