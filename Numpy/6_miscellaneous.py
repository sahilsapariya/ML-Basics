"""
    There is some data in data.txt
    Load the data from file
"""
import numpy as np

# Loading data from file

# type casting to 'int32' using astype() method
filedata = np.genfromtxt('Numpy/data.txt', delimiter=',')
print(filedata)
# [[  1.  13.  21.  11. 196.  75.   4.   3.  34.   6.   7.   8.   0.   1.
#     2.   3.   4.   5.]
#  [  3.  42.  12.  33. 766.  75.   4.  55.   6.   4.   3.   4.   5.   6.
#     7.   0.  11.  12.]
#  [  1.  22.  33.  11. 999.  11.   2.   1.  78.   0.   1.   2.   9.   8.
#     7.   1.  76.  88.]]
filedata = filedata.astype('int32')
print(filedata)
# [[  1  13  21  11 196  75   4   3  34   6   7   8   0   1   2   3   4   5]
#  [  3  42  12  33 766  75   4  55   6   4   3   4   5   6   7   0  11  12]
#  [  1  22  33  11 999  11   2   1  78   0   1   2   9   8   7   1  76  88]]

# type casting using 'dtype' attribute
print(np.genfromtxt('Numpy/data.txt', delimiter=',', dtype='int32'))


# Boolean Masking and Advanced Indexing
print(filedata > 50)
# [[False False False False  True  True False False False False False False
#   False False False False False False]
#  [False False False False  True  True False  True False False False False
#   False False False False False False]
#  [False False False False  True False False False  True False False False
#   False False False False  True  True]]


print(filedata[filedata > 50])
# Gives the output for true values
# [196  75 766  75  55 999  78  76  88]


# You can index with a list in NumPy
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]])    # [2 3 9]


print(((filedata > 50) & (filedata < 100)))   
# [[False False False False False  True False False False False False False
#   False False False False False False]
#  [False False False False False  True False  True False False False False
#   False False False False False False]
#  [False False False False False False False False  True False False False
#   False False False False  True  True]]
print(filedata[((filedata > 50) & (filedata < 100))])   # [75 75 55 78 76 88]


