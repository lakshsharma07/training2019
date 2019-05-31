# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:46:04 2019

@author: Lakshay
"""
"""
Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.
"""

import pandas as pd
import matplotlib.pyplot as plt

dataset1=pd.read_csv("iq_size.csv")

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

features =dataset1.iloc[:,1:].values
labels=dataset1.iloc[:,0].values

regressor.fit(features,labels)
regressor.predict([[90,70,150]])

import statsmodels.api as sm
features = sm.add_constant(features)

features_opt = features[:, [0, 1, 2,3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [ 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

features_opt = features[:, [ 1]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
regressor_OLS.pvalues

x=list(regressor_OLS.pvalues)
list1=[0,1,2,3]
while (max(x)>0.05):
    features_opt = features[:, list1]
    regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
    x=list(regressor_OLS.pvalues)
    if (max(x)>0.05):
        list1.pop(x.index(max(x)))
print (list1)
        
        
        
        
    

