from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_digits
digits = load_digits() 
(train_X, test_X, train_Y, test_Y) = train_test_split(digits.data,digits.target, test_size=0.2, random_state=0)
 #データを割り振る
print(train_X)
print(test_X)


print(train_Y)
print(test_Y)