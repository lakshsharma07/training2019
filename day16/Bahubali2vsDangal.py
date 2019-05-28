# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:40:13 2019

@author: Lakshay
"""

"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""

import pandas as pd

dataset=pd.read_csv("Bahubali2_vs_Dangal.csv")

#Second Approach - Create one model with two labels
feature=dataset.iloc[:,0].values
feature=feature.reshape(9,1)
labels=dataset.iloc[:,1:].values

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(feature, labels) 

print(regressor.intercept_)  
print (regressor.coef_)

print (regressor.predict(10))

#First Approach - Create two models, one for Bahubali and another for Dangal
feature=dataset.iloc[:,0].values
feature=feature.reshape(9,1)
labels=dataset.iloc[:,1:2].values

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(feature, labels) 
print ("Bahubali 10 day collection"+str(regressor.predict(10)))

feature=dataset.iloc[:,0].values
feature=feature.reshape(9,1)
labels=dataset.iloc[:,2].values

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(feature, labels) 

print ("Dangal 10 day collection"+str(regressor.predict(10)))

#using training and testing

from sklearn.model_selection import train_test_split  
feature_train, feature_test, labels_train, labels_test = train_test_split(feature, labels, test_size=0.2, random_state=0)  
regressor.fit(feature_train, labels_train)

print(regressor.predict(feature_test))

import matplotlib.pyplot as plt

plt.plot(feature,labels)

