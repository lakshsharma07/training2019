# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:53:03 2019

@author: Lakshay
"""


"""
Code Challenge: Simple Linear Regression
  Name: 
    Food Truck Profit Prediction Tool
  Filename: 
    Foodtruck.py
  Dataset:
    Foodtruck.csv
  Problem Statement:
    Suppose you are the CEO of a restaurant franchise and are considering 
    different cities for opening a new outlet. 
    
    The chain already has food-trucks in various cities and you have data for profits 
    and populations from the cities. 
    
    You would like to use this data to help you select which city to expand to next.
    
    Perform Simple Linear regression to predict the profit based on the 
    population observed and visualize the result.
    
    Based on the above trained results, what will be your estimated profit, 
    
    If you set up your outlet in Jaipur? 
    (Current population in Jaipur is 3.073 million)
        
  Hint: 
    You will implement linear regression to predict the profits for a 
    food chain company.
    Foodtruck.csv contains the dataset for our linear regression problem. 
    The first column is the population of a city and the second column is the 
    profit of a food truck in that city. 
    A negative value for profit indicates a loss.
"""

import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv("Foodtruck.csv")

features=dataset.iloc[:,0].values
features=features.reshape(97,1)
labels=dataset.iloc[:,1].values

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels)
#plotting the result
plt.plot(features,regressor.predict(features))
print("Current population in Jaipur is 3.073 million so profit or loss will be"+str(regressor.predict(3.073)))


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)
regressor.fit(features_train,labels_train) 

output=regressor.predict(features_test) 

df=pd.DataFrame({'actual':labels_test,'result':output})
df

