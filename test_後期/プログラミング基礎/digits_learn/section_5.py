from sklearn import metrics 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report 
from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier 
from matplotlib import pyplot as plt
digits = load_digits() 
(train_X, test_X, train_Y, test_Y) = train_test_split(digits.data,digits.target, test_size=0.2, random_state=0)
model = KNeighborsClassifier() 
model.fit(train_X, train_Y) 
pred = model.predict(test_X) 
score = accuracy_score(test_Y, pred) 

print(train_X) 
index = 1000
X0=train_X[index] #データ
print(train_Y[index])   #答え
X0_square = X0.reshape(8,8) 
X0_square  
X0_square.shape
fig, ax = plt.subplots() 
ax.imshow(X0_square, cmap='binary')
plt.show()