# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:14:42 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""
import json
import requests
url1="http://free.currencyconverterapi.com/api/v5/convert"
url2="?q=USD_INR"
url3="&apiKey=d2b3bd20200eef73c9a7"
url=(url1+url2+url3)
print(url)
response = requests.get(url)
jsondata1 = response.json()