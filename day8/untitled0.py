# -*- coding: utf-8 -*-
"""
Created on Wed May 15 19:56:43 2019

@author: Lakshay
"""

"""
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image


"""

from  selenium import webdriver

url = "http://forsk.in/images/Forsk_logo_bw.png"

browser = webdriver.Chrome("E:/training/day8/chromedriver.exe")

browser.get(url)
import urllib
# get the image source
img = browser.find_element_by_xpath('/html/body/img')
src = img.get_attribute('src')
urllib.request.urlretrieve(src,'Forsk_logo_bw.png')


from bs4 import BeautifulSoup as bs
soup=bs(browser,'lxml')
print(soup.head.title.text)
name=browser.find_element_by_xpath('/html/head/title').text




client = pymongo.MongoClient("mongodb://sharma1997lak:<password>@cluster0-shard-00-00-na88p.mongodb.net:27017,cluster0-shard-00-01-na88p.mongodb.net:27017,cluster0-shard-00-02-na88p.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
db = client.test






