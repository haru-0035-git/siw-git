import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

r=0.2
w=2

def func(X,t):
    dXdt=[X[1],-r*X[1]-w*X[0]]
    return dXdt

X0 = [1,0]
t = np.arange(0,40,0.01)

X = odeint(func,X0,t) #微分方程式を解く



plt.axhline(0, color='black', lw=0.8)



plt.plot(t,X[:,0]) #グラフの作成
plt.show() #グラフの表示