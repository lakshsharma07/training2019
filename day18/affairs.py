# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:53:34 2019

@author: Lakshay
"""
"""
Q1. (Create a program that fulfills the following specification.)
affairs.csv


Import the affairs.csv file.

It was derived from a survey of women in 1974 by Redbook magazine, in which married women were asked about their participation in extramarital affairs.

Description of Variables

The dataset contains 6366 observations of 10 variables:(modified and cleaned)

rate_marriage: woman's rating of her marriage (1 = very poor, 5 = very good)

age: women's age

yrs_married: number of years married

children: number of children

religious: women's rating of how religious she is (1 = not religious, 4 = strongly religious)

educ: level of education (9 = grade school, 12 = high school, 14 = some college, 16 = college graduate, 17 = some graduate school, 20 = advanced degree)

occupation: women's occupation (1 = student, 2 = farming/semi-skilled/unskilled, 3 = "white collar", 4 = teacher/nurse/writer/technician/skilled, 5 = managerial/business, 6 = professional with advanced degree)

occupation_husb: husband's occupation (same coding as above)

affair: outcome 0/1, where 1 means a woman had at least 1 affair.

    Now, perform Classification using logistic regression and check your model accuracy using confusion matrix and also through .score() function.

NOTE: Perform OneHotEncoding for occupation and occupation_husb, since they should be treated as categorical variables. Careful from dummy variable trap for both!!

    What percentage of total women actually had an affair?

(note that Increases in marriage rating and religiousness correspond to a decrease in the likelihood of having an affair.)

    Predict the probability of an affair for a random woman not present in the dataset. She's a 25-year-old teacher who graduated college, has been married for 3 years, has 1 child, rates herself as strongly religious, rates her marriage as fair, and her husband is a farmer.
[3,25,3,1,4,16,4,2]
Optional

    Build an optimum model, observe all the coefficients.


--------------------------
"""
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv("affairs.csv")

features=dataset.iloc[:,:8].values
labels=dataset.iloc[:,-1].values

#changing to one hot encoder and remove retundancy
from sklearn.preprocessing import OneHotEncoder
obj_onehotencoder1=OneHotEncoder(categorical_features = [6])
features = obj_onehotencoder1.fit_transform(features).toarray()
features = features[:, 1:]


obj_onehotencoder2=OneHotEncoder(categorical_features = [11])
features = obj_onehotencoder2.fit_transform(features).toarray()
features = features[:, 1:]




#train the model
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state =0)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)


# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

#checking for score
Score = classifier.score(features_train, labels_train)
Score = classifier.score(features_test, labels_test)

#What percentage of total women actually had an affair?
per=float(dataset['affair'].sum())/6366*100


#prediction for women [3,25,3,1,4,16,4,2]
import numpy as np
x = [3,25,3,1,4,16,4,2]
x = np.array(x)

ohe = obj_onehotencoder1.transform(x.reshape(-1,8)).toarray()
ohe=ohe[:,1:]
ohe = obj_onehotencoder2.transform(ohe).toarray()
ohe= ohe[:,1:]
classifier.predict(ohe)


#optimize the model
import statsmodels.api as sm
features = sm.add_constant(features)

features_opt = features[:, 0:]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()



x=list(regressor_OLS.pvalues)
list1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
while (max(x)>0.05):
    features_opt = features[:, list1]
    regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
    x=list(regressor_OLS.pvalues)
    if (max(x)>0.05):
        list1.pop(x.index(max(x)))
        x.pop(x.index(max(x)))
        
print (list1)















