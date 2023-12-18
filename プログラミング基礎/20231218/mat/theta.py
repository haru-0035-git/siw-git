import matplotlib.pyplot as plt
import numpy as np
from sympy import sieve

# n = 10**5
# p = np.array([i for i in sieve.primerange(2, n)])
# x = p * np.cos(p)
# y = p * np.sin(p)

# scale = 5
# ratio = 2
# width = np.max(p)

# fig, ax = plt.subplots(facecolor="black", figsize=(ratio*scale,scale))
# ax.axis("off")
# ax.set_xlim(-width,width)
# ax.set_ylim(-width/ratio, width/ratio)
# ax.scatter(x,y,s=1,c="yellow")
# plt.title("num of primes: {}".format(len(p)),c="white")
# plt.show()
  
theta = np.linspace(0,4*np.pi,1000)
r = theta ** 2
x = r * np.cos(theta)
y = r * np.sin(theta)
plt.figure(figsize=(8,8))
plt.plot(x,y)
plt.show()