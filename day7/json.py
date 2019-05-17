# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:56:36 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""
import requests
city=input()
url1="http://api.openweathermap.org/data/2.5/weather"
url2="?q="+city
url3="e9185b28e9969fb7a300801eb026de9c"
url=(url1+url2+url3)

response = requests.get(url)
# requests.get(url,params={"q":"Jaipur", "appid"="e9185b28e9969fb7a300801eb026de9c"})
jsondata = response.json()
jsondata['coord']
jsondata['weather']
jsondata['wind']
jsondata['sys']
# Content in binary form
print (type(response.content))