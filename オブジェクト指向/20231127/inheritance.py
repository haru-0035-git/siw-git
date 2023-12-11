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


class Customer(Person):       #派生クラスを定義
    def __init__(self, nm, ag, ad, tl):    #派生クラスのコンストラクタ
        super().__init__(nm, ag)      #基底クラスを初期化するためコンストラクタ
        self.adr = ad      #追加するデータ属性
        self.tel = tl
    def getName(self):       #基底クラスのメソッドを上書きする
        self.name = "顧客：" + self.name
        return self.name
    def getAdr(self):
        return self.adr       #追加するメソッド
    def getTel(self):
        return self.tel      #追加するメソッド
    
cu = Customer('鈴木',23,'aaa@gmail.com','xxx-xxxx-xxxx')
print(f'{cu.getName()}:{cu.getAge()}:{cu.getAdr()}:{cu.getTel()}')