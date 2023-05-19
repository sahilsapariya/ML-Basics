"""
    Accessing/Changing specific elements, rows, columns etc.
"""

import numpy as np

a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(a)
# [[ 1  2  3  4  5  6  7]
#  [ 8  9 10 11 12 13 14]]

# Get a specific element [r, c]
print(a[1, 5])  # 13
print(a[1, -2]) # 13

# Get specific row
print(a[1, :])  # [ 8  9 10 11 12 13 14]

# Get specific column
print(a[:, 3])  # [ 4 11]

# Getting a littel more fancy [startindex:endindex:stepsize]
print(a[0, 1:6:2])  # [2,4,6]
print(a[0, 1:-1:2])  # [2,4,6]


a[1, 5] = 20
print(a)
# [[ 1  2  3  4  5  6  7]
#  [ 8  9 10 11 12 20 14]]

a[:, 2] = [1,2]
print(a)
# [[ 1  2  1  4  5  6  7]
#  [ 8  9  2 11 12 20 14]]


# 3 Dimentional Examples

b = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(b)
# [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]

# Get specific element
print(b[0, 1, 1])   # 4

# replace 
b[:, 1, :] = [[9,9], [8,8]]
print(b)
# [[[1 2]
#   [9 9]]

#  [[5 6]
#   [8 8]]]