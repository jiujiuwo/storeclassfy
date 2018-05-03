# -*- coding: utf-8 -*-
"""
Created on Thu May  3 09:56:40 2018

@author: 李海峰
"""

import tensorflow as tf

reader = tf.TFRecordReader()

fileNameQueue = tf.train.string_input_producer(["./tfrecord.record"])

_,serializedExample = reader.read(fileNameQueue)

features = tf.parse_single_example(
        serializedExample,
        features={
                'pixels': tf.FixedLenFeature([],tf.string),
                'label':tf.FixedLenFeature([],tf.int64),
                'size':tf.FixedLenFeature([],tf.int64)})

image = tf.decode_raw(features['pixels'],tf.int64)
label = tf.cast(features['label'],tf.int64)
size = tf.cast(features['size'],tf.int64)

sess = tf.Session()

coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess,coord=coord)

for i in range(10):
    image,label,size = sess.run([image,label,size])
    print 
