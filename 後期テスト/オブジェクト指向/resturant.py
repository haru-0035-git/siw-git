import sys
sys.dont_write_bytecode = True
from menu import Menu,Omurais,Hanbarg,Sterk
class Cooking:
    def __init__(self):
        self.menus = []
    def add_menu(self,menu):
        self.menus.append(menu)
        
        