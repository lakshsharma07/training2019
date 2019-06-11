# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:15:33 2019

@author: Lakshay
"""

"""
Q1. Human Activity Recognition

Human Activity Recognition with Smartphones

(Recordings of 30 study participants performing activities of daily living)

(Click Here To Download Dataset): https://github.com/K-Vaid/Python-Codes/blob/master/Human_activity_recog.zip



In an experiment with a group of 30 volunteers within an age bracket of 19 to 48 years, each person performed six activities
 (WALKING, WALKING UPSTAIRS, WALKING DOWNSTAIRS, SITTING, STANDING, LAYING) wearing a smartphone (Samsung Galaxy S II) on the 
 waist. The experiments have been video-recorded to label the data manually.

The obtained dataset has been randomly partitioned into two sets, where 70% of the volunteers was selected for generating the
 training data and 30% the test data.

 

Attribute information 

For each record in the dataset the following is provided:

        Triaxial acceleration from the accelerometer (total acceleration) and the estimated body acceleration. 
        Triaxial Angular velocity from the gyroscope.
        A 561-feature vector with time and frequency domain variables.
        Its activity labels.
        An identifier of the subject who carried out the experiment.

Train a tree classifier to predict the labels from the test data set using the following approaches:

  (a) a decision tree approach,

  (b) a random forest approach and

  (c) a logistic regression.

  (d) KNN approach

Examine the result by reporting the accuracy rates of all approach on both the testing and training data set. Compare the results.
 Which approach would you recommend and why?

        Perform feature selection and repeat the previous step. Does your accuracy improve?
        Plot two graph showing accuracy bar score of all the approaches taken with and without feature selection.
        
"""
import pandas as pd

test_data=pd.read_csv("test.csv")

train_data=pd.read_csv("train.csv")

features_train=train_data.iloc[:,0:562].values
labels_train=train_data.iloc[:,-1].values


features_test=test_data.iloc[:,0:562].values
labels_test=test_data.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
labels_train=lb.fit_transform(labels_train)
labels_test=lb.fit_transform(labels_test)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)



accuracy_list1=[]
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
accuracy_list1.append(accuracy_score(labels_test, labels_pred))




#Training and making predictions
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 


from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  


from sklearn.metrics import accuracy_score
print(accuracy_score(labels_train, labels_train))
accuracy_list1.append(accuracy_score(labels_test, labels_pred))





#train the model
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  

from sklearn.metrics import accuracy_score
print(accuracy_score(labels_train, labels_train))
accuracy_list1.append(accuracy_score(labels_test, labels_pred))





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
accuracy_list1.append(accuracy_score(labels_test, labels_pred))




import statsmodels.api as sm
features_train= sm.add_constant(features_train)

features_opt = features_train[:, 0:]
regressor_OLS = sm.OLS(endog = labels_train, exog = features_opt).fit()
regressor_OLS.summary()


x=list(regressor_OLS.pvalues)
list1=[]
for i in range (0,563):
    list1.append(i)
while (max(x)>0.05):
    features_opt = features_train[:, list1]
    regressor_OLS = sm.OLS(endog = labels_train, exog = features_opt).fit()
    x=list(regressor_OLS.pvalues)
    if (max(x)>0.05):
        list1.pop(x.index(max(x)))
print (list1)



accuracy_list2=[]
# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(features_opt, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test[:,list1])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

from sklearn.metrics import accuracy_score
print(accuracy_score(labels_train, labels_train))
accuracy_list2.append(accuracy_score(labels_test, labels_pred))




#Training and making predictions
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_opt, labels_train)

labels_pred = classifier.predict(features_test[:,list1]) 


from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  


from sklearn.metrics import accuracy_score
print(accuracy_score(labels_train, labels_train))
accuracy_list2.append(accuracy_score(labels_test, labels_pred))





#train the model
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(features_opt, labels_train)  
labels_pred = classifier.predict(features_test[:,list1])

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  

from sklearn.metrics import accuracy_score
print(accuracy_score(labels_train, labels_train))
accuracy_list2.append(accuracy_score(labels_test, labels_pred))





# Fitting Logistic Regression to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_opt, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test[:,list1])

# Predicting the class labels
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

from sklearn.metrics import accuracy_score
print(accuracy_score(labels_train, labels_train))
accuracy_list2.append(accuracy_score(labels_test, labels_pred))







import matplotlib.pyplot as plt
list2=['Logistic','DecisionTree',"RandomForest",'KNeighbors']
plt.bar(accuracy_list1,list1)
plt.title("before reduction")

plt.bar(accuracy_list1,list1)
plt.title("after reduction")





