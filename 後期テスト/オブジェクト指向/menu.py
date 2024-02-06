class Menu:
    def __init__(self,number):
        self.number = number
    def menu(self):
        print(f'{self.number}番が注文されました')

class Omurais(Menu):
    def attend_omu(self):
        print(f'{self.number}番のオムライスが注文されました')

class Sterk(Menu):
    def attend_ste(self):
        print(f'{self.number}番のステーキが注文されました')

class Hanbarg(Menu):
    def attend_hun(self):
        print(f'{self.number}番のハンバーグが注文されました')