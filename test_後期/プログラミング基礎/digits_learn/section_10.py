from PIL import Image, ImageEnhance 
import matplotlib.pyplot as plt
import os
from PIL import ImageEnhance ,ImageOps

#明暗を反転
im = Image.open(f'{os.path.dirname(__file__)}/aaa.jpeg') 
im_enhanced = ImageEnhance.Brightness(im).enhance(2.0)  
im_gray = im_enhanced.convert(mode='L') 
im_88 = im_gray.resize((8, 8)) 
im_inverted = ImageOps.invert(im_88) 

import numpy 
x_im2d = numpy.asarray(im_inverted)  #変換

#一次元のデータに変換
X_im1d = x_im2d.reshape(-1) 

X_multiplied = X_im1d * (16/ 255)
print(X_multiplied)