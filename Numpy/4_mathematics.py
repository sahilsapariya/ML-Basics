import numpy as np

a = np.array([1,2,3,4])

print(a + 2)    # [3 4 5 6]

print(a - 2)    # [-1  0  1  2]

print(a * 2)     # [2 4 6 8]

print(a / 2)    # [0.5 1.  1.5 2. ]

print(a ** 2)   # [ 1  4  9 16]

a += 2
print(a)    # [3 4 5 6]

b = np.array([0,1,0,1])

print(a + b)    # [3 5 5 7]



# Trigonomatry
print(np.sin(a))    # [ 0.14112001 -0.7568025  -0.95892427 -0.2794155 ]
print(np.cos(a))    # [-0.9899925  -0.65364362  0.28366219  0.96017029]
print(np.tan(a))    # [-0.14254654  1.15782128 -3.38051501 -0.29100619]
print(np.sinh(a))   # [ 10.01787493  27.2899172   74.20321058 201.71315737]
print(np.cosh(a))   # [ 10.067662    27.30823284  74.20994852 201.71563612]
print(np.tanh(a))   # [0.99505475 0.9993293  0.9999092  0.99998771]

# Linear algebra

a = np.ones((2, 3))
print(a)
# [[1. 1. 1.]
#  [1. 1. 1.]]

b = np.full((3, 2), 2)
print(b)
# [[2 2]
#  [2 2]
#  [2 2]]

print(np.matmul(a, b))
# [[6. 6.]
#  [6. 6.]]


# Finding determinant
c = np.identity(3)
print(np.linalg.det(c)) # 1.0

# Determinant
# Trace
# Singular Vector Decomposition
# Eigenvalues
# Matrix Norm
# Inverse


# Statics

stats = np.array([[1,2,3], [4,5,6]])

print(np.min(stats))    # 1
print(np.max(stats))    # 6

print(np.min(stats, axis=1)) # [1 4]
print(np.max(stats, axis=1)) # [3 6]
