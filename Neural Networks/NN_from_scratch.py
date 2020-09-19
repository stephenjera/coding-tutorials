# Neuron example with random numbers
inputs = [1.1, 4, 6]
weights = [3, 4.6, 4]
bias = 3

# output = inputs * weights + bias
output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias
print(output)
