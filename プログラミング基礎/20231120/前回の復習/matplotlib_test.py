import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('fm08_m_1.csv',delimiter=',')
plt.plot(data)
plt.show()
