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
import matplotlib.image as mtimg


"""
if use Image.open from pillow it's not Numpy array .
If you think you can't do image processing bcz of not Numpy array WRONG.
you can do Image processing using Pillow function
 """
# Pillow library
print("\nUsing Pillow \n ")
image = Image.open("images/cat.jpg") 
print(type(image))
image.show()
print("Format of Image ", image.format) # will print format of image like jpg, png, tiff etc

# Convert to Numpy
image1 = np.asanyarray(image)
print(type(image1))
plt.imshow(image1)
plt.colorbar() # will plot bar with image
# print(image1.format) # Error bcz of Numpy array
print("Shape", image1.shape)
print(image1) # will show float values
print("Minimum Value", image1.min())
print("Maximum Value", image1.max())

##########################
# Open image using Matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mtimg

print("\nUsing Matplotlib \n ")
image2 = mtimg.imread("images/dog.jpg")
print("Type ", type(image2))
print("Size of Image", image2.size) # (x, y, channels) = x * y * channels
plt.imshow(image2)
plt.colorbar() # will plot bar with image
print(image2) # will show float values
print("Minimum Value", image2.min())
print("Maximum Value", image2.max())

###########################

"""
# Scikit image
    Can use for:
    image segmentation
    J-Matrix transformation
    Color space manuplation
    Analysis
    Filtering
    Feature Extraction
    
"""
from skimage import io, img_as_float, img_as_ubyte, img_as_int
import matplotlib.pyplot as plt
import matplotlib.image as mtimg

print("\nUsing Scikit Image \n ")
image3 = io.imread("images/lion.jpg")
print("Type of Image",type(image3))
print("Size", image3.size) # (x, y, channels) = x * y *channels
print(image3)
plt.imshow(image3)
plt.colorbar() # will plot bar with image
print(image3) # will show float values
print("Minimum Value", image3.min())
print("Maximum Value", image3.max())

# Can use this too but values will be 0-255 it float number NOT float image conversion
# float_image4 = io.imread("images/lion.jpg").astype(float) 
float_image4 = img_as_float(image3) # convert to float in btw 0.0 - 1.0
print("Ater conversion")
plt.imshow(float_image4)
print(float_image4) # will show float values
print("Minimum Value", float_image4.min())
print("Maximum Value", float_image4.max())
