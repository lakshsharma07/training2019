# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:34:22 2019

@author: Lakshay
"""
"""
Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.
"""


import sqlite3

from pandas import DataFrame
#os.chdir('/Users/sylvester/Desktop/Database and Python/Python/')
conn = sqlite3.connect ( 'student.db' )
c = conn.cursor()
c.execute ("""CREATE TABLE student(
          Student_name TEXT,
          Student_Age INTEGER,
          Student_roll_no INTEGER,
          Student_Branch TEXT
          )""")
c.execute("INSERT INTO student VALUES ('rahul',21,101,'CSE')")
c.execute("INSERT INTO student VALUES ('gaurav',22,102,'IT')")
c.execute("INSERT INTO student VALUES ('ravi',22,103,'IT')")
c.execute("INSERT INTO student VALUES ('harsh',20,104,'CSE')")
c.execute("INSERT INTO student VALUES ('krishna',21,105,'CSE')")
c.execute("SELECT * FROM STUDENT")
print ( c.fetchone())
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["id","first","last","pay"]

conn.commit()
conn.close()



import mysql.connector
conn = mysql.connector.connect(user='sharma1997lak', password='laksh_2727',host='db4free.net',database = 'student_data') 
from pandas import DataFrame

c = conn.cursor()

c.execute ("""CREATE TABLE student(
          Student_name TEXT,
          Student_Age INTEGER,
          Student_roll_no INTEGER,
          Student_Branch TEXT
          )""")
c.execute("INSERT INTO student VALUES ('rahul',21,101,'CSE')")
c.execute("INSERT INTO student VALUES ('gaurav',22,102,'IT')")
c.execute("INSERT INTO student VALUES ('ravi',22,103,'IT')")
c.execute("INSERT INTO student VALUES ('harsh',20,104,'CSE')")
c.execute("INSERT INTO student VALUES ('krishna',21,105,'CSE')")
c.execute("SELECT * FROM student")
print ( c.fetchone())

c.execute("SELECT * FROM student")
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["name","age","roll","branch"]

conn.commit()
conn.close()



import pymongo

client = pymongo.MongoClient("mongodb://sharma1997lak:lakshya%5F2727@cluster0-shard-00-00-na88p.mongodb.net:27017,cluster0-shard-00-01-na88p.mongodb.net:27017,cluster0-shard-00-02-na88p.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
db = client.student

def add_detail(name1,age1,roll1,branch1):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    db.student.insert_one(
            {
            "name" : name1,
            "age" : age1,
            "roll no" : roll1,
            "branch" : branch1
            })
    return "student added added successfully"
add_detail('rahul',21,101,'CSE')
add_detail('gaurav',22,102,'IT')
add_detail('ravi',22,103,'IT')
add_detail('harsh',20,104,'CSE')
add_detail('krishna',21,105,'CSE')
def fetch_all_employee():
    user = db.student.find()
    for i in user:
        print (i)
        
fetch_all_employee()






