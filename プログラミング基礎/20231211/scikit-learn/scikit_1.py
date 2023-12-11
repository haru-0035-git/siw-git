#irisデータの読み込み
from sklearn.datasets import load_iris

iris = load_iris()
# print(iris.data.shape)
# print(iris.data[:10])
# print(iris.target_names)

#2種類のデータの準備
from sklearn.model_selection import train_test_split

(train_X, test_X, train_Y, test_Y) = train_test_split(iris.data, iris.target, test_size=0.2)
print(iris.target_names[test_Y])
# print(test_Y)
# print(test_X)


# K 近傍法
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()
model.fit(train_X, iris.target_names[train_Y])

#学習データを使った予測
from sklearn import metrics
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

pred = model.predict(test_X)
score = accuracy_score(iris.target_names[test_Y], pred)

# print('score:%s' % score)
# print(classification_report(iris.target_names[test_Y], pred))
# print(confusion_matrix(iris.target_names[test_Y], pred))


#ロジスティック回帰
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

model = LogisticRegression()
print(model)
model.fit(train_X, iris.target_names[train_Y])
pred = model.predict(test_X)
score = accuracy_score(iris.target_names[test_Y], pred)
print('score:%s' % score)
print(classification_report(iris.target_names[test_Y], pred))
print(confusion_matrix(iris.target_names[test_Y], pred))