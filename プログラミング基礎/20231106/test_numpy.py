import numpy as np

# arr = np.array([10,20,30])
# print(arr)

# arr0 = np.zeros(5)
# arr1 = np.ones(5)
# print(arr0)
# print(arr1)

# #等差数列
# arr3 = np.arange(0,100,20)
# arr4 = np.linspace(0,100,5)
# print(arr3)
# print(arr4)

#等比数列

# arr5 = np.geomspace(1,10000,5,dtype=np.int64)
# print(arr5)

#ベクトルの計算
# arr6 = np.array([1,2,3,5,8])
# print(arr6 + 10)

#ベクトル同士の演算
# arr7 = np.array([1,2,3,5,8])
# arr8 = np.array([8,13,21,34])
# print(arr7 * arr8)
# print(arr7 / arr8)

# ベクトルの結合
# arr9 = np.array([1,2,3])
# arr10 = np.array([4,5,6])
# arr11 = arr9 + arr10  # 垂直に結合
# arr12 = np.ravel([arr9,arr10]) #並列に結合
# print(arr11)
# print(arr12)

arr_1 = np.array(np.random.randint(0,100,(10,10)))
print(arr_1)
print(f'平均{np.mean(arr_1)}')
print(f'中央値{np.median(arr_1)}')
print(f'分散{np.var(arr_1)}')
print(f'標準偏差{np.std(arr_1)}')