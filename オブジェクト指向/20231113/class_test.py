class Hero:
    name = '松田'
    hp = 100
    hung = 100
    def sleep(self,hours):
        print(f'{self.name}は{hours}時間寝た!')
        self.hp += hours
    def power(self,power):
        print(f'{self.name}は{power}パワー消費した')
        self.hung -= power
        print(f'今の{self.name}の満腹度は{self.hung}')


print('')
h = Hero()
h.sleep(3)
h.power(5)
print(f'{h.hp}')
print(f'{h.hung}')