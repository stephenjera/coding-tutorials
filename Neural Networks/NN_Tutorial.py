import numpy


def neural_net(measure1, measure2, weight1, weight2, bias):
    """Takes two measurements, two weights and a bias """
    # z in intermediate value
    z = (measure1 * weight1) + (measure2 * weight2) + bias
    return sigmoid(z)


def sigmoid(x):
    """Changes input to a number between 0 and 1"""
    return 1/(1 + numpy.exp(-x))


w1 = numpy.random.randn()
w2 = numpy.random.randn()
b = numpy.random.randn()

print(neural_net(3, 1.5, w1, w2, b))  # From pretend dataset (made up)

