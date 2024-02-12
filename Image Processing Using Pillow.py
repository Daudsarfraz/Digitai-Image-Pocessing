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

# Here i'm resizing Orignai Image Not Numpy array converted Image

"""
Image.resize resizes to the dimensions you define width and Height
"""
large_image = image.resize((1500, 1500))
large_image.save("images/large_cat.jpg")
print("Size of Image", large_image.size)
large_image.show()

"""
# In thumbnail you can do without resize without assigning to a new variable
Image.thumbnail resizes to the largest size that 
    1. preserves the aspect ratio
    2. Does not exceed dimensions of the original image
    3. Does not exceed the size specified in the arguments of thumbnail
"""

image.thumbnail((350, 450))  # Large size
image.save("images/large_thumbnail_cat.jpg")
print("Large size of Image used Thumbnail", image.size)
image.show()


image.thumbnail((35, 50))  # Small Size
image.save("images/small_thumbnail_cat.jpg")
print("Small size of Image used Thumbnail", image.size)
image.show()


# Now i'm using using Numpy array Converted Image2

"""
Image.resize resizes to the dimensions you define width and Height
"""
image3 = Image.fromarray(image2) # Converting Numpy Arrat to back into Image
print("Type of Image after Back to Image", image3)
large_image3 = image3.resize((1500, 1500))
large_image3.save("images/large_image2_cat.jpg") # 
print("Size of Image", large_image3.size)
large_image3.show()

"""
# In thumbnail you can do without resize without assigning to a new variable
Image.thumbnail resizes to the largest size that 
    1. preserves the aspect ratio
    2. Does not exceed dimensions of the original image
    3. Does not exceed the size specified in the arguments of thumbnail
"""

image3.thumbnail((350, 450))  # Large size
image3.save("images/thumbnail_large_cat.jpg")
print("Large size of Image used Thumbnail", image3.size)
image3.show()


image3.thumbnail((35, 50))  # Small Size
image3.save("images/thumbnail_small_cat.jpg")
print("Small size of Image used Thumbnail", image3.size)
image3.show()


moon = Image.open("images/earth.jpg")