# -*- coding: utf-8 -*-
"""
Created on Thu May 30 18:23:24 2019

@author: Lakshay
"""

"""

Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
    [10,4,0,1,0]
    Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.
    [10,4,1,0,1]
"""
import pandas as pd

data=pd.read_csv("PastHires.csv")

features=data.drop('Hired',axis=1).values
values=data['Hired'].values

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
values=le.fit_transform(values)
list1=[1,3,4,5]
for i in list1:
    features[:,i]=le.fit_transform(features[:,i])
 
from sklearn.model_selection import train_test_split

features_train, features_test, values_train, values_test = train_test_split(features, values, test_size=0.2, random_state=0) 

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)

from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, values_train)

values_pred = classifier.predict(features_test) 

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(values_test, values_pred)) 


#Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:
features=data.drop(['Employed?','Hired'],axis=1).values
values=data['Employed?'].values

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
values=le.fit_transform(values)
list1=[2,3,4]
for i in list1:
    features[:,i]=le.fit_transform(features[:,i])


from sklearn.ensemble import RandomForestClassifier
regressor = RandomForestClassifier(n_estimators=10, random_state=0)  
regressor.fit(features, values)  

pred1=[[10,4,0,1,0]]
values_pred = regressor.predict(pred1)

pred2=[[10,4,1,0,1]]
values_pred2 = regressor.predict(pred2)


 