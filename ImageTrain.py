#-*-encoding = utf-8 -*-
from datetime import datetime
import time

import tensorflow as tf

import ImageModel
import os
import ImageEval 
from tensorflow.python import debug as tf_debug

os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string('checkpointDir', './checkpoint/',
                           """Directory where to write event logs """
                           """and checkpoint.""")
tf.app.flags.DEFINE_integer('max_steps', 10000000,
                            """Number of batches to run.""")
tf.app.flags.DEFINE_boolean('log_device_placement', False,
                            """Whether to log device placement.""")
tf.app.flags.DEFINE_integer('log_frequency', 10,
                            """How often to log results to the console.""")


def train():

  with tf.Graph().as_default():
    global_step = tf.train.get_or_create_global_step()

    # Get images and labels for CIFAR-10.
    # Force input pipeline to CPU:0 to avoid operations sometimes ending up on
    # GPU and resulting in a slow down.
    # 获取CIFAR-10的图像和标签。 强制输入管道到CPU：0以避免有时会在GPU上结束并导致减速的操作。
    with tf.device('/cpu:0'):
      images, labels = ImageModel.getTrainInputs()
      print('getTrainInputs')

    # Build a Graph that computes the logits predictions from the
    # inference model.
    # 构建一个graph，用于计算推理模型中的logits预测。
    # logits: 未归一化的概率， 一般也就是 softmax的输入
    logits = ImageModel.inference(images)

    #print(logits)

    # Calculate loss.
    loss = ImageModel.loss(logits, labels)

    # Build a Graph that trains the model with one batch of examples and
    # updates the model parameters.
    # 构建一个graph，通过一批示例来训练模型并更新模型参数。
    train_op = ImageModel.train(loss, global_step)

    print('计算图创建成功')

    class _LoggerHook(tf.train.SessionRunHook):
      """Logs loss and runtime."""

      def begin(self):
        self._step = -1
        self._start_time = time.time()

      def before_run(self, run_context):
        self._step += 1
        return tf.train.SessionRunArgs(loss)  # Asks for loss value.

      def after_run(self, run_context, run_values):
        if self._step % FLAGS.log_frequency == 0:
          current_time = time.time()
          duration = current_time - self._start_time
          self._start_time = current_time

          loss_value = run_values.results
          examples_per_sec = FLAGS.log_frequency * FLAGS.batch_size / duration
          sec_per_batch = float(duration / FLAGS.log_frequency)

          format_str = ('%s: step %d, loss = %.2f (%.1f examples/sec; %.3f '
                        'sec/batch)')
          print (format_str % (datetime.now(), self._step, loss_value,
                               examples_per_sec, sec_per_batch))


    with  tf_debug.LocalCLIDebugWrapperSession(tf.train.MonitoredTrainingSession(
        checkpoint_dir=FLAGS.checkpointDir,
        hooks=[tf.train.StopAtStepHook(last_step=FLAGS.max_steps),
               tf.train.NanTensorHook(loss),
               _LoggerHook()],
        config=tf.ConfigProto(
            log_device_placement=FLAGS.log_device_placement),
        save_checkpoint_steps=500)) as mon_sess:
      mon_sess.add_tensor_filter("has_inf_or_nan", tf_debug.has_nan_or_inf)
      while not mon_sess.should_stop():
        mon_sess.run(train_op)
        #print(mon_sess.run(images))
        #print(mon_sess.run(labels))

def main(argv=None):  # pylint: disable=unused-argument
  train()


if __name__ == '__main__':
  tf.app.run()
