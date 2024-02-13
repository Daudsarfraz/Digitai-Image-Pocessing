#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:05:01 2024

@author: Dawood Sarfraz
"""

from skimage import io, img_as_ubyte, img_as_float

image1 = io.imread("images/cat.jpg")
print("Type of Image is ", type(image1))
print("Type of Image is ", image1.shape) # (x, y, channel)
image2 = img_as_float(image1)
print("Type of Image is ", type(image2))
print("Type of Image is ", image2.shape) # (x, y, channel)



image3 = io.imread("images/cat.jpg", as_gray=True) # 
print("Type of Image is ", type(image3))
print("Type of Image is ", image3.shape) # (x, y)
image4 = img_as_float(image3)
print("Type of Image is ", type(image2))
print("Type of Image is ", image2.shape) # (x, y, channel)