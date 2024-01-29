import numpy as np
import numpy.linalg as LA

A = np.array([[5,3],[4,-3]])
b = np.array([4,14])
try:
    x = LA.solve(A,b)
    print(x)
except Exception as e:
    print(e)
