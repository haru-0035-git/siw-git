from sklearn.datasets import load_digits 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression 
import numpy as np 
from PIL import Image, ImageEnhance, ImageOps 
import matplotlib.pyplot as plt  
import os

# 手書き数字データセットの読み込み 
digits = load_digits()  # 訓練データとテストデータの分割 
(train_X, test_X, train_Y, test_Y) = train_test_split(digits.data, digits.target, test_size=0.2, random_state=0)  

# LogisticRegression モデルの訓練 
clf = LogisticRegression(random_state=0, solver='liblinear', multi_class='auto') 
clf.fit(train_X, train_Y)  

# 新しい画像 'digi.jpeg' の読み込み 
im = Image.open(f'{os.path.dirname(__file__)}/無題.jpeg')  

# 画像の前処理 # 明るさの調整、グレースケール変換、リサイズ、色反転 
im_enhanced = ImageEnhance.Brightness(im).enhance(2.0) 
im_gray = im_enhanced.convert(mode='L') 
im_88 = im_gray.resize((8, 8)) 
im_inverted = ImageOps.invert(im_88)  

# 画像データを配列に変換し、適切な形状に変更 
x_im2d = np.asarray(im_inverted) 
X_im1d = x_im2d.reshape(-1) 
X_multiplied = X_im1d * (16 / 255)  
clf.predict([X_multiplied])[0] 

# 画像データに対する予測 
prediction = clf.predict([X_multiplied])[0] 
print("Predicted label:", prediction)