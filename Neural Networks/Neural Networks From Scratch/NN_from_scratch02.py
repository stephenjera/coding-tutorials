import numpy as np

# Neuron example with random numbers
# Every input has its own weight
inputs = [[1.1, 4, 6, 2],  # Can be a value from the input layer (tracked values) or other neurons
          [2.1, 4, 3, -4],
          [3.3, 2, 1, 2]]

# Weights and biases do not change with batch inputs
weights = [[3, 4.6, 4, 4],
           [0.5, -0.91, 0.28, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 4]

weights2 = [[3, 4.6, 4],
           [0.5, -0.91, 0.28],
           [-0.26, -0.27, 0.17]]
biases2 = [2, 3, 4]

# Order of weights and inputs matters
layer01_outputs = np.dot(inputs, np.array(weights).T) + biases
#  Adding a second layer od neurons
layer02_outputs = np.dot(layer01_outputs, np.array(weights2).T) + biases2

print(layer02_outputs)


