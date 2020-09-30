import numpy as np


# Multilayer perceptron
class MLP:
    def __init__(self, num_inputs=3, num_hidden_layers=[3, 5], num_outputs=2):
        """:param num_inputs: Number of inputs to neural net
           :param num_hidden_layers: Each entry is the number of neurons in a layer,total is size of array
           :param num_outputs: Number of outputs to neural net"""
        self.num_inputs = num_inputs
        self.num_hidden_layers = num_hidden_layers
        self.num_outputs = num_outputs

        # Cast inputs and outputs to list the join to single list
        layers = [self.num_inputs] + self.num_hidden_layers + [self.num_outputs]
        # print("num inputs: ", [self.num_inputs])
        # print("Layers: ", layers)

        # Initiate random weights
        self.weights = []
        # Iterate through all the layers and create weights
        # print("layers length: ", len(layers))
        for i in range(len(layers)-1):
            # Build weight matrices "w"
            w = np.random.rand(layers[i], layers[i+1])
            print("weight matrix: ", w)
            self.weights.append(w)  # Add newly created data to weights list

    def forward_propagation(self, inputs):
        activations = inputs

        for w in self.weights:
            # Calculate net inputs
            net_inputs = np.dot(activations, w)

            # Calculate activations
            activations = self._sigmoid(net_inputs)

        return activations

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))


if __name__ == '__main__':
    # Create MLP
    mlp = MLP()

    # Create inputs
    inputs = np.random.rand(mlp.num_inputs)

    # Perform forward propagation
    outputs = mlp.forward_propagation(inputs)

    # Print the results
    print("The network input is: {}".format(inputs))
    print("The network output is: {}".format(outputs))
