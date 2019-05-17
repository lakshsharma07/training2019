# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:54:04 2019

@author: Lakshay
"""
"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi
"""
import requests
import sqlite3
from pandas import DataFrame
from bs4 import BeautifulSoup as bs


wiki="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
data=requests.get(wiki)

soup=bs(data,'lxml')

right_table=soup.find('table', class_='table')
#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]

for row in right_table.findAll('tr'):
    cells = row.findAll('td')

    if len(cells) == 5:
        #A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())


#os.chdir('/Users/sylvester/Desktop/Database and Python/Python/')
conn = sqlite3.connect ( 'IccRanking.db' )
c = conn.cursor()
#c.execute("DROP TABLE ICC ")
c.execute ("""CREATE TABLE ICC(
          Team_name TEXT,
          Match_Played INTEGER,
          Points INTEGER,
          Raiting INTEGER
          )""")

for i in range(0,len(B)):
    c.execute("INSERT INTO ICC VALUES ('{}','{}','{}','{}')".format(B[i],C[i],D[i],E[i]))

c.execute("SELECT * FROM ICC")
print ( c.fetchone())
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["Team Name","Match Played","Points","Raiting"]

conn.commit()
conn.close()
