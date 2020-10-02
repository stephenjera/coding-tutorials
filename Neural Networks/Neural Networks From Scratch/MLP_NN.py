import numpy as np

# TODO: Save activations
# TODO: Implement back propagation
# TODO: Implement gradient decent
# TODO: Implement training
# TODO: Train with some dummy data
# TODO: Make some predictions


class MLP:
    """Multilayer Perceptron Class"""
    def __init__(self, num_inputs=4, num_hidden_layers=[3, 5], num_outputs=2):
        """Constructor for MLP. Takes the number of inputs, hidden layers and outputs
           :param int num_inputs: Number of inputs to neural net
           :param list num_hidden_layers: Each entry is the number of neurons in a layer,total is size of array
           :param int num_outputs: Number of outputs to neural net
        """
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
            # Build weight matrices "w" of shape [x,y] with values between 0 and 1
            # Number of rows = current layer
            # Number of columns = number of neurons in next layer
            w = np.random.rand(layers[i], layers[i+1])
            print("weight matrix: ", w)
            self.weights.append(w)  # Add newly created data to weights list (creates list of arrays)
        print("\n")

        activations = []
        for i in range(len(layers)):
            a = np.zeros(layers[i])
            activations.append(a)
        self.activations = activations

        derivatives = []
        for i in range(len(layers)):
            d = np.zeros(layers[i], layers[i]+1)
            derivatives.append(d)
        self.derivatives = derivatives

    def forward_propagation(self, inputs):
        # The first layer number of activation = number of inputs
        activations = inputs

        for w in self.weights:
            # Calculate net inputs
            # Net inputs are activation of the previous layer multiplied by the weights
            net_inputs = np.dot(activations, w)

            # Calculate activations
            activations = self._sigmoid(net_inputs)
            print("Activations: ", activations)
            slef.activations[i+1] = activations
        print("\n")
        return activations

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))


if __name__ == '__main__':
    # Create MLP
    mlp = MLP(5)

    # Create inputs matrix with random numbers between 0 - 1
    inputs = np.random.rand(mlp.num_inputs)

    # Perform forward propagation
    outputs = mlp.forward_propagation(inputs)

    # Print the results
    print("mlp weights: ", mlp.weights)
    print("\n")
    print("The network input is: {}".format(inputs))
    print("The network output is: {}".format(outputs))
