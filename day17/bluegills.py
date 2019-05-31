# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:42:18 2019

@author: Lakshay
"""
"""
Q. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota. The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced by taking into account a quadratic function of the age of the fish.
"""
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv("bluegills.csv")

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

features=dataset.iloc[:,0].values
features=features.reshape(78,1)
labels=dataset.iloc[:,-1].values

plt.scatter(features,labels)
#train the model
regressor.fit(features,labels)
#plot the prediction
plt.scatter(features,labels)
plt.plot(features,regressor.predict(features))


 #polynomial equation
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree =2 )
features_poly = poly_object.fit_transform(features)
regressor1=LinearRegression()
regressor1.fit(features_poly,labels)

regressor1.predict(poly_object.fit_transform(5))

plt.scatter(features, labels, color = 'red')
plt.plot(features, regressor1.predict(poly_object.fit_transform(features)), color = 'blue')


#using train and test method
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree =2 )
features_poly = poly_object.fit_transform(features_train)
regressor1=LinearRegression()
regressor1.fit(features_poly,labels_train)
regressor1.predict(poly_object.fit_transform(features_train))

regressor1.predict(poly_object.fit_transform(5))
print (regressor1.score(poly_object.fit_transform(features_test), labels_test))



