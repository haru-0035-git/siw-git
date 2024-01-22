from PIL import Image, ImageEnhance 
import matplotlib.pyplot as plt
import os
from PIL import ImageEnhance 

#文字をグレースケール化
im = Image.open(f'{os.path.dirname(__file__)}/aaa.jpeg')  
enhancer = ImageEnhance.Brightness(im) 
im_enhanced = ImageEnhance.Brightness(im).enhance(2.0) 
im_gray = im_enhanced.convert(mode='L')
im_88 = im_gray.resize((8, 8))
fig, ax = plt.subplots() 
ax.imshow(im_88, cmap='gray')
plt.show()



