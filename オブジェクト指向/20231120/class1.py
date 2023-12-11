# class Volume:
#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#     def content(self):
#         return self.width*self.height*self.depth
#     def tri(self):
#         return (self.width*self.height)/2
# class Cube(Volume):
#     def __init__(self,length):
#         self.width = self.height = self.depth = length
# c = Cube(20)
# print(c.content())
    
# abc1 = Volume(10,20,30)
# print(abc1.content())

# abc2=Volume(50, 60, 70)
# print(abc2.content())

# print(abc1.height)
# print(abc2.height)
# abc1.height=50
# print(abc1.content())

# class Square:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width*self.height
    # def tri(self):
    #     return (self.width*self.height)/2
# abc3 = Square(20,10)
# print(abc3.area())
# abc4 = Square(20,10)
# print(abc4.tri())

# class Food:
#     def __init__(self, name, price):
#         self.__name = name
#         self.__price = price
#     def show(self):
#         print(self.__name, self.__price)
# x = Food('milk', 150)
# x._Food__price //= 2
# x.show()

class Volume:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
    def content(self):
        return self.width*self.height*self.depth
    def tri(self):
        return (self.width*self.height)/2
class Cube(Volume):
    def __init__(self,length):
        self.width = self.height = self.depth = length
    def tri(self):
        return (self.width*self.height)
c = Cube(20)
print(c.tri())