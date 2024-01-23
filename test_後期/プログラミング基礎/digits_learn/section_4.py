from sklearn import metrics 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report 
from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier 
digits = load_digits() 
(train_X, test_X, train_Y, test_Y) = train_test_split(digits.data,digits.target, test_size=0.2, random_state=0)
model = KNeighborsClassifier() 
model.fit(train_X, train_Y) 

#KNeighborsClassifierで予測
pred = model.predict(test_X) 
score = accuracy_score(test_Y, pred) 
print('score:%s' % score)  


#予測の結果
print(pred[:20]) 
print(test_Y[:20]) 
print(classification_report(test_Y, pred)) 
print(confusion_matrix(test_Y, pred)) 