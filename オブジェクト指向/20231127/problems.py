class Robot:
    def __init__(self,name,power):
        self.name = name
        self.power =power
    def robo(self):
        print(f'名前は{self.name}:パワーは{self.power}')

class Machine(Robot):
    def __init__(self, name, power,work):
        super().__init__(name, power)
        self.work = work
    def robo(self):
        print(f'名前は{self.name}パワーは{self.power}仕事は{self.work}')
rb1 = Robot('やわらか戦車',1)
rb1.robo()

rb2 = Robot('ガンダム',1000)
rb2.robo()

rb3 = Machine('R2-D2',100,50)
rb3.robo()