import os
import re
import sys

from six.moves import urllib
import tensorflow as tf

import ImageInputHelper

FLAGS = tf.app.flags.FLAGS

# Basic model parameters.
tf.app.flags.DEFINE_integer('batch_size', 128,
                            """Number of images to process in a batch.""")
tf.app.flags.DEFINE_string('data_dir', './train/',
                           """Path to the image directory.""")

# Global constants describing the CIFAR-10 data set.
NUM_CLASSES = ImageInputHelper.NUM_CLASSES
NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN = ImageInputHelper.NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN
NUM_EXAMPLES_PER_EPOCH_FOR_TEST = ImageInputHelper.NUM_EXAMPLES_PER_EPOCH_FOR_TEST


# Constants describing the training process.
MOVING_AVERAGE_DECAY = 0.9999     # The decay to use for the moving average.移动均值的指数衰减，用于参数更新
NUM_EPOCHS_PER_DECAY = 350.0      # Epochs after which learning rate decays.学习率衰减的epoch
LEARNING_RATE_DECAY_FACTOR = 0.1  # Learning rate decay factor.学习率衰减率
INITIAL_LEARNING_RATE = 0.1  # Initial learning rate.初始学习率

# If a model is trained with multiple GPUs, prefix all Op names with tower_name
# to differentiate the operations. Note that this prefix is removed from the
# names of the summaries when visualizing a model.
# 如果模型使用多个GPU进行训练，则使用tower_name将所有Op名称加前缀以区分操作。
# 请注意，在可视化模型时，将从摘要名称中删除此前缀。
TOWER_NAME = 'tower'

# 为参数添加tensorboard显示
def _activation_summary(x):
  """Helper to create summaries for activations.
  为激活创建摘要的助手

  Creates a summary that provides a histogram of activations.
  Creates a summary that measures the sparsity of activations.
  创建一个提供激活直方图的摘要。
  创建一个衡量激活稀疏性的摘要。
  Args:
    x: Tensor
  Returns:
    nothing
  """
  # Remove 'tower_[0-9]/' from the name in case this is a multi-GPU training
  # session. This helps the clarity of presentation on tensorboard.
  tensor_name = re.sub('%s_[0-9]*/' % TOWER_NAME, '', x.op.name)
  tf.summary.histogram(tensor_name + '/activations', x)
  tf.summary.scalar(tensor_name + '/sparsity',
                                       tf.nn.zero_fraction(x))
  '''
 tf.nn.zero_fraction(
    value,
    name=None
)
返回value中零的分数。这在summary中用于衡量和报告稀疏性很有用。 
  '''


def _variable_on_cpu(name, shape, initializer):
  """Helper to create a Variable stored on CPU memory.
  在CPU存储中创建变量的助手

  Args:
    name: name of the variable
    shape: list of ints
    initializer: initializer for Variable

  Returns:
    Variable Tensor
  """
  with tf.device('/cpu:0'):
    var = tf.get_variable(name, shape, initializer=initializer, dtype=tf.float32)
  return var


def _variable_with_weight_decay(name, shape, stddev, wd):
  """Helper to create an initialized Variable with weight decay.
  创建一个权重衰减的初始化变量的助手
  Note that the Variable is initialized with a truncated normal distribution.
  A weight decay is added only if one is specified.
  请注意，变量是用截断的正态分布初始化的。 只有在指定了权重衰减时才会添加权重衰减。
  Args:
    name: name of the variable
    shape: list of ints
    stddev: standard deviation of a truncated Gaussian
    wd: add L2Loss weight decay multiplied by this float. If None, weight
        decay is not added for this Variable.

  Returns:
    Variable Tensor
  """
  var = _variable_on_cpu(
      name,
      shape,
      tf.truncated_normal_initializer(stddev=stddev, dtype=tf.float32))
  if wd is not None:
    weight_decay = tf.multiply(tf.nn.l2_loss(var), wd, name='weight_loss')
    tf.add_to_collection('losses', weight_decay)
  return var
  '''
  tf.add_to_collection(
    name,
    value
  )
  name: The key for the collection. For example, the GraphKeys class contains many standard names for collections.
  value: The value to add to the collection.
  '''


def getTrainInputs():
  """Construct distorted input for CIFAR training using the Reader ops.
  使用Reader ops构建CIFAR10训练的失真输入，用于训练

  Returns:
    images: Images. 4D tensor of [batch_size, IMAGE_SIZE, IMAGE_SIZE, 3] size.
    labels: Labels. 1D tensor of [batch_size] size.

  Raises:
    ValueError: If no data_dir
  """
  if not FLAGS.data_dir:
    raise ValueError('Please supply a data_dir')
  images, labels = ImageInputHelper.getTrainInputs(dataDir=FLAGS.data_dir,
                                                  batchSize=FLAGS.batch_size)
  return images, labels

def getTestInputs():

  if not FLAGS.data_dir:
    raise ValueError('Please supply a data_dir')
  images, labels = ImageInputHelper.getTestInputs()
  return images, labels

# 构建模型，输入是distorted_inputs()或者inputs()的返回值
# 增加对提供的图像执行推断（即分类）的操作。
def inference(images):
  """Build the CIFAR-10 model.
     创建 CIFAR-10模型

  Args:
    images: Images returned from distorted_inputs() or inputs().

  Returns:
    Logits.返回logits
  """
  # We instantiate all variables using tf.get_variable() instead of
  # tf.Variable() in order to share variables across multiple GPU training runs.
  # If we only ran this model on a single GPU, we could simplify this function
  # by replacing all instances of tf.get_variable() with tf.Variable().
  # 我们使用tf.get_variable（）而不是tf.Variable（）来实例化所有变量，以便跨多个
  # GPU训练运行共享变量。 如果我们只在单个GPU上运行此模型，我们可以通过用tf.Variable（）
  # 替换tf.get_variable（）的所有实例来简化此功能。

  # conv1 第一层卷积
  with tf.variable_scope('conv1') as scope:
    kernel = _variable_with_weight_decay('weights',
                                         shape=[5, 5, 3, 64],
                                         stddev=5e-2,
                                         wd=None)
    conv = tf.nn.conv2d(images, kernel, [1, 1, 1, 1], padding='SAME')
    biases = _variable_on_cpu('biases', [64], tf.constant_initializer(0.0))
    pre_activation = tf.nn.bias_add(conv, biases)
    conv1 = tf.nn.relu(pre_activation, name=scope.name)
    _activation_summary(conv1)

  # pool1 第一层池化
  pool1 = tf.nn.max_pool(conv1, ksize=[1, 3, 3, 1], strides=[1, 2, 2, 1],
                         padding='SAME', name='pool1')
  # norm1  第一层正则化
  #norm1 = tf.nn.lrn(pool1, 4, bias=1.0, alpha=0.001 / 9.0, beta=0.75,
                    #name='norm1')

  # conv2  第二层卷积
  with tf.variable_scope('conv2') as scope:
    kernel = _variable_with_weight_decay('weights',
                                         shape=[5, 5, 64, 64],
                                         stddev=5e-2,
                                         wd=None)
    conv = tf.nn.conv2d(pool1, kernel, [1, 1, 1, 1], padding='SAME')
    biases = _variable_on_cpu('biases', [64], tf.constant_initializer(0.1))
    pre_activation = tf.nn.bias_add(conv, biases)
    conv2 = tf.nn.relu(pre_activation, name=scope.name)
    _activation_summary(conv2)

  # norm2 第二层正则化
  #norm2 = tf.nn.lrn(conv2, 4, bias=1.0, alpha=0.001 / 9.0, beta=0.75,
                    #name='norm2')
  # pool2 第二层池化
  pool2 = tf.nn.max_pool(conv2, ksize=[1, 3, 3, 1],
                         strides=[1, 2, 2, 1], padding='SAME', name='pool2')

  # local3 第一层全连接
  with tf.variable_scope('local3') as scope:
    # Move everything into depth so we can perform a single matrix multiply.
    # 将所有东西都移到深处，以便我们可以执行单个矩阵乘法。
    reshape = tf.reshape(pool2, [images.get_shape().as_list()[0], -1])
    dim = reshape.get_shape()[1].value
    weights = _variable_with_weight_decay('weights', shape=[dim, 1024],
                                          stddev=0.04, wd=0.004)
    biases = _variable_on_cpu('biases', [1024], tf.constant_initializer(0.1))
    local3 = tf.nn.relu(tf.matmul(reshape, weights) + biases, name=scope.name)
    _activation_summary(local3)

  # local4 第2层全连接
  with tf.variable_scope('local4') as scope:
    weights = _variable_with_weight_decay('weights', shape=[1024, 512],
                                          stddev=0.04, wd=0.004)
    biases = _variable_on_cpu('biases', [512], tf.constant_initializer(0.1))
    local4 = tf.nn.relu(tf.matmul(local3, weights) + biases, name=scope.name)
    _activation_summary(local4)

    # local5 第3层全连接
  with tf.variable_scope('local5') as scope:
    weights = _variable_with_weight_decay('weights', shape=[512, 512],
                                          stddev=0.04, wd=0.004)
    biases = _variable_on_cpu('biases', [512], tf.constant_initializer(0.1))
    local5 = tf.nn.relu(tf.matmul(local4, weights) + biases, name=scope.name)
    _activation_summary(local5)

    # local6 第二层全连接
  with tf.variable_scope('local6') as scope:
    weights = _variable_with_weight_decay('weights', shape=[512, 256],
                                          stddev=0.04, wd=0.004)
    biases = _variable_on_cpu('biases', [256], tf.constant_initializer(0.1))
    local6 = tf.nn.relu(tf.matmul(local5, weights) + biases, name=scope.name)
    _activation_summary(local6)

  # linear layer(WX + b),
  # We don't apply softmax here because
  # tf.nn.sparse_softmax_cross_entropy_with_logits accepts the unscaled logits
  # and performs the softmax internally for efficiency.
  # 线性层（WX + b），我们不在这里应用softmax，因为
  # tf.nn.sparse_softmax_cross_entropy_with_logits接受未缩放的logits并在内部执行softmax以提高效率。
  with tf.variable_scope('softmax_linear') as scope:
    weights = _variable_with_weight_decay('weights', [256, NUM_CLASSES],
                                          stddev=1/192.0, wd=None)
    biases = _variable_on_cpu('biases', [NUM_CLASSES],
                              tf.constant_initializer(0.0))
    softmax_linear = tf.add(tf.matmul(local6, weights), biases, name=scope.name)
    _activation_summary(softmax_linear)

  return softmax_linear


def loss(logits, labels):
  """Add L2Loss to all the trainable variables.
  将L2Loss添加到所有可训练变量。

  Add summary for "Loss" and "Loss/avg".
  Args:
    logits: Logits from inference().
    labels: Labels from distorted_inputs or inputs(). 1-D tensor
            of shape [batch_size]

  Returns:
    Loss tensor of type float.
  """
  # Calculate the average cross entropy loss across the batch.
  # 计算整个批次的平均交叉熵损失。
  labels = tf.cast(labels, tf.int64)
  cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
      labels=labels, logits=logits, name='cross_entropy_per_example')
  cross_entropy_mean = tf.reduce_mean(cross_entropy, name='cross_entropy')
  tf.add_to_collection('losses', cross_entropy_mean)
  _activation_summary(cross_entropy_mean)

  # The total loss is defined as the cross entropy loss plus all of the weight
  # decay terms (L2 loss).
  # 总损失定义为交叉熵损失加上所有的权重衰减项（L2损失）。
  return tf.add_n(tf.get_collection('losses'), name='total_loss')


def _add_loss_summaries(total_loss):
  """Add summaries for losses in CIFAR-10 model.

  Generates moving average for all losses and associated summaries for
  visualizing the performance of the network.

  Args:
    total_loss: Total loss from loss().
  Returns:
    loss_averages_op: op for generating moving averages of losses.
  """
  # Compute the moving average of all individual losses and the total loss.
  loss_averages = tf.train.ExponentialMovingAverage(0.9, name='avg')
  losses = tf.get_collection('losses')
  loss_averages_op = loss_averages.apply(losses + [total_loss])

  # Attach a scalar summary to all individual losses and the total loss; do the
  # same for the averaged version of the losses.
  for l in losses + [total_loss]:
    # Name each loss as '(raw)' and name the moving average version of the loss
    # as the original loss name.scalar:标量
    tf.summary.scalar(l.op.name + ' (raw)', l)
    tf.summary.scalar(l.op.name, loss_averages.average(l))

  return loss_averages_op


def train(total_loss, global_step):
  """Train CIFAR-10 model.

  Create an optimizer and apply to all trainable variables. Add moving
  average for all trainable variables.

  Args:
    total_loss: Total loss from loss().
    global_step: Integer Variable counting the number of training steps
      processed.
  Returns:
    train_op: op for training.
  """
  # Variables that affect learning rate.
  num_batches_per_epoch = NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN / FLAGS.batch_size
  #print('num_batches_per_epoch: %s'%num_batches_per_epoch)
  decay_steps = int(num_batches_per_epoch * NUM_EPOCHS_PER_DECAY)

  # Decay the learning rate exponentially based on the number of steps.
  # 根据步骤的数量以指数方式衰减学习速率。
  lr = tf.train.exponential_decay(INITIAL_LEARNING_RATE,
                                  global_step,
                                  decay_steps,
                                  LEARNING_RATE_DECAY_FACTOR,
                                  staircase=True)
  tf.summary.scalar('learning_rate', lr)

  # Generate moving averages of all losses and associated summaries.
  # 生成所有损失和相关汇总的移动平均值。
  loss_averages_op = _add_loss_summaries(total_loss)

  # Compute gradients.计算梯度
  with tf.control_dependencies([loss_averages_op]):
    opt = tf.train.GradientDescentOptimizer(lr)
    grads = opt.compute_gradients(total_loss)

  # Apply gradients. 应用梯度
  apply_gradient_op = opt.apply_gradients(grads, global_step=global_step)

  # Add histograms for trainable variables.
  # 为可训练变量添加直方图。
  '''for var in tf.trainable_variables():
    if var is not None:
      tf.summary.histogram(var.op.name, var)

  # Add histograms for gradients.
  # 为梯度添加直方图
  for grad, var in grads:
    if grad is not None:
      tf.summary.histogram(var.op.name + '/gradients', grad)'''

  # Track the moving averages of all trainable variables.
  # 跟踪所有可训练变量的移动平均值。
  variable_averages = tf.train.ExponentialMovingAverage(
      MOVING_AVERAGE_DECAY, global_step)
  with tf.control_dependencies([apply_gradient_op]):
    variables_averages_op = variable_averages.apply(tf.trainable_variables())

  return variables_averages_op