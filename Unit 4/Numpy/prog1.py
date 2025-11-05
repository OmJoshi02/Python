import numpy as np

l1 = [x for x in range(1,1000000) if x%2 == 1]
l2 = [y for y in range(1,1000000) if y%2 == 1]

arr1 = np.array(l1)
arr2 = np.array(l2)

print(arr1 + arr2)