# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:39:31 2019

@author: Lakshay
"""
"""
Code Challenge 4
GIF Creator

A program that puts together multiple images (PNGs, JPGs, TIFFs) to make a smooth 
GIF that can be exported. Make the program convert small video files to GIFs as 
well.
"""
import imageio
filenames=["pil_color1.png","pil_color2.png","pil_color3.png","pil_color0.png","pil_color4.png"]
with imageio.get_writer('E:/training/day10/movie.gif', mode='I', duration=0.4) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
    writer.close()