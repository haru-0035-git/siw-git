class Person:
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.count += 1
    def getName(self): #メソッドを定義
        return self.name #データー属性を表すにはselfをつける
    def getAge(self):
        return self.age
    @classmethod
    def getCount(cls):
        return cls.count
    


pr1=Person('鈴木',23) #インスタンスの作成
print(f'{Person.getCount()}人目')
print(pr1.getName(),"さんは", pr1.getAge(), "才です。")
pr2=Person('田中',38) #インスタンスの作成
print(f'{pr2.getCount()}人目')
print(pr2.getName(),"さんは", pr2.getAge(), "才です。")