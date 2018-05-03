# -*- coding: utf-8 -*-
"""
Created on Wed May  2 21:26:19 2018

@author: 李海峰
"""


import tensorflow as tf
import numpy as np
from PIL import Image
import os
import pandas as pd

imageDir = "./train/"
file_name = "./tfrecord.record"
labelFile = "./train.txt"

#遍历和获取图片信息的类
class ImagesInfo:
	def __init__(self,dataDir):
		self.imagePaths = []
		self.imageNames = []

		for root,subFolder,fileList in os.walk(dataDir):
			for filePath in fileList:
				self.imagePaths += [os.path.join(root,filePath)]
				self.imageNames.append(filePath)

	def loadLables(self,filePath):
		self.labelTable = pd.read_table('train.txt',delim_whitespace=True,header=None)
		labelDic ={}
		for index,row in self.labelTable.iterrows():
			labelDic[row[0]] = row[1]
		return labelDic

	def maxLenthHeight(self):
		maxLen = 0
		maxHeight = 0
		for imagePath in self.imagePaths:
			image = Image.open(imagePath)
			if maxLen < image.size[0]:
				maxLen = image.size[0]
			if maxHeight < image.size[1]:
				maxHeight = image.size[1]
		return maxLen,maxHeight

imageInfo = ImagesInfo(imageDir)

#生成整数型的属性
def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


writer = tf.python_io.TFRecordWriter(file_name)

labelDic =imageInfo.loadLables(labelFile)

length,height = imageInfo.maxLenthHeight()

for root,subFolder,fileList in os.walk(imageDir):
    for filePath in fileList:
        print(os.path.join(root,filePath))
        imageRawData = tf.gfile.FastGFile(os.path.join(root,filePath),'rb').read()
        with tf.Session() as sess:
            imageData = tf.image.decode_jpeg(imageRawData)
            imageData = tf.image.convert_image_dtype(imageData,dtype=tf.int64)
            resized = tf.image.resize_images(imageData,[max(length,height),max(length,height)],method=0)
            print(resized.shape)
            label = labelDic[filePath]
            example = tf.train.Example(features=tf.train.Features(
                    feature={
                            'pixels':_bytes_feature((str(resized)).encode('utf-8')),
                            'label':_int64_feature(label),
                            'size':_int64_feature(max(length,height))
                            }))
            writer.write(example.SerializeToString())
writer.close