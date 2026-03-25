# Numpy basics
import numpy as np

arr1 = np.array([1,2,3,4,5])
print("1D array: ", arr1)

arr2 = np.array([[1,2,3],[4,5,6]]) # Bracket ke andar list
print("2D array: ", arr2)

#List vs numpy array

py_list = [1,2,3]
print("Python list multiplication: ", py_list*2)

np_array = np.array([1,2,3])
print("Python array multiplication: ", np_array*2)

# creating array from scatch
zeros = np.zeros((3,3))
print(zeros)

ones = np.ones((3,3))
print(ones)

full = np.full((3,3),196)
print(full)

random = np.random.random((3,3)) # In 0's and 1's only
print(random)

sequence = np.arange(0,20,2)
print(sequence)
