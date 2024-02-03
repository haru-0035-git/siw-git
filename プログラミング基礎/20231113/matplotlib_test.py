import matplotlib.pyplot as plt
import numpy as np
import os

data = np.loadtxt(f'{os.path.dirname(__file__)}/fm08_m_1.csv',delimiter=',')
plt.plot(data)
plt.show()
