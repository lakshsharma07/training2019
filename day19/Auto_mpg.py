# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:19:24 2019

@author: Lakshay
"""

"""

Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" respectively
    Display the Car Name with highest miles per gallon value
    Build the Decision Tree and Random Forest models and find out which of the two is more accurate in predicting the MPG value
    Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)
[6,215,100,2630,22.2,80,3]

"""

import pandas as pd
"""
file1=[]
with open("Auto_mpg.txt") as file:
    for i in file:
        data=i.split()
        file1.append(data)
data=pd.DataFrame(file1)
data=data.drop([11,12,13],axis=1)
data=data.merge([8,9,10])
"""

data=pd.read_table("Auto_mpg.txt",delim_whitespace=True)
data.columns=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]

data['car name'][data['mpg']==data['mpg'].max()]
data=data.iloc[:,0:8]

data['horsepower']=data['horsepower'].replace('?',data['horsepower'].mode()[0])
features=data.iloc[:,1:].values
labels=data.iloc[:,0].values

 
"""
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
labels=le.fit_transform(labels) 
"""
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)
#Training and making predictions
from sklearn.tree import DecisionTreeRegressor  
classifier = DecisionTreeRegressor()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 

df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
df 

classifier.score(features_train, labels_train)
classifier.score(features_test, labels_test)
classifier.score(features_test, labels_pred)

import numpy as np
x=[6,215,100,2630,22.2,80,3]
x=np.array(x)
x=x.reshape(1,-1)
x= sc.transform(x)

labels_pred = classifier.predict(x) 


#using randomtree
from sklearn.ensemble import RandomForestRegressor

reg = RandomForestRegressor(n_estimators=20, random_state=0)  
reg.fit(features_train, labels_train)  
labels_pred = reg.predict(features_test)

reg.score(features_train, labels_train)
reg.score(features_test, labels_test)
labels_pred = reg.predict(x)
#Evaluate the algo


 

