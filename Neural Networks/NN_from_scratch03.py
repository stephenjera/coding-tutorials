import numpy as np

np.random.seed(0)

# Neuron example with random numbers
# Every input has its own weight
# Capital X is standard for input data
X = [[1.1, 4, 6, 2],  # Can be a value from the input layer (tracked values) or other neurons
          [2.1, 4, 3, -4],
          [3.3, 2, 1, 2]]


class LayerDense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))  # This is a tuple!

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


layer1 = LayerDense(4, 5)
layer2 = LayerDense(5, 2)

layer1.forward(X)
#print(layer1.output)

layer2.forward(layer1.output)
print(layer2.output)

#print(0.1*np.random.randn(4, 3))
'''# Weights and biases do not change with batch inputs
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

print(layer02_outputs)'''


