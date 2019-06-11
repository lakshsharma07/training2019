# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:11:17 2019

@author: Lakshay
"""

"""
Q1. 

(Click Here To Download Training data File): 
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_training_data.json

(Click Here To Download Test data File):
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_test_data.json


This is the data for local classified advertisements. It has 9 prominent sections: jobs, resumes, gigs, personals, housing, 
community, services, for-sale and discussion forums. Each of these sections is divided into subsections called categories. 
For example, the services section has the following categories under it:
beauty, automotive, computer, household, etc.

For a set of sixteen different cities (such as newyork, Mumbai, etc.), we provide to you data from four sections

        for-sale
        housing
        community
        services

and we have selected a total of 16 categories from the above sections.

        activities
        appliances
        artists
        automotive
        cell-phones
        childcare
        general
        household-services
        housing
        photography
        real-estate
        shared
        temporary
        therapeutic
        video-games
        wanted-housing

Each category belongs to only 1 section.

About Data:

        city (string) : The city for which this Craigslist post was made.
        section (string) : for-sale/housing/etc.
        heading (string) : The heading of the post.

each of the fields have no more than 1000 characters. The input for the program has all the fields but category which you have
 to predict as the answer.

A total of approximately 20,000 records have been provided to you, proportionally represented across these sections, 
categories and cities. The format of training data is the same as input format but with an additional field "category", 
the category in which the post was made.

Task:

    Given the city, section and heading of an advertisement, can you predict the category under which it was posted?
    Also Show top 5 categories which has highest number of posts
"""

import pandas as pd

with open ('Advertisement_training_data.json') as f:
    data=f.read()

data=data[data.find('{'):]
train_data=pd.read_json(data,lines=True)

with open ('test1.json',encoding='utf8') as f:
    data=f.read()

data=data[data.find('{'):]
test_data=pd.read_json(data,lines=True)




#test_data=pd.read_json('test.json',lines=True)

labels_train=train_data.iloc[:,0]
features_train=train_data.iloc[:,1:]
features_test=test_data

from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
list1=[0,2]
for i in list1:
    features_train.iloc[:,i]=lb.fit_transform(features_train.iloc[:,i])
    features_test.iloc[:,i]=lb.transform(features_test.iloc[:,i])
#labels_train=lb.fit_transform(labels_train)


import numpy as np
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
def nlp_data(column):
    review = re.sub('[^a-zA-Z]', ' ', column)
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    #lem = WordNetLemmatizer() #Another way of finding root word
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    return review

features_train['heading']=features_train['heading'].apply(nlp_data)
corpus = []    
features_test['heading']=features_test['heading'].apply(nlp_data)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
features1=cv.transform(corpus).toarray()

features_train=np.append(features_train.iloc[:,[0,2]],features,axis=1)
features_test=np.append(features_test.iloc[:,[0,2]],features1,axis=1)



#Training and making predictions
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 

test_data['category']=labels_pred


print(test_data['category'].value_counts().head(5))






