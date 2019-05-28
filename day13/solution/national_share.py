"""
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area


Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""


# scraping and pie chart

import requests as re
from bs4 import BeautifulSoup 
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
data = re.get(url).text

soup = BeautifulSoup(data, "lxml")


all_table= soup.find_all('table')

right_table= soup.find('table', class_= 'wikitable')


A = []
B = []

for row in right_table.findAll('tr'):
    cells = row.findAll('td')

    if len(cells) == 7:
        A.append(cells[1].text.strip())
        B.append(cells[4].text.strip())

labels = (A[0],A[1],A[2],A[3],A[4],A[5])
sizes = B[0:6]
explode = [0.1,0,0,0,0,0]
colors = ['blue', 'orange','gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig('National_share.jpg')

