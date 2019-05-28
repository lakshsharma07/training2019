# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:49:22 2019

@author: Lakshay
"""

"""
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area


Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from collections import OrderedDict
import matplotlib.pyplot as plt


#extract data
wiki='https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area'
data=requests.get(wiki).text

link=bs(data,'lxml')

A=[]
B=[]
table1=link.find('table',class_='wikitable sortable')
for row in table1.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 7:
        A.append(cells[1].text.strip())
        B.append(cells[4].text.strip())
        
#store in dataframe
col_name = ["State/Territory","National Share (%)"]
col_data = OrderedDict(zip(col_name,[A,B]))
df = pd.DataFrame(col_data) 


df1=df.head(6)

#plot pie chart
plt.pie(df1['National Share (%)'], explode = (0.5,0,0,0,0,0), labels=df1['State/Territory'], autopct='%2.2f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
