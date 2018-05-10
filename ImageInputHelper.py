#-*-encoding = utf-8 -*-
import tensorflow as tf
import os
import random
import time
import logging
import numpy as np 
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from PIL import Image

#设置日志
logger = logging.getLogger('data helper')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)

#设置一些全局常量
tf.app.flags.DEFINE_string('labelFilePath','./train.txt','the train data label file')
tf.app.flags.DEFINE_string('imageDataDir','./train/','the train image file')



tf.app.flags.DEFINE_string('testLabelFilePath','./test.txt','the test data label file')
tf.app.flags.DEFINE_string('testImageDataDir','./test/','the train image file')

tf.app.flags.DEFINE_integer('batchSize',64,'batchSize')

tf.app.flags.DEFINE_integer('epochToTrain',2000,'epochToTrain')

TRAIN_NUM_EPOCHS = 100
FLAGS = tf.app.flags.FLAGS
NUM_CLASSES = 100
NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN = 2724
NUM_EXAMPLES_PER_EPOCH_FOR_TEST = 1000

IMAGE_RESIZE_SIZE = 100

#遍历和获取图片信息的类
class ImageIterator:
	def __init__(self,dataDir,labelFilePath):
		self.imagePaths = []
		self.imageNames = []

		for root,subFolder,fileList in os.walk(dataDir):
			for filePath in fileList:
				self.imagePaths += [os.path.join(root,filePath)]
				self.imageNames.append(filePath)
		self.labelDic = self.loadLablesDic(labelFilePath)
		self.labels = self.getLabels()
		self.length,self.height = self.maxLenthHeight()

	def loadLablesDic(self,labelFilePath):
		self.labelTable = pd.read_table(labelFilePath,delim_whitespace=True,header=None)
		labelDic ={}
		for index,row in self.labelTable.iterrows():
			try:
				labelDic[row[0]] = row[1]
			except KeyError:
				labelDic[row[0]] = 0
		self.labelDic = labelDic
		return labelDic

	def getLabels(self):
		labels = []
		#print(self.labelDic)
		for i in range (len(self.imageNames)):
			try:
				label = int(self.labelDic[self.imageNames[i]])-1
				if label >=0:
					labels.append(label)
				else:
					labels.append(0)
					print('label error:%s'%self.imageNames[i])
			except KeyError:
				print(self.imageNames[i])
		return labels

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


#使用numpy读取一张图片
def readImage(inputQueue,length,height):
	#print(inputQueue)
	size = IMAGE_RESIZE_SIZE
	print('image size afer resize: %d'%size)
	if inputQueue != None:
		images = tf.read_file(inputQueue[0])
		#plt.show(inputQueue[0])
		images = tf.image.convert_image_dtype(tf.image.decode_png(images, channels=3), tf.float32)
		resized = tf.image.resize_images(images,[size,size],method=0)
		#resized = resized / 255
		resized.set_shape([size,size,3])
		return resized
	else:
		logger.info('文件%s不存在'.format(inputQueue))
		return None


def getTrainInputs(dataDir=FLAGS.imageDataDir,batchSize=FLAGS.batchSize,labelFilePath = FLAGS.labelFilePath):
	imageIterator = ImageIterator(dataDir,labelFilePath)
	imagePaths = imageIterator.imagePaths
	#print('input queue shunxu:')
	#print(imagePaths[0],imagePaths[-1])
	#print(imageIterator.labels[0],imageIterator.labels[-1])

	NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN = len(imagePaths)

	imagesTensor = tf.convert_to_tensor(imagePaths,dtype=tf.string)
	labelsTensor = tf.convert_to_tensor(imageIterator.labels,dtype=tf.int64)

	#print('labelTensorShape',labelsTensor.shape)
	print('imagesTensor:%s'%imagesTensor)
	print('labelsTensor:%s'%labelsTensor)
	inputQueue = tf.train.slice_input_producer([imagesTensor,labelsTensor],num_epochs=FLAGS.epochToTrain)
	print('inputQueue:%s'%inputQueue)

	images = readImage(inputQueue,imageIterator.length,imageIterator.height)
	#数据增强
	labels = inputQueue[1]
	#print('labels:',labels)

	#logger.info('开始数据增强')

	with tf.name_scope('data_augmentation'):
		logger.info(inputQueue)

		width,height = imageIterator.maxLenthHeight()

		minFractionOfExampleInQueue = 0.4
		minQueueExamples = int(NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN*minFractionOfExampleInQueue)
		#发现
		print ('Filling queue with %d images before starting to train. '
			'This will take a few minutes.' % minQueueExamples)
	return generateImageAndLabelBatch(images,labels,minQueueExamples,batchSize,shuffle=False)


def getTestInputs(dataDir=FLAGS.testImageDataDir,batchSize=FLAGS.batchSize,labelFilePath = FLAGS.testLabelFilePath):
	imageIterator = ImageIterator(dataDir,labelFilePath)
	imagePaths = imageIterator.imagePaths

	imagesTensor = tf.convert_to_tensor(imagePaths,dtype=tf.string)
	labelsTensor = tf.convert_to_tensor(imageIterator.labels,dtype=tf.float32)

#	NUM_EXAMPLES_PER_EPOCH_FOR_TEST = len(imagePaths)
	#print('imagesTensor:%s'%imagesTensor)
	#print('labelsTensor:%s'%labelsTensor)
	inputQueue = tf.train.slice_input_producer([imagesTensor,labelsTensor],num_epochs=2)
	#print('inputQueue:%s'%inputQueue)

	images = readImage(inputQueue,imageIterator.length,imageIterator.height)
	#数据增强
	labels = inputQueue[1]
	#print('labels:',labels)

	width,height = imageIterator.maxLenthHeight()

	minFractionOfExampleInQueue = 0.4
	minQueueExamples = int(NUM_EXAMPLES_PER_EPOCH_FOR_TEST*minFractionOfExampleInQueue)
		#发现
	print ('Filling queue with %d images before starting to test. '
			'This will take a few minutes.' % minQueueExamples)
	print(images,labels)
	return generateImageAndLabelBatch(images,labels,minQueueExamples,batchSize,shuffle=False)


def generateImageAndLabelBatch(image,label,minQueueExamples,batchSize,shuffle):
	numPreprocessThreads = 1
	if shuffle:
		images,labelBatch = tf.train.shuffle_batch([image,label],batchSize = batchSize,num_threads=numPreprocessThreads,
			capacity = minQueueExamples + 3* batchSize,min_after_dequeue = minQueueExamples)
	else:
		images,labelBatch = tf.train.batch([image,label],batch_size = batchSize,num_threads=numPreprocessThreads,
			capacity = minQueueExamples + 3* batchSize)
	tf.summary.image('images',images)
	labelBatch = tf.reshape(labelBatch,[batchSize])
	return images,labelBatch

