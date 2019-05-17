# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:35:45 2019

@author: Lakshay
"""

"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplusgem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
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
    
    
import pandas as pd
from collections import OrderedDict

col_name = ["ID","ITEMS","ADDRESS","STARTING DATE","ENDING DATE","QUANTITY"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))
df = pd.DataFrame(col_data) 
df.to_csv("data/former.csv")

