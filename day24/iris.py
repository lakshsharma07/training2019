# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:00:27 2019

@author: Lakshay
"""

"""
Q2. (Create a program that fulfills the following specification.)

The iris data set consists of 50 samples from each of three species of Iris flower (Iris setosa, Iris virginica and Iris versicolor).



    Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres (iris.data).
    Import the iris dataset already in sklearn module using the following command:\


from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data
Reduce dimension from 4-d to 2-d and perform clustering to distinguish the 3 species.

"""
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.datasets import load_iris
iris = load_iris()

iris1=pd.DataFrame(iris['data'],columns=iris['feature_names'])
iris1['labels']=iris['target']

features=iris1.iloc[:,0:4]
labels=iris1.iloc[:,4]

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(features)
explained_variance = pca.explained_variance_ratio_

plt.scatter(features[:,0], features[:,1])
plt.show()


from sklearn.cluster import KMeans
# Fitting K-Means to the dataset

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



kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)



# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Iris setosa')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Iris virginica')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Iris versicolor')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of flowers')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()