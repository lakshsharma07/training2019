# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:06:22 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    URL shortening service Bitly
  Filename: 
    bitly.py
  Problem Statement:
    (usagov_bitly_data.json)
    In 2011, URL shortening service Bitly partnered with the US government website
    USA.gov to provide a feed of anonymous data gathered from users who shorten links
    ending with .gov or .mil. 
    In 2011, a live feed as well as hourly snapshots were available
    as downloadable text files. 
    This service is shut down at the time of this writing (2017),
    but we preserved one of the data files.
    In the case of the hourly snapshots, each line in each file contains a common form of
    web data known as JSON. (Use usagov_bitly_data.txt file from Resources)

    Replace the 'nan' values with 'Mising' and ' ' values with 'Unknown' keywords
    Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with and without Pandas
    Count the number of occurrence for each time-zone
    Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)
    From field 'a' which contains browser information and separate out browser capability(i.e. the first token in the string
    eg. Mozilla/5.0)
    Count the number of occurrence for separated browser capability field and plot bar graph for top 5 values (using Seaborn)
    Add a new Column as 'os' in the dataset, separate users by 'Windows' for the values in  browser information column 
    i.e. 'a' that contains "Windows" and "Not Windows" for those who don't

Hint:
    http://1usagov.measuredvoice.com/2011/
    
"""
"""
import json 
with open('usagov_bitly_data.json', 'r') as file:
     json_data = json.load(file)
     for item in json_data:
           if item['ParameterKey'] in ["Shell","Type"]:
              item['ParameterKey'] = "new value"
with open('/path/to/josn_file.json', 'w') as file:
    json.dump(json_data, file, indent=2)
"""
import json
import pandas as pd

tweets = []
for line in open('usagov_bitly_data.json', 'r'):
    tweets.append(json.loads(line))
df = pd.DataFrame(tweets)
df=df.fillna('Mising')
df=df.replace({'':'UnKnown'})

#Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with and without Pandas
df2=df["tz"].value_counts()
df2=df2.head(10)

from collections import Counter

dict_tz =Counter(df['tz'].tolist()).most_common(10)

#    Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)
df2.plot.bar()


#From field 'a' which contains browser information and separate out browser capability(i.e. the first token in the string eg. Mozilla/5.0)
x=df['a'].tolist()
y=[]
for i in x:
    pass
    y.append(i.split(' ')[0])
    
df_a=pd.DataFrame(y)
x=df_a[0].value_counts()




