import tensorflow as tf
import numpy as np

data = tf.Tensor(np.random.randint(1,10,5))
datapd = tf.math.softmax(data)

data2 = tf.Tensor(np.random.randint(1,10,5))
datapd2 = tf.math.softmax(data2)

print(tf.distributions.kl_divergence(datapd, datapd2), sign, data*sign)