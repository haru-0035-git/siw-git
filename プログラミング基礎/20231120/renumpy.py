import numpy as np
import os
mount = np.loadtxt(f'{os.path.dirname(__file__)}\Mountain.csv',delimiter=',')
print(f'世界の山トップ10の平均は{np.mean(mount[:,0])}m')
print(f'日本の山トップ10の平均は{np.mean(mount[:,1])}m')
print(f'世界で一番高い山の標高は{np.max(mount[:,0])}m')
print(f'日本で一番高い山の標高は{np.max(mount[:,0])}m')
# print(score)