import numpy as np
import os
num = np.loadtxt(f'{os.path.dirname(__file__)}\\book1.csv',delimiter=',')

print(num)
print(round(np.mean(num[:,0]),2))
print(round(np.mean(num[:,1]),2))
print(round(np.mean(num[:,2]),2))
