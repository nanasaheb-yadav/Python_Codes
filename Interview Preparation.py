import numpy as np

#print(np.random.rand(100))

# 1. count the occurrence of each value in a numpy array
arr = np.array([0, 5, 5, 0, 2, 4, 3, 0, 0, 5, 4, 1, 9, 9])
print(np.bincount(arr))

# 2. remove from one array those items that exist in another.
a = np.array([5, 4, 3, 2, 1])
b = np.array([4, 8, 9, 10, 1])
# remove from one array those items that exist in another
print(np.setdiff1d(a, b))
# remove duplicates from both array and keep only unique values
print(np.setxor1d(a, b))

# 3. sort a numpy array by a specific column in a 2D array.
arr = np.array([[10, 20, 3], [4, 5, 6], [11,1,1]])
print(arr[arr[:,1].argsort()])

# 4. find the indices of an array where a condition is true.
arr = np.array([[9,8,7],[6,5,4],[3,2,1]])
print(arr[arr > 3])
print(arr > 3)
# 5.
nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])
print(np.histogram(nums, bins))

