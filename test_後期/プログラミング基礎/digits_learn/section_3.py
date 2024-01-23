from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier 
digits = load_digits() 
(train_X, test_X, train_Y, test_Y) = train_test_split(digits.data,digits.target, test_size=0.2, random_state=0)
#K近傍法
model = KNeighborsClassifier() 
model.fit(train_X, train_Y) 
print(model)