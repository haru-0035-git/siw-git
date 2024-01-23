import string
from random import choice
nums = string.digits
# nums = string.punctuation
# ・string.ascii_letters：大文字小文字のアルファベットを返す    
# ・string.punctuation：ascii に含まれる記号を返す
print(choice(nums)+choice(nums)+choice(nums)+choice(nums))