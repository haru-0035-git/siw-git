from animals import *
class Zoo:
    def __init__(self):
        self.animals = []
    def add_animals(self,animal):
        self.animals.append(animal)
    def show_animals(self):
        for animal in self.animals:
            print(f'{animal.name}, a {animal.__class__.__name__}')
