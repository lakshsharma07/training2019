# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 12:46:04 2019

@author: Lakshay
"""

"""
Q2. Code Challenge

#Online Marketing

(Click Here To Download Resource File) : http://openedx.forsk.in/c4x/Manipal_University/FL007/asset/online_marketing.sql

Objective of this case study is to explore Online Lead Conversion for a Life Insurance company. Some people are interested 
in buying insurance products from this company hence they visit the site of this Life Insurance Company and fill out a survey
 asking about attributes like income, age etc. These people are then followed and some of them become customers from leads. 
 Company have all the past data of who became customers from lead. Idea is to learn something from this data and when

some new lead comes, assign a propensity of him/her converting to a customer based on attributes asked in the survey. 
This sort of problem is called as Predictive Modelling

Concept:

Predictive modelling is being used by companies and individuals all over the world to extract value from historical data. 
These are the mathematical algorithms, which are used to "learn" the patterns hidden on all this data. 
The term supervised learning or classification is also used which means you have past cases tagged or classified 
(Converted to Customer or Not) and you want to use this learning on new data. (machine learning)

Here are the attributes of the survey:

Attribute

age (Age of the Lead)

Job (Job Category e.g. Management)

marital (Marital Status)

education (Education of Lead)

smoker (Is Lead smoker or not (Binary – Yes / No))

monthlyincome (Monthly Income)

houseowner (Is home owner or not (Binary – Yes / No))

loan (Is having loan or not (Binary – Yes / No))

contact (Contact type e.g. Cellphone)

mod (Days elapsed since survey was filled)

monthlyhouseholdincome (Monthly Income of all family member)

target_buy (altogether Is converted to customer or not (Binary –Yes /No). This is known as Target or Responseand this is 
what we are modelling.)



Activities you need to perform:


a. Handle the missing data and perform necessary data pre-processing.
b. Summarise the data.
c. Perform feature selection and train using prediction model.
d. For a new lead, predict if it will convert to a successful lead or not.
e. Use different classification techniques and compare accuracy score and also plot them in a bar graph.
"""
import pandas as pd
import mysql.connector
conn = mysql.connector.connect(user='sharma1997lak', password='laksh_2727',host='db4free.net',database = 'student_data') 

c = conn.cursor()

data=pd.read_sql("SELECT * FROM online_marketing",conn)
data.info()

features=data.iloc[:,0:-1]
labels=data.iloc[:,-1]

from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
labels=lb.fit_transform(labels)

list1=[1,2,3,4,6,7,8]
for i in list1:
    lb=LabelEncoder()
    features.iloc[:,i]=lb.fit_transform(features.iloc[:,i])

import statsmodels.api as sm
features= sm.add_constant(features)

features_opt = features.iloc[:,0:]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()


x=list(regressor_OLS.pvalues)
list1=[]
for i in range (0,12):
    list1.append(i)
while (max(x)>0.05):
    features_opt = features.iloc[:, list1]
    regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
    x=list(regressor_OLS.pvalues)
    if (max(x)>0.05):
        list1.pop(x.index(max(x)))
print (list1)


from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features_opt,labels,test_size=.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features = sc.fit_transform(features_train)
features_test = sc.transform(features_test)



list1=[]
# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

from sklearn.metrics import accuracy_score
print(accuracy_score(labels_train, labels_train))
list1.append(accuracy_score(labels_test, labels_pred))




#Training and making predictions
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 


from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  


from sklearn.metrics import accuracy_score
print(accuracy_score(labels_train, labels_train))
list1.append(accuracy_score(labels_test, labels_pred))





#train the model
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  

from sklearn.metrics import accuracy_score
print(accuracy_score(labels_train, labels_train))
list1.append(accuracy_score(labels_test, labels_pred))





# Fitting Logistic Regression to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

from sklearn.metrics import accuracy_score
print(accuracy_score(labels_train, labels_train))
list1.append(accuracy_score(labels_test, labels_pred))




import matplotlib.pyplot as plt
list2=['Logistic','DecisionTree',"RandomForest",'KNeighbors']

plt.bar(list2,list1)
plt.title("accuracy")