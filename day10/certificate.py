# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:36:58 2019

@author: Lakshay
"""


"""
Code Challenge 1

Certificate Generator

Develop a Python code that can generate certificates in image format. 
It must take names and other required information from the user and generates 
certificate of participation in a Python Bootcamp conducted by Forsk.

Certificate should have Forsk Seal, Forsk Signature, Different Fonts
"""

from PIL import Image,ImageDraw,ImageFont
 
img = Image.new('RGB', (1024, 1024), color = (0,0,0))
d = ImageDraw.Draw(img)  
img.paste(img2, (10, 10))
fnt2 = ImageFont.truetype('arial.ttf', 45)
d.text((300,10),"FORSK TECHNOLOGIES ",font=fnt2, fill=(255,255,255))
d.text((300,60),"PYTHON BOOTCAMP 2019",font=fnt2, fill=(255,255,255))
fnt1 = ImageFont.truetype('arial.ttf', 25)
input1=input("name : ")
input2=input("college name : ")
input3=input("date : ")
d.text((10,300),"This is to certify that {} of {} college has attend his python Bootcamcanp\n\nconducted by Forsk Technologies on {} 2019".format(input1,input2,input3),font=fnt1, fill=(255,255,255))
img.save('pil_color.png')


#resize size of img
img2 = Image.open("Forsk_logo_bw.png")
width, height = img2.size 
img2= img2.resize((int(width/6), int(height/6))) 
img2.save("Forsk_logo_bw.png")


73, 109, 137

from PIL import Image
import sys
 
in_file = sys.argv[1]
 
img = Image.open(in_file)
print(img.size)
print(img.size[0])
print(img.size[1])
