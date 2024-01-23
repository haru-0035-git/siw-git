from sklearn.linear_model import LogisticRegression 
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
clf = LogisticRegression(random_state=0, solver='liblinear', multi_class='auto')

clf.fit(train_X,train_Y) 

