"""
    Initializing Different Types of Arrays
"""

import numpy as np

a = np.zeros(5) # [0. 0. 0. 0. 0.]
a = np.zeros(5, dtype='int') # [0 0 0 0 0]
print(a)

print(np.ones((4,2,2), dtype='int32'))
# [[[1 1]
#   [1 1]]

#  [[1 1]
#   [1 1]]

#  [[1 1]
#   [1 1]]

#  [[1 1]
#   [1 1]]]

# Any other number
print(np.full((2,2), 99))
# [[99 99]
#  [99 99]]

# Any other number (full_like)
print(np.full_like(a, 4))   # [4 4 4 4 4]
print(np.full_like(a.shape, 4))   # [4]

# Random decimal numbers
print(np.random.rand(4, 2))
# [[0.07512159 0.87904902]
#  [0.01333747 0.11420965]
#  [0.52322437 0.61194531]
#  [0.77275923 0.57352405]]

print(np.random.random_sample(a.shape))
# [0.91002803 0.60154868 0.81407811 0.8764333  0.7060545 ]

# Random Integer values
print(np.random.randint(7, size=(3,3)))
# [[5 4 0]
#  [5 4 3]
#  [6 1 5]]
print(np.random.randint(4, 8, size=(3,3)))
# [[6 6 4]
#  [7 5 7]
#  [7 7 6]]

# The identity matrix
print(np.identity(5))
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]


# Repeating arrays
arr = np.array([1,2,3])
r1 = np.repeat(arr, 3, axis=0)
print(r1)
# [1 1 1 2 2 2 3 3 3]

arr = np.array([[1,2,3]])
r1 = np.repeat(arr, 3, axis=0)
print(r1)

# !Excersice: WAP to print pattern like this
# [[1. 1. 1. 1. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 0. 9. 0. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 1. 1. 1. 1.]]

output = np.ones((5, 5))
z = np.zeros((3, 3))
z[1, 1] = 9
output[1:-1, 1:-1] = z

# !Excersice ends


# Copying arrays
# because normally python follows shallow copy
a = np.array([1,2,3])
b = a
b[0] = 100
print(a)    # [100   2   3]

# to overcome this issue use .copy() method
a = np.array([1,2,3])
b = a.copy()
b[0] = 100
print(a)    # [1   2   3]
print(b)    # [100   2   3]
