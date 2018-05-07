from datetime import datetime
import math
import time

import numpy as np
import pandas as pd
import tensorflow as tf

import ImageModel

tf.app.flags.DEFINE_string('checkpoint_dir', './checkpoint/',
                           """Directory where to read model checkpoints.""")

FLAGS = tf.app.flags.FLAGS

NUM_EXAMPLES_PER_EPOCH_FOR_TEST=1000

def test_once(saver,logits):
  """Run Eval once.

  Args:
    saver: Saver.
    summary_writer: Summary writer.
    top_k_op: Top K op.
    summary_op: Summary op.
  """
  with tf.Session() as sess:

    sess.run(tf.global_variables_initializer())
    sess.run(tf.local_variables_initializer())

    ckpt = tf.train.get_checkpoint_state(FLAGS.checkpoint_dir)
    if ckpt and ckpt.model_checkpoint_path:
      # Restores from checkpoint
      saver.restore(sess, ckpt.model_checkpoint_path)
      # Assuming model_checkpoint_path looks something like:
      #   /my-favorite-path/ImageModel_train/model.ckpt-0,
      # extract global_step from it.
      global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
    else:
      print('No checkpoint file found')
      return

    # Start the queue runners.
    coord = tf.train.Coordinator()
    try:
      threads = []
      for qr in tf.get_collection(tf.GraphKeys.QUEUE_RUNNERS):
        threads.extend(qr.create_threads(sess, coord=coord, daemon=True,
                                         start=True))

      num_iter = int(math.ceil(NUM_EXAMPLES_PER_EPOCH_FOR_TEST / FLAGS.batch_size))

      predictions = []
      step = 0
      while step < num_iter and not coord.should_stop():
        step = step +1
        labels = sess.run(logits)
        predictions.extend(np.argmax(labels,axis=1))
        #labels = np.argmax(labels,axis=1)
    except Exception as e:  # pylint: disable=broad-except
      coord.request_stop(e)
    finally:
      result = pd.read_table('test.txt',delim_whitespace=True,header=None)
      result[1] = predictions[:NUM_EXAMPLES_PER_EPOCH_FOR_TEST]
      #print(len(result[1]))
      result.to_csv('result.csv',index=None,header=None,sep=' ')

    coord.request_stop()
    coord.join(threads, stop_grace_period_secs=10)


def test():
  """Eval CIFAR-10 for a number of steps."""
  with tf.Graph().as_default() as g:
    # Get images and labels for CIFAR-10.
    images, labels = ImageModel.getTestInputs()

    # Build a Graph that computes the logits predictions from the
    # inference model.
    logits = ImageModel.inference(images)

    # Restore the moving average version of the learned variables for eval.
    variable_averages = tf.train.ExponentialMovingAverage(
        ImageModel.MOVING_AVERAGE_DECAY)
    variables_to_restore = variable_averages.variables_to_restore()
    #print('variables_to_restore%s:'% variables_to_restore)
    saver = tf.train.Saver(variables_to_restore)


    test_once(saver,logits)


def main(argv=None):  # pylint: disable=unused-argument
  test()


if __name__ == '__main__':
  tf.app.run()
