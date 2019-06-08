# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 09:20:41 2019

@author: Lakshay
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat")

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?
"""
import pandas as pd
import numpy as np

data=pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",delimiter=' ')


data.isnull().any(axis=0)

features=data.iloc[:,:8].values
lables=data['lpsa'].values
lables.mean()
from sklearn.model_selection import train_test_split
features_train,features_test,lables_train,lables_test=train_test_split(features,lables,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
features_train=ss.fit_transform(features_train)
features_test=ss.transform(features_test)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(features_train,lables_train) 

prediction=lr.predict(features_test)

df=pd.DataFrame({"actual":lables_test,"prediction":prediction})

lr.score(features_test,lables_test)
lr.score(features_train,lables_train)

from sklearn import metrics
print ("Simple Regression Root Mean Square Error (MSE) for TEST data is") 
print (np.round (np.sqrt(metrics .mean_squared_error(lables_test,prediction)),2) )#0.73

#prediction using lasso
#import module
from sklearn.linear_model import Lasso
#creating object
lr_lasso=Lasso()
#fitting the model
lr_lasso.fit(features_train,lables_train) 

prediction_lasso=lr_lasso.predict(features_test)

df=pd.DataFrame({"actual":lables_test,"prediction":prediction_lasso})

lr_lasso.score(features_test,lables_test)
lr_lasso.score(features_train,lables_train)

from sklearn import metrics
print ("Lasso Regression Root Mean Square Error (MSE) for TEST data is") 
print (np.round (np.sqrt(metrics.mean_squared_error(lables_test, prediction_lasso)),2) )
#1.08

#prediction using Ridge
#import module
from sklearn.linear_model import Ridge
#creating object
lr_ridge=Ridge()
#fitting the model
lr_ridge.fit(features_train,lables_train) 

prediction_ridge=lr_ridge.predict(features_test)

df=pd.DataFrame({"actual":lables_test,"prediction":prediction_ridge})

lr_ridge.score(features_test,lables_test)
lr_ridge.score(features_train,lables_train)

from sklearn import metrics
print ("Ridge Regression Root Mean Square Error (MSE) for TEST data is") 
print (np.round (np.sqrt(metrics.mean_squared_error(lables_test, prediction_ridge)),2) )
#0.72


mean1=data['lpsa'].mean()
data['lpsa']=list(map(lambda x:'high' if (x > mean1) else 'low',data['lpsa']))

features=data.iloc[:,:8].values
lables=data['lpsa'].values

from sklearn.model_selection import train_test_split
features_train,features_test,lables_train,lables_test=train_test_split(features,lables,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
features_train=ss.fit_transform(features_train)
features_test=ss.transform(features_test)

from sklearn.linear_model import LogisticRegression
logClassifier = LogisticRegression(random_state=0)
logClassifier.fit(features_train, lables_train)

lables_pred=logClassifier.predict(features_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(lables_test, lables_pred)
