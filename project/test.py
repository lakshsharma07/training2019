# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:58:11 2019

@author: Lakshay
"""

import pandas as pd

data=pd.read_csv("train.csv")

features=data.iloc[:,1:].values
labels=data.iloc[:,0:1].values

#train test split the data
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.25,random_state=0)


#features scalling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)


model_accuracy=[]
# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

#k-fold cross validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = features_train, y = labels_train, cv = 10)
model_accuracy.append(accuracies.mean())
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())




# Fitting KNN to the Training set
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

#k-fold cross validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = features_train, y = labels_train, cv = 10)
model_accuracy.append(accuracies.mean())
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())




#Training using DecisionTree and making predictions
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 


from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  

#k-fold cross validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = features_train, y = labels_train, cv = 10)
model_accuracy.append(accuracies.mean())
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())




#train the model using RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=20, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)

from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))  

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = features_train, y = labels_train, cv = 10)
model_accuracy.append(accuracies.mean())
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())





# Fitting Kernel SVM to the Training set
# kernels: linear, poly and rbf
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
#score = classifier.score(features_test,labels_test)
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = features_train, y = labels_train, cv = 10)
model_accuracy.append(accuracies.mean())
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())




#Train The model using NaiveBayes and getting Prediction
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
gnb = BernoulliNB()
gnb.fit(features_train,labels_train)
labels_pred = gnb.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_gnb = confusion_matrix(labels_test, labels_pred)

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = gnb, X = features_train, y = labels_train, cv = 10)
model_accuracy.append(accuracies.mean())
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())

import matplotlib.pyplot as plt
list2=['LR','KNN','DT',"RF",'SVM','NB']
plt.bar(list2,model_accuracy)
plt.xlabel('Different Models')
plt.ylabel('Accuracy')
plt.title('Accuracy of Different Model without scaling')
plt.grid(True)
plt.savefig('fig1.png')




from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
model = ExtraTreesClassifier()
model.fit(features_train,labels_train)
print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
#plot graph of feature importances for better visualization
feat_importances = pd.Series(model.feature_importances_, index=features_train.columns)
feat_importances.nlargest(10).plot(kind='barh')
plt.xlabel('Fatures')
plt.ylabel('features_importance')
plt.title(' feature_importances without scaling')
#plt.grid(True)
plt.savefig('fig5.png')
plt.show()