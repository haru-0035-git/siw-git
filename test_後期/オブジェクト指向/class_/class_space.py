import time 
class Universe():
    def __init__(self,name):
        self.name = name
    def landing(self):
        print(f'{self.name} 着陸しました')
    def take_off(self):
        print(f'{self.name} 離陸しました')
        
ship1 = Universe('はやぶさ')
ship1.take_off()
time.sleep(2)
ship1.landing()