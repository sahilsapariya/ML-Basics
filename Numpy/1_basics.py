"""
    Load in NumPy
"""

import numpy as np

a = np.array([1,2,3])
print(a)
# we can also specify the data type in list
# a = np.array([1,2,3], dtype='int16')

b = np.array([[9.0,8.0,7.0], [6.0,4.0,5.5]])
print(b)

# Get Dimension
print(a.ndim)   # 1
print(b.ndim)   # 2

# Get Shape
print(a.shape)  # (3, )
print(b.shape)  # (3, 4)

# Get Type
print(a.dtype)  # int32
print(b.dtype)  # float64

# Get Size
print(a.size)    # 3

# Gives output in bytes
# If there is 'int32' then a.itemsize will be 4
# and if 'int16' then a.itemsize will be 2
print(a.itemsize)   # 4 


# Get total size
print(a.size * a.itemsize)  # 12
# or
print(a.nbytes) # 12