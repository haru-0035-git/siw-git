from PIL import Image
from PIL import ImageFilter
import os
# img = Image.open(f'{os.path.dirname(__file__)}\\aaa.jpg')

# # img.save('aaa1.png') #名称や形式を変えられる
#エラー処理
try :
    img = Image.open(f'{os.path.dirname(__file__)}\\aaa.jpg')
except IOError:
    print("Cant't Open File!")
    exit()
img.show()

# #サイズ変更
# (w,h) = img.size
# img2 = img.resize((w * 2,h * 2)) #,resample = Image.NEAREST)
# img2.show()

# img2 = img.resize((500,500))
# img2.show()

#イメージの回転
# img2 = img.rotate(45,expand=True)
# img2.show()

#イメージの反転
# img2 = img.transpose(Image.FLIP_TOP_BOTTOM)
# img2.show()

#RGB ,グレースケースの変換
# img2 = img.filter(ImageFilter.BLUR)
# img2.show()

#ブラー処理
# img2 = img.filter(ImageFilter.SMOOTH)
# img2.show()

#ブラーの強度を値で変えられる
# img2 = img.filter(ImageFilter.GaussianBlur(100,0))
# img2.show()
# img2 = img.filter(ImageFilter.BoxBlur(radius=10))
# img2.show()


#アンシャープマスク
# img2 = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
# img2.show()

#輝度調整
# img2 = img.point(lambda x:x*2)
# img2.show()

#リストによる輝度調節
# (w, h) = img.size
# img2 = img.point(list(range(256, 0, -1)) + list([255] * 256) + list(range(256, 0, -1)))
# img2.show()

#UnsharpMask
# img2 = img.filter(ImageFilter.UnsharpMask(radius=20,percent=1500,threshold=3))
# img2.show()

#kernel
# my_kernel =[1,5,0,1,5,-9,1,5,-10]
# img2 = img.filter(ImageFilter.Kernel(size=(3,3),kernel=my_kernel,scale=None,offset=0))
# img2.show()

#MedianFilter
# img2 = img.filter(ImageFilter.MedianFilter(size=21))
# img2.show()

#イメージを重ねる
# (w, h) = img.size
# img2 = img.resize((w // 3, h // 3))
# img.paste(img2, (0, h // 3 * 2))
# img.paste(img2, (w // 3, h // 3))
# img.paste(img2, (w // 3 * 2, 0))
# img.show()