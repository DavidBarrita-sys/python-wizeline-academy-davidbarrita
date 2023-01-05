import numpy as np
import math


# This function can sum from two values up to as many as the user desires.
def addition(addition_values):
    total = 0
    for value in addition_values:
        total += value
    return total


# This function can subtract two values.
def subtract_by_simple(subtract_values):
    total = subtract_values[0] - subtract_values[1]
    return total


# This function can subtract from one target to N values.
def subtract_by_target(subtract_values):
    target = subtract_values[0]
    total = 0
    for value in subtract_values:
        if value != subtract_values[0]:
            total += value
    value = target - total
    return value


# This function can multiply two numbers
def multiplication_by_simple(multiplication_values):
    total = multiplication_values[0] * multiplication_values[1]
    return total


# This function can multiply N numbers
def multiplication_by_n_values(multiplication_values):
    total = multiplication_values[0]
    length = len(multiplication_values)
    for i in range(length):
        if i > 0:
            total = (total * multiplication_values[i])
    return total


# This function can divide
def divide_by_simple(divide_values):
    return divide_values[0] / divide_values[1]


# This function can get the root of one number
def root_by_simple(value):
    total = math.sqrt(value[0])
    return total


# This function can get the root of N numbers
def root_by_n_values(root_values):
    new_values = []
    for value in root_values:
        new_values.append(math.sqrt(value))
    return new_values


# This function can get the pow of one number
def pow_by_simple(pow_values):
    return math.pow(pow_values[0], pow_values[1])


# This function can get the sin
def sin_by_simple(value):
    return np.sin(value[0])


# This function can get the sin of N numbers
def sin_by_n_values(sin_values):
    new_values = []
    for value in sin_values:
        new_values.append(np.sin(value))
    return new_values


# This function can get the cos
def cos_by_simple(value):
    return np.cos(value[0])


# This function can get the cos of N numbers
def cos_by_n_values(cos_values):
    new_values = []
    for value in cos_values:
        new_values.append(np.cos(value))
    return new_values


# This function can get the tan
def tan_by_simple(value):
    return np.tan(value[0])


# This function can get tan of N numbers
def tan_by_n_values(tan_values):
    new_values = []
    for value in tan_values:
        new_values.append(np.tan(value))
    return new_values
