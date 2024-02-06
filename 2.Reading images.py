#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:51:31 2024

@author: Dawood Sarfraz
"""
"""
Libraries:
    1: Pillow
    2: Scikit image
    4: OpenCV
    4: Matplotlib
    
"""
 # !pip install pillow # if not imstalled before
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open("images/cat.jpg")
# if use Image.open from pillow it's not Numpy array .If you think you can't do image processing bcz of not Numpy array WRONG. you can do Image processing using Pillow function
print(type(image))
image.show()
print("Formate of Image ", image.format) # will print format of image like jpg, png, tiff etc

# Convert to Numpy
image1 = np.asanyarray(image)
print(type(image1))
plt.imshow(image1)
print(image1.format)