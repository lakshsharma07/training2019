# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:51:08 2019

@author: Lakshay
"""

str1 = "ETRFDRSGR"
i=int(str1.index('R'))
print(str1[:i+1]+(str1[i+1:].replace('R','#')))
   

