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
fig, ax = plt.subplots() 
ax.imshow(im_inverted, cmap='gray') 
plt.show()

