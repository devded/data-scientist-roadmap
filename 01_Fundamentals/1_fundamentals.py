#!/usr/bin/python3


import numpy as np


# Generate a list of 4 list of 5 random numbers each
list_of_lists = [np.random.randint(low=0, high=100, size=5) for _ in range(4)]

# Convert list_of_lists into numpy matrix
matrix = np.matrix(list_of_lists)
print(f'Here is your matrix:\n{matrix}\n')

# Addition
new_matrix = np.sum([matrix, 5])
print(f'Here is your matrix with addition +5:\n{new_matrix}\n')

# Multiplication
new_matrix = np.multiply(matrix, matrix)
print(f'Here is your matrix multiplied by itself:\n{new_matrix}\n')

# Transposition
new_matrix = np.transpose(matrix)
print(f'Here is your matrix transposed:\n{new_matrix}\n')
