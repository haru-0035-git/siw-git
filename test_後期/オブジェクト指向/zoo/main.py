from animals import *
from zoo import Zoo
zoo = Zoo()
zoo.add_animals(Lion("Leo",4))
zoo.add_animals(Elephant("Ella",10))
zoo.add_animals(Monkey("miko",3))

zoo.show_animals()
leo = zoo.animals[0]
leo.roar()

ella = zoo.animals[1]
ella.trumpet()

miko = zoo.animals[2]
miko.climb()