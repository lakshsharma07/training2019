# -*- coding: utf-8 -*-
"""
Created on Thu May 16 12:50:32 2019

@author: Lakshay
"""
"""
Code Challenge 3
In the Bid plus Code Challenege 

          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database mySQL Database
"""

from  selenium import webdriver

url = "https://bidplus.gem.gov.in/bidlists"

browser = webdriver.Chrome("E:/training/day8/chromedriver.exe")

browser.get(url)

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for i in range(1,10):
    id=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text
    A.append(id)
    item=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text
    B.append(item)
    address=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text
    C.append(address)
    date_start=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text
    D.append(date_start)
    date_end=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text
    E.append(date_end)
    quan=browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text
    F.append(quan)

import mysql.connector
conn = mysql.connector.connect(user='sharma1997lak', password='laksh_2727',host='db4free.net',database = 'student_data') 
from pandas import DataFrame

c = conn.cursor()

c.execute ("""CREATE TABLE bid(
          ID TEXT,
          ITEMS TEXT,
          ADDRESS TEXT,
          START_DATE TEXT,
          END_DATE TEXT,
          QUANTITY INTEGER
          )""")

for i in range(1,9):
    c.execute("INSERT INTO bid VALUES ('"+A[i]+"','"+B[i]+"','"+C[i]+"','"+D[i]+"','"+E[i]+"','"+F[i]+"')")
c.execute("SELECT * FROM bid")
print ( c.fetchone())

c.execute("SELECT * FROM bid")
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["ID","ITEMS","ADDRESS","START_DATE","END_DATE","QUANTITY"]

conn.commit()
conn.close()





import sqlite3
conn = sqlite3.connect ( 'bid.db' )
c = conn.cursor() 
#c.execute("DROP TABLE bid")
c.execute ("""CREATE TABLE bid(
          ID TEXT,
          ITEMS TEXT,
          ADDRESS TEXT,
          START_DATE TEXT,
          END_DATE TEXT,
          QUANTITY INTEGER
          )""")

for i in range(1,len(A)):
    c.execute("INSERT INTO bid VALUES ('"+A[i]+"','"+B[i]+"','"+C[i]+"','"+D[i]+"','"+E[i]+"','"+F[i]+"')")
c.execute("SELECT * FROM bid")
print ( c.fetchone())

c.execute("SELECT * FROM bid")
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["ID","ITEMS","ADDRESS","START_DATE","END_DATE","QUANTITY"]  
    
conn.commit()
conn.close()
