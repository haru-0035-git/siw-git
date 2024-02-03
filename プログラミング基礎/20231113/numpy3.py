# import random as r
# rand = r.randint(1,6)
# print(rand)

# list = [1,2,3,4,5,6,7]
# a=r.choice(list)
# print(a)

#(1)
import numpy as np
# A=np.array([[1,4,-3],[-2,1,2]])
# B=np.array([[2,-3,5],[-1,4,1]])
# C=2*A-3*B
# print(C)

#(2)
# z1=2-3j
# z2=complex(2,-3)
# z3=3+0j
# print(z1, z2)
# print(type(z3))
# print(z1.real, z1.imag)
# print(type(z1.real),type(z1.imag))
# print(z1.conjugate())
# A=np.array([[2+3j, -1+2j, 2+1j], [-3 -1j, 3+4j, 2-1j]])
# B=np.array([[1+1j, 2j],[-1j, 3+2j], [5-2j, 6+ 1j]])
# C=A@B
# D=B@A
# print(C,D,sep='¥n')
# print(np.conjugate(C.transpose()))
# print(C.T)

#(3)
import numpy.linalg as LA
# A=np.array([[1, 3, 5], [-2, 5, 2], [3, 2, 4]])
# b=np.array([14, -6, 16])
# #A=np.array([[1,3,2,-1],[2,-1,-5,2],[3,2,-3,1],[1,-4,-7,3]])
# #b=np.array([5,-2,3,7])
# r=LA.matrix_rank(A)
# print('rank(A)=',r)
# try:
#     x=LA.solve(A,b)
#     print(x)
# except Exception as message:
#     print(message)

# A=np.array([[-5, 2], [1, -1]])
# b=np.array([-8,-2])

# x=LA.solve(A,b)
# print(x)


import numpy as np
import os
score = np.loadtxt(f'{os.path.dirname(__file__)}\seiseki.csv',delimiter=',')
# print(score)
print(np.mean(score,axis=1))
# print(np.max(score,axis=0))
# print(np.min(score,axis=0))
# print(np.median(score,axis=0))
# print(np.var(score,axis=0))
# print(np.std(score,axis=0))


# score = np.loadtxt('weather.csv',delimiter=',')
# # print(score)
# print(np.mean(score,axis=0))
# print(np.max(score,axis=0))
# print(np.min(score,axis=0))
# print(np.median(score,axis=0))
# print(np.var(score,axis=0))
# print(np.std(score,axis=0))

# score = np.loadtxt('fm08_m_1.csv',delimiter=',')
# print(score)

# import numpy as np
# score = np.loadtxt('lake.csv',delimiter=',')
# print(score)
# print(f'平均深度は{np.mean(score[:,1])}mです')
# print(f'最大面積は{np.max(score[:,0])}m^2です')