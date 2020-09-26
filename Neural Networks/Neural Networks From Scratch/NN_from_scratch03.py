import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()  # Sets random seed and default data type for numpy

# Has two features X and y 
X, y = spiral_data(100, 3)


class LayerDense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))  # This is a tuple!

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


class ActivationReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


layer1 = LayerDense(2, 5) 
activation1 = ActivationReLU()
layer1.forward(X)
activation1.forward(layer1.output)
print(activation1.output)



