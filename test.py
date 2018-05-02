# -*- coding: utf-8 -*-
"""
Created on Wed May  2 10:49:48 2018

@author: 李海峰
"""
from PIL import Image

imagePaths = []
imageNames = []
for root,subFolder,fileList in os.walk('train'):
    for filePath in fileList:  
        imagePaths += [os.path.join(root,filePath)]
        imageNames.append(filePath)

maxLength = 0
maxHeight = 0
for imagePath in imagePaths:
    image = Image.open(imagePath)
    if maxLength < image.size[0]:
        maxLength = image.size[0]
    if maxHeight < image.size[1]:
        maxHeight = image.size[1]
print(maxLength,maxHeight)
import numpy as np

a = np.array(image)

labelTable = pd.read_table('train.txt',delim_whitespace=True,header=None)