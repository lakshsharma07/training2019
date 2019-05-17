# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:46:56 2019

@author: Lakshay
"""
# Create a new Code Challenge to POST data 

# Research the below wesbite and post some data on it

# https://requestbin.com
 
import json
with open("faculty.json", "r") as read_file:
    jsondata=json.load(read_file)


import json
import requests

Host = "https://en69j7ijwkqr4.x.pipedream.net"

data = {"firstname":"dev","language":"English"}

headers = {'{"name": "Darth Vader"}',"Content-Type: application/json"}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )