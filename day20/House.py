# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:08:27 2019

@author: Lakshay
"""

"""
Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score
"""
import pandas as pd

dataset=pd.read_csv("kc_house_data.csv")

dataset.isnull().any(axis=0)
dataset['sqft_above']=dataset['sqft_above'].fillna(dataset['sqft_above'].mean())

fe=dataset.drop(dataset.iloc[:,0:3],axis=1)
lb=dataset['price']

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(fe, lb, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

#Let's import the Lasso, Ridge, Elasticnet regression object and define model
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
lm = LinearRegression ()
lm_lasso = Lasso() 
lm_ridge =  Ridge() 
 

#Fit a model on the train data

lm.fit(features_train, labels_train)
lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)


import numpy as np
df=pd.DataFrame()
print ("RSquare Value for Simple Regresssion TEST data is-  "+str(np.round (lm.score(features_test,labels_test)*100,2))) 

print ("RSquare Value for Lasso Regresssion TEST data is- "+str(np.round (lm_lasso.score(features_test,labels_test)*100,2)))

print ("RSquare Value for Ridge Regresssion TEST data is- "+str(np.round (lm_ridge.score(features_test,labels_test)*100,2)))


predict_test_lm =	lm.predict(features_test ) 
predict_test_lasso = lm_lasso.predict (features_test) 
predict_test_ridge = lm_ridge.predict (features_test)


from sklearn import metrics
print ("Simple Regression Root Mean Square Error (MSE) for TEST data is") 
print (np.round (np.sqrt(metrics .mean_squared_error(labels_test, predict_test_lm)),2) )

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lasso),2))

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_ridge),2))

