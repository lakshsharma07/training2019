# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:20:53 2019

@author: Lakshay
"""

"""
Q3.Code Challenge -
Data: "data.csv"

This data is provided by The Metropolitan Museum of Art Open Access
1. Visualize the various countries from where the artworks are coming.
2. Visualize the top 2 classification for the artworks
3. Visualize the artist interested in the artworks
4. Visualize the top 2 culture for the artworks
"""

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("data.csv")


list1=data['Country'].value_counts().head()

y=list(list1.index)
patches, texts=plt.pie(list1.values,labels=list1.index,autopct='%1.1f%%',shadow=True, startangle=90)
plt.legend(patches, y, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()



list1=data['Classification'].value_counts().head(2)
plt.bar(list1.index,list1)


list1=data['Artist Display Name'].value_counts()
plt.bar(list1.index,list1)

list1=data['Culture'].value_counts().head(2)
plt.bar(list1.index,list1)



















import matplotlib.pyplot as plt

labels = ['Cookies', 'Jellybean', 'Milkshake', 'Cheesecake']
sizes = [38.4, 40.6, 20.7, 10.3]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
patches, texts = plt.pie(sizes, colors=colors, shadow=True,labeldistance=2.9, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()
