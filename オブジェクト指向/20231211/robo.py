class Robot:
    def __init__(self):
        self.a = 0
        self.b = 0
    def walk(self):
        while True:
            try:
                x = input('xにいくつ動くか(右がプラス)>>')
                x = int(x)
                break
            except :
                print('整数で入力してください')
        while True:
            try:
                y = input('yにいくつ動くか(前進がプラス)>>')
                y = int(y)
                break
            except :
                print('整数で入力してください')
        print(f'xに{x}歩、yに{y}歩進んだ')
        self.a = self.a + x +5
        self.b = self.b + y
    def sum_walk(self):
        print(f'現在の座標はx:{self.a}、y:{self.b}')

robo1 = Robot()
robo1.walk()
robo1.sum_walk()



class Battery(Robot):
    def __init__(self,hp = 100):
        super().__init__()
        self.battery = hp
    def batte(self):
        battery = self.a + self.b
        self.battery -= battery
        print(f'現在の充電残量は{self.hp}')

robo2 = Battery()
robo2.walk()
robo2.sum_walk()
robo2.batte()


# class BatteryRobot(Robot):
#     def __init__(self, initial_battery=100):
#         super().__init__()
#         self.battery = initial_battery

#     def walk(self):
#         super().walk()  # 親クラスのwalkメソッドを呼び出し

#         distance = abs(self.a) + abs(self.b)
#         energy_consumed = distance  # 単純な例として、移動した距離分だけバッテリーを消費

#         if energy_consumed > self.battery:
#             print('バッテリーが足りません。')
#         else:
#             self.battery -= energy_consumed
#             print(f'バッテリー残量: {self.battery}')


# # 使用例
# battery_robot = BatteryRobot()

# # バッテリー残量を考慮して歩かせる
# battery_robot.walk()

# # 現在の座標とバッテリー残量を表示
# battery_robot.sum_walk()





        

