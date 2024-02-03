import matplotlib.pyplot as plt
import numpy as np

# import numpy as np 
# import matplotlib.pyplot as plt  
# x=np.array(range(0, 10))
# print(x) 
# y=x 
# plt.plot(x, y) 
# plt.show()
# import numpy as np 
# import matplotlib.pyplot as plt  
# x = np.arange(-np.pi,np.pi,0.1) 
# y = np.sin(x) 
# print(x[:10]) 
# print(y[:10])  
# plt.plot(x, y) 
# plt.show()

x = np.arange(-2*np.pi,2*np.pi,0.2)
y0 = np.sin(x)
y1 = np.cos(x)
# # y1 = np.tan(x)
# plt.plot(x,y0,label = 'y = sin(x)')
# plt.plot(x,y1,label = 'y = cos(x)')
# plt.legend()
# plt.show()

#表示エリアを設定
# plt.xlim([3, 5])
# plt.ylim([-1.0, -0.5])

#グリッド表示と凡例
# plt.title('sample graph')
# plt.xlabel('degree')
# plt.ylabel('value')
# plt.grid(which='both', axis='x', color='#0000ff', alpha=0.25,
# linestyle='-', linewidth=1)
# plt.grid(which='major', axis='y', color='#00ff00', alpha=0.5,
# linestyle=':', linewidth=2)

# plt.show()

#グラフを2分割する
# fig, (p_a1,p_a2) = plt.subplots(2,1)
# p_a1.plot(x, y0, 'r', label='y = sin(x)')
# p_a1.legend()
# p_a2.plot(x, y1, 'b', label='y = cos(x)')
# p_a2.legend()
# plt.show()

#テキストの追加
# plt.plot(x, y0, 'b', label='y = sin(x)')
# plt.legend()
# plt.text(2.1, -0.04, 'This is Sample!', fontsize=14, color='m')
# plt.arrow(2,0, -1.5, 0, width=0.05,head_width=0.2, head_length=0.5, color='y')
# plt.xlim([-1,3])
# plt.ylim([-1, 1])
# plt.show()

#一定幅で塗りつぶし
# plt.plot(x, y0, 'b', label='y = sin(x)')
# plt.legend()
# plt.axhspan(0., 1., color='g', alpha=0.25)
# plt.axvspan(-np.pi, 0., color='c', alpha=0.25)
# plt.show()

#指定範囲で塗りつぶし
# s_x = np.arange(-np.pi, np.pi+0.001, np.pi / 20)
# s_y = np.sin(s_x)
# c_x = np.arange(-np.pi, np.pi+0.001, np.pi / 20)
# c_y = np.cos(c_x)
# plt.plot(x, y0, 'b', label='y = sin(x)')
# plt.legend()
# plt.fill(s_x, s_y, color='m', alpha=0.2)
# plt.fill(c_x, c_y, color='c', alpha=0.2)
# plt.show()

#棒グラフ
# x = list('abcdefg')
# y2 = np.array([np.random.randint(75) + 25 for i in range(7)])
# plt.bar(x, y2, label='random value.')
# plt.legend()
# plt.show()

#棒グラフを積み上げる
# x = list('abcdefg')
# y3 = np.array([np.random.randint(75) + 25 for i in range(7)])
# y4 = np.array([np.random.randint(75) + 25 for i in range(7)])
# plt.bar(x, y3, label='random A')
# plt.bar(x, y4, bottom=y3, label='random B')
# plt.legend()
# plt.show()

#円グラフを書く
# x = np.array([np.random.randint(75) + 25 for i in range(7)])
# y5 = list('abcdefg')
# ex = [0, 0, 0, 0.25, 0, 0, 0]
# plt.pie(x, labels=y5, shadow=True, autopct='%1.1f%%', explode=ex)
# plt.legend()
# plt.show()

#ヒストグラム
# (sigma, mu) = (10, 50)
# value = np.random.randn(1000)*sigma+mu
# plt.hist(value, 25)
# plt.show()

#ヒストグラムに確率密度曲線の表示
# from scipy.stats import norm
# (sigma, mu) = (10, 50)
# value = np.random.randn(1000)*sigma+mu
# (n, bins, patches) = plt.hist(value, 50, density=True)
# plt.plot(bins, norm.pdf(bins, loc=mu, scale=sigma))
# plt.show()

#散布図
from scipy.stats import norm
(n,sigma, mu) = (300, 10, 50)
x = np.random.randn(n) * sigma + mu
y = np.random.randn(n) * sigma + mu
c = np.random.rand(n)
s = np.random.rand(n)**2 * np.pi * 100
plt.scatter(x, y, s=s, c=c, alpha=0.25)
plt.show()

#3Dグラフ
# from mpl_toolkits.mplot3d import Axes3D
# ax = plt.figure().add_subplot(projection='3d')
# x0 = np.arange(0, 5, 0.1)
# y0 = np.arange(0, 5, 0.1)
# (x, y) = np.meshgrid(x0, y0)
# z = np.sin(x * y)
# surf = ax.plot_surface(x, y, z, cmap='gray', antialiased=True)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# # Figureと3DAxeS
# fig = plt.figure(figsize = (8, 8))
# ax = fig.add_subplot(111, projection="3d")
# # 軸ラベルを設定
# ax.set_xlabel("x", size = 16)
# ax.set_ylabel("y", size = 16)
# ax.set_zlabel("z", size = 16)
# # 円周率の定義
# pi = np.pi
# # (x,y)データを作成
# x = np.linspace(-3*pi, 3*pi, 256)
# y = np.linspace(-3*pi, 3*pi, 256)
# # 格子点を作成
# X, Y = np.meshgrid(x, y)
# # 高度の計算式
# Z = np.cos(X/pi) * np.sin(Y/pi)
# # 曲面を描画
# ax.plot_surface(X, Y, Z, cmap = "summer")
# # 底面に等高線を描画
# ax.contour(X, Y, Z, colors = "black", offset = -1)
# plt.show()