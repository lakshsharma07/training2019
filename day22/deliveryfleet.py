# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:47:08 2019

@author: Lakshay
"""

"""
Q1. (Create a program that fulfills the following specification.)
deliveryfleet.csv


Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature) and the mean percentage of time a driver was >5 mph 
over the speed limit (speeding_feature).

    Perform K-means clustering to distinguish urban drivers and rural drivers.
    Perform K-means clustering again to further distinguish speeding drivers from those who follow speed limits, in addition to the rural vs. urban division.
    Label accordingly for the 4 groups.
"""

import pandas as pd
import matplotlib.pyplot as plt

data =pd.read_csv("deliveryfleet.csv")


features=data.iloc[:,1:].values

from sklearn.preprocessing import StandardScaler
features = StandardScaler().fit_transform(features)

plt.scatter(features[:,0],features[:,1])

from sklearn.cluster import KMeans
#wcss score to find no of cluster
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)    

#Now plot it        
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()


kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)


# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'RURAL IN SPEED LIMIT')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'URBAN IN SPEED LIMIT')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'RURAL CROSS LIMIT')
plt.scatter(features[pred_cluster == 3, 0], features[pred_cluster == 3, 1], c = 'gray', label = 'URABAN CROSS LIMIT')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('Distance travelled')
plt.ylabel('Speed Limit')
plt.legend()
plt.show()