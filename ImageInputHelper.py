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
tf.app.flags.DEFINE_string('trainImageLabelFile','./train.txt','the train data label file')
FLAGS = tf.app.flags.FLAGS
IMAGE_SIZE = 1211*891
NUM_CLASSES = 100
NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN = 500
NUM_EXAMPLES_PER_EPOCH_FOR_EVAL = 100

#遍历和获取图片信息的类
class ImageIterator:
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


#使用numpy读取一张图片
def readImage(imagePathsQueue):
	print(imagePathsQueue)
	if imagePathsQueue != None:
		return np.array(Image.open(imagePathsQueue))
	else:
		logger.info('文件%s不存在'.format(imagePathsQueue))
		return None


def getTrainInputs(dataDir,batchSize):
	imageIterator = ImageIterator(dataDir)
	imagePaths = imageIterator.imagePaths
	imageNames = imageIterator.imageNames

	imageLabelsDic = imageIterator.loadLables(FLAGS.trainImageLabelFile)

	imagePathsQueue = tf.train.string_input_producer(imagePaths)

	logger.info('图像数据读取完成')
	#数据增强
	logger.info('开始数据增强')

	with tf.name_scope('data_augmentation'):
		logger.info(imagePathsQueue)

		imageInput = readImage(imagePathsQueue)
		labelInput = imageLabelsDic[imagePathsQueue]
		convertImage = tf.cast(tf.convert_to_tensor(imageInput),tf.float32)
		convertLabel = tf.cast(tf.convert_to_tensor(labelInput),tf.int32)

		width,height = imageIterator.maxLenthHeight()

		minFractionOfExampleInQueue = 0.4
		minQueueExamples = int(2725*minFractionOfExampleInQueue)
		#发现
	return generateImageAndLabelBatch(convertImage,convertLabel,minQueueExamples,batchSize)

def generateImageAndLabelBatch(image,label,minQueueExamples,batchSize,shuffle):
	numPreprocessThreads = 16
	if shuffle:
		images,labelBatch = tf.train.shuffle_batch([image,label],batchSize = batchSize,num_threads=numPreprocessThreads,
			capaity = minQueueExamples + 3* batchSize,min_after_dequeue = minQueueExamples)
	else:
		images,labelBatch = tf.train.batch([image,label],batchSize = batchSize,num_threads=numPreprocessThreads,
			capaity = minQueueExamples + 3* batchSize,min_after_dequeue = minQueueExamples)
	tf.summary.image('images',images)
	return images,tf.reshape(labelBatch,[batchSize])