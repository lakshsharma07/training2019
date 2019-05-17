# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:40:51 2019

@author: Lakshay
"""

"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number  Book Title  Author Quantity  Price per Item
    34587 Learning Python, Mark Lutz  4 40.95
    98762 Programming Python, Mark Lutz 5 56.80
    77226 Head First Python, Paul Barry 3 32.95
    88112 Einführung in Python3, Bernd Klein  3 24.99    
    
    Write a Python program, You need to write a solution without using lambda,map,list comprehension first and then with lambda,map,reduce
    
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.

  Hint: 
    Write a Python program using lambda and map.

"""
"""
book_shop=[[34587 ,'Learning Python', 'Mark Lutz' , 4 ,40.95],[98762 ,'Programming Python', 'Mark Lutz', 5 ,56.80],[77226 ,'Head First Python', 'Paul Barry' ,3 ,32.95],[88112 ,'Einführung in Python3',' Bernd Klein' , 3 ,24.99]]
entry=['Order Number' , 'Book Title ', 'Author' ,'Quantity' , 'Price per Item']
c=[]
for i in book_shop:
    c.append(dict(zip(entry,i)))
order_summary=[]
for i in c:
    order_summary.append(list(zip(i['order number'],(i['quantity']*i['price per items'])))
    i['order number']
    
""" 
    
    
book_shop=[[34587 ,'Learning Python', 'Mark Lutz' , 4 ,40.95],[98762 ,'Programming Python', 'Mark Lutz', 5 ,56.80],[77226 ,'Head First Python', 'Paul Barry' ,3 ,32.95],[88112 ,'Einführung in Python3',' Bernd Klein' , 3 ,24.99]]    
list1=[]   
for i in book_shop:
    list1.append([i[0],(i[3]*i[4])])

for i in list1:
    if(i[1]<100):
        i[1]=i[1]+10
    else:
        continue
    
x=list(map(lambda i:([i[0],i[1]+10]) if (i[1]<100) else ([i[0],i[1]]),(list(map(lambda x:([x[0],(x[3]*x[4])]),book_shop)))))
    