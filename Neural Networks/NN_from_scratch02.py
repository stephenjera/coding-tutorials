import numpy as np

# Neuron example with random numbers
# Every input has its own weight
inputs = [1.1, 4, 6, 2]  # Can be a value from the input layer (tracked values) or other neurons
weights = [[3, 4.6, 4, 4],
            [0.5, -0.91, 0.28, -0.5],
            [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 4]

# Order of weights and inputs matters
output = np.dot(weights, inputs) + biases
print(output)


