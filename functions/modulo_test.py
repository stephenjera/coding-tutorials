# How modulo functions


# Returns the remainder
A = 10
B = 4
print("Remainder: ", A % B)

# Returns the smallest number
C = 50
D = 51
print("Smallest number: ", C % D)


def f(x):
    """Takes x values and performs g(x)"""
    return g(x) + 3 % 2


def g(x):
    return (x ** 2) + 2


print("Function output: ", f(g(1)))
