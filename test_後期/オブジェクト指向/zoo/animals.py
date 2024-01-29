class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(f'{self.name} is crying')
    def sleep(self):
        print(f'{self.name} is sleeping')

class Lion(Animal):
    def roar(self):
        print(f'{self.name} is roaring')

class Elephant(Animal):
    def trumpet(self):
        print(f'{self.name} is trumpeting')

class Monkey(Animal):
    def climb(self):
        print(f'{self.name} is climbing')