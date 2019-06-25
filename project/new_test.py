import pandas as pd
import numpy as np
df=pd.read_csv("train.csv")
df2=pd.read_csv("test.csv")
features=df.iloc[:,[1,2,8,12,13,19]]
labels=df.iloc[:,0]

#************************************888
#************************************************************************
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)


from sklearn.preprocessing import FunctionTransformer
sc=FunctionTransformer(np.log1p, validate=True)
features_train=sc.fit_transform(features_train)
features_test=sc.transform(features_test)

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression( random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)  

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = features_test, y = labels_test, cv = 10)
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())


import pickle

with open("pick_pickle","wb") as fp:
    pickle.dump(classifier,fp)
    
with open("pick_pickle1","wb") as fp:
    pickle.dump(sc,fp)
    