import numpy as np

before = np.array([[1,2,3,4], [5,6,7,8]])
print(before)
# [[1 2 3 4]
#  [5 6 7 8]]

after = before.reshape((4, 2))
print(after)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]


# Vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1,v2,v1,v2]))
# [[1 2 3 4]
#  [5 6 7 8]
#  [1 2 3 4]
#  [5 6 7 8]]

h1 = np.ones((2, 4))
h2 = np.zeros((2, 2))

print(np.hstack([h1, h2]))
# [[1. 1. 1. 1. 0. 0.]
#  [1. 1. 1. 1. 0. 0.]]

