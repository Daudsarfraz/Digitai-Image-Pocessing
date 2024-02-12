#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:13:16 2024

@author: Dawood Sarfraz
"""
"""
 Here i'm exploring some image processing Functions
     1. Resize
     2. Thumbnail
"""
from PIL import Image
import numpy as np

print("\nUsing Pillow \n ")
image = Image.open("images/cat.jpg") 
print(type(image)) # In pillow image is NOT an array but can convert
image.show()
print("Type of Image", type(image))
print("Mode of Image", image.mode)
print("Format of Image ", image.format) # will print format of image like jpg, png, tiff etc
print("Size of Image", image.size)
width, height = image.size
print("Width of Image", width)
print("Height of Image", height)


# After converting into Numpy array
image2 = np.array(image)
print("Type of Image1", type(image2))
print("Size of Image", image2.shape)
width, height, channels = image2.shape
print("Width of Image", width)
print("Height of Image", height)
print("Channels of Image", height)
print(image2)

# Here i'm resizing Image
large_image = image.resize((1500, 1500))
large_image.save("images/large_cat.jpg")
print("Size of Image", large_image.size)
large_image.show()

image.thumbnail((350, 350)) # In thumbnail you can do without resize without assigning to a new variable
image.save("images/thumbnail_cat.jpg")
print("Size of Image used Thumbnail", image.size)
image.show()
