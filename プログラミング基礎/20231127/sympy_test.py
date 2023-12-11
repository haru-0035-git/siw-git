from sympy import * 
import math 

# a  = 12 * 36
# print(a)
# b = sy.Rational(1,3) # Rational(分子,分母)
# print(b)
# print(a*b)

# 分数
# a1 = Rational(1,3)
# b1 = Rational(5,6)
# print(a1+b1)

# a2  = Rational(1,3)
# b2 = Rational(5,6)
# print(a2-b2)

#分数の累乗
# a3  = Rational(1,3)
# b3 = (a3+3) ** 2 -4
# print(b3)

#定数
# a=Rational(1,3)
# print(N(pi,30))
# print(N(E,20))
# print(N(oo, 30))
# a5 = sqrt(32)
# b4 = sqrt(24)
# pprint(a5*b4)

#平方根
# x = Symbol('x')
# res = x**2 +4*x -6
# print(res)
# res1 = (x+1)**2
# res2 = 2*x+7
# print(res1)
# print(res2)
# print(res1+res2)
# print(simplify(res1+res2))

# x = Symbol('x')
# re = (x+2)**3
# print(expand(re))

# x = Symbol('x')
# re1 = x**3-x**2-x+1
# re2 = 4*x**2 - 1
# re3 = 2*x**2 + 10*x +12
# re4 = x**3 - 7*x**2 - 8*x
# re5 = (x+1)**2 -16
# print(factor(re1))
# print(factor(re2))
# print(factor(re3))
# print(factor(re4))
# print(factor(re5))

# x,y=symbols('x y')
# re=x**2-2*y
# print(re)
# print(re.subs([(x,10),(y,20)]))

# x=Symbol('x')
# re=x**2+2*x-8
# print(re)
# print(solve(re))

# (x,y)=symbols('x y')
# re=(x+y)**2-9
# print(re)
# print(solve(re))
# print('x=%s' % solve(re,x))
# print('y=%s' % solve(re,y))

# (x,y)=symbols('x y')
# re1=2*x+6*y+4
# re2=(x+y)**2-9
# print(solve((re1,re2)))

# (x,y)=symbols('x y')
# re1=sqrt(2)*x+sqrt(3)*y-1
# re2=sqrt(3)*x+sqrt(2)*y-1
# pprint(solve((re1,re2)))

# (x,y)=symbols('x y')
# re1=Eq(y, x**2+6*x+2)
# re2=Eq(y, (x+2)**2)
# print(re1)
# print(re2)
# print(solve((re1,re2)))

x  = Symbol('x')
# y = sin(x)/x
# lim_y = limit(y, x, 0)
# print(lim_y)
# p = plot(y, (x, -12, 12), ylabel="y")

# y = x * sin(1/x)
# lim_y = limit(y, x, 0)
# print(lim_y)
# p = plot(y, (x, -0.1, 0.1), ylabel = "y", line_color="red")

# (x,y)=symbols('x y')
# re=2*x**3
# print(diff(re,x))
# print(limit((2*(x+y)**3-2*x**3)/y,y,0))
# print(diff(re,x,2))
# print(limit((6*(x+y)**2-6*x**2)/y,y,0))

# print(expand(2*(x+y)**3-2*x**3))

# x=Symbol('x')
# re=2*x**3
# print(integrate(re,x))
# print(integrate(re, (x,0,1)))

# import matplotlib.pyplot as plt
# import numpy as np
# from sympy import Symbol
# # シンボル x を定義
# x = Symbol('x')
# re = 2 * x**3
# # SymPy の式を NumPy の関数に変換
# re_np = lambdify(x, re, 'numpy')
# # x の値を生成
# x_values = np.linspace(-2, 2, 400)
# y_values = re_np(x_values)
# # グラフを描画
# plt.plot(x_values, y_values, label='2x^3')
# plt.title('Graph of 2x^3')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.grid(True)
# plt.show()