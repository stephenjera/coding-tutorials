import numpy as np
from random import random

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
        # Save parameters in class instance
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
            # print("weight matrix{}: {}".format(i, w))
            # Creates weight matrices
            self.weights.append(w)  # Add newly created data to weights list
        # print("\n")

        # Create a place to save activations
        activations = []
        for i in range(len(layers)):
            a = np.zeros(layers[i])  # Number of zeroes = number of neurons in layer
            activations.append(a)
        self.activations = activations

        # Create a place to save derivatives
        # dE/dW, derivative of error with respect to weight
        # Weight matrices are in-between layers so one less total layers
        derivatives = []
        for i in range(len(layers)-1):
            # Rows = neurons in current layer, columns = neurons in next layer
            d = np.zeros((layers[i], layers[i+1]))  # Zeros has multiple parameters so parenthesis needed
            derivatives.append(d)
        self.derivatives = derivatives

    def forward_propagation(self, inputs):
        """Computes the forward propagation of the network based on inputs
        :param (ndarray) inputs: inputs signals
        :returns ndarray activations: output values
        """
        # The input layer activation is just the input itself
        activations = inputs
        self.activations[0] = inputs

        # Iterate through the network layers
        for i, w in enumerate(self.weights):
            # Calculate net inputs
            # Net inputs are activations of the previous layer multiplied by the weights
            net_inputs = np.dot(activations, w)

            # Apply sigmoid activation function
            activations = self._sigmoid(net_inputs)
            # print("Activations: ", activations)
            # Activation(a) of layer 3 = sigmoid(h_3)  (h = output)
            # h_3 = a_3 * W_2, the activation is for next layer
            self.activations[i+1] = activations
        # print("\n")
        return activations  # Return output layer activations

    def back_propagation(self, error_nn, verbose=False):
        # Error = expected output(y) - prediction
        # Error = (y - a_[i+1])
        # a = activations, h = output, s' = derivative
        # dE/dW_i = (y - a_[i+1]) s'(h_[i+1])) a_i
        # s'(h_[i+1]) = s(h_[i+1])(1 - s(h_[i+1])
        # s(h_[i+1]) = a_[i+1]
        # dE/dW_[i-1] = (y - a_[i+1] s'(h_[i+1])) w_i s'(h_i) a_[i-1]

        for i in reversed(range(len(self.derivatives))):
            activations = self.activations[i+1]

            delta = error_nn * self._sigmoid_derivative(activations)  # ndarray([0.1, 0.2]) --> ndarray([[0.1, 0.2]])
            delta_reshaped = delta.reshape(delta.shape[0], -1).T

            current_activations = self.activations[i]  # ndarray([0.1, 0.2]) --> ndarray([[0.1], [0.2]])
            # change activations to column vector
            current_activations_reshaped = current_activations.reshape(current_activations.shape[0], -1)

            self.derivatives[i] = np.dot(current_activations_reshaped, delta_reshaped)
            error_nn = np.dot(delta, self.weights[i].T)

            if verbose:
                print("Derivatives for W{}: {}".format(i, self.derivatives[i]))
                print("\n")
        return error_nn

    def gradient_decent(self, learning_rate):
        for i in range(len(self.weights)):
            weights = self.weights[i]
            # print("Original W{} {}".format(i, weights))
            # print("\n")
            derivatives = self.derivatives[i]
            weights += derivatives * learning_rate
            # print("Modified W{} {}".format(i, weights))
            # print("\n")

    def train_model(self, inputs, targets, epochs, learning_rate):
        """Trains the neural network
        :param inputs
        :param targets
        :param epochs: Number of times to feed whole dataset to neural network
        :param learning_rate
        """
        for i in range(epochs):
            sum_error = 0
            for (input, target) in zip(inputs, targets):
                # Perform forward propagation
                output = self.forward_propagation(input)

                # Calculate error
                error = target - output

                # Back propagation
                self.back_propagation(error)

                # Apply gradient decent
                self.gradient_decent(learning_rate)

                sum_error += self.mse(target, output)

            # Report error
            print("Error: {} at epoch {}".format(sum_error / len(inputs), i))

    @staticmethod
    def mse(target, output):
        """Calculates Mean Squared Error"""
        return np.average((target - output)**2)

    @staticmethod
    def _sigmoid_derivative(x):
        return x * (1.0 - x)

    @staticmethod
    def _sigmoid(x):
        """Sigmoid activation function
        :param x: Value to be processed
        :returns y: Output
        """
        y = 1 / (1 + np.exp(-x))
        return y


if __name__ == '__main__':
    # Create dataset to train network for the sum operation
    inputs = np.array([[random() / 2 for _ in range(2)] for _ in range(1000)])
    targets = np.array([[i[0] + i[1]] for i in inputs])

    # Create MLP
    mlp = MLP(2, [5], 1)

    # Train MLP
    mlp.train_model(inputs, targets, 50, 0.1)

    # Create dummy data
    input = np.array([0.5, 0.1])
    target = np.array([0.1])
    
    output = mlp.forward_propagation(input)
    print()
    print()
    print("Network thinks {} + {} = {}".format(input[0], input[1], output[0]))
    '''
    # Perform forward propagation
    outputs = mlp.forward_propagation(inputs)

    # Calculate error
    error = target - outputs

    # Back propagation
    mlp.back_propagation(error, verbose=True)

    # Apply gradient decent
    mlp.gradient_decent(learning_rate=1)'''

    '''# Print the results
    print("mlp weights: ", mlp.weights)
    print("\n")
    print("The network input is: {}".format(inputs))
    print("The network output is: {}".format(outputs))'''
