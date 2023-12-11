from random import randint
import time
class Hero():
    def __init__(self,name,hp,power,defence):
        self.name = name
        self.hp = hp
        self.power = power
        self.defence = defence
    def attack(self,enemy):
        enemy.hp -= self.power - enemy.defence
        print(f'{self.power - enemy.defence}減った')
        print(f'{enemy.name}のHPは{enemy.hp}')
    def mao_attack(self,enemy):
        enemy.hp -= self.power * 1.5 
        print(f'の魔法が炸裂')
        print(f'{enemy.name}のHPは{enemy.hp}')

hero = Hero('アフラ・マズダー',200,40,20)
mao = Hero('アンリマユ',200,30,20)

while True:
    mao_luck = randint(1,11)
    if mao_luck == 2 or mao_luck == 7 or mao_luck == 9:
        time.sleep(1)
        mao.mao_attack(hero)
        if hero.hp < 0:
            print('アフラ・マズダーの敗北')
            break
    else:
        mao.attack(hero)
        if hero.hp < 0:
            print('アフラ・マズダーの敗北')
            break
    hero.attack(mao)
    if mao.hp < 0:
        print('アンリマユの敗北')
        break