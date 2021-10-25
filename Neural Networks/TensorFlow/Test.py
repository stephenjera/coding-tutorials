import tensorflow as tf
print('Your TensorFlow version: {0}'.format(tf.__version__))


# Create a constant
A = tf.constant([[4, 2],
                [5, 4]])
print(A)
