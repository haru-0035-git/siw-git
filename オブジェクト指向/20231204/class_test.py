class Cafe:
    count = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Cafe.count += 1
    def menu(self):
        print(f'{self.name}の値段は{self.price}円')
    @classmethod
    def getCount(cls):
        print(f'メニュー数は{cls.count}')
# cake = Cafe('ケーキセット',800)
# cake.menu()
# cake1 = Cafe('珈琲',450)
# cake1.menu()
# Cafe.getCount()

class Order(Cafe):
    count = 0
    def __init__(self, name, price):
        super().__init__(name, price)
        Order.count += 1
    def menu(self):
        print(f'{self.name}を注文した')
    @classmethod
    def getCount(cls):
        print(f'{cls.count}')

pr = Order('ケーキ',800)
pr.menu()
pr.getCount()
