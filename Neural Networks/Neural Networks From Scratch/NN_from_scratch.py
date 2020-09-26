# Neuron example with random numbers
# Every input has its own weight
inputs = [1.1, 4, 6, 2]  # Can be a value from the input layer (tracked values) or other neurons
weights1 = [3, 4.6, 4]
weights2 = [0.5, -0.91, 0.28, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]
bias1 = 2  # A neuron only has 1 bias
bias2 = 3
bias3 = 0.5

# output = inputs * weights + bias
# Modeling 3 neurons with 4 inputs
output = [inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[2]*weights1[2] + bias1,
          inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[2]*weights2[2] + bias2,
          inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[2]*weights3[2] + bias3]
print(output)
