# -*- coding: utf-8 -*-
"""
Created on Sat May 25 22:22:56 2019

@author: Lakshay
"""

"""
Code Challenge 

import Automobile.csv file.

Using MatPlotLib create a PIE Chart of top 10 car makers according to the number 
of their cars and explode the largest car maker


"""
import pandas as pd
import matplotlib.pyplot as plt
automobile=pd.read_csv("Automobile.csv")

top=automobile['make'].value_counts().head(10)

explode = (0.5,0,0,0,0,0,0,0,0,0)

plt.pie(top.values, explode = explode, labels=top.index, autopct='%2.2f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
