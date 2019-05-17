# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:01:07 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""
import csv
def print_file():
    file1=open('zoo.csv')
    read=file1.readlines()
    print(read)
def animal_list():
    dict1={}   
    with open("zoo.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            if row[0] in dict1:
                dict1[row[0]]=dict1[row[0]]+1
            else:
                dict1[row[0]]=1
def water_animal():
    dict2={}   
    with open("zoo.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            if row[0] in dict2:
                dict2[row[0]]=dict2[row[0]]+int(dict2[row[0]])
            else:
                dict2[row[0]]=int(row[2]) 
def total_water():
    sum=0
    with open("zoo.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            sum=sum+int(row[2])
        print(sum)
