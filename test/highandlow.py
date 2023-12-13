from random import randint
class Card:
    def __init__(self):
        self.rank = randint(0,12)
    def card(self):
        ranks = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        return ranks[self.rank]


j = 0
d = 0
p = 0
while j < 10:   
    player1 = Card()
    dealer = player1.card()
    player2 = Card()
    player = player2.card()

    while True:
        print('*************')
        print(f'    {dealer}')
        print('*************')
        r = (input('high and low? h/l >>'))
        if r == 'h':
            break
        elif r == 'l':
            break
        else:
            print('h or l')
            continue

    print('*************')
    print(f'    {player}')
    print('*************')

    if dealer == 'A':
        dealer = 1
    elif dealer == 'J':
        dealer = 11
    elif dealer == 'Q':
        dealer = 12
    elif dealer == 'K':
        dealer = 13

    if player == 'A':
        player = 1
    elif player == 'J':
        player = 11
    elif player == 'Q':
        player = 12
    elif player == 'K':
        player = 13



    if dealer < player and r == 'h':
        print('プレイヤーの勝ち')
        p += 1
    elif dealer > player and r == 'h':
        print('プレイヤーの負け')
        d += 1
    if dealer > player and r == 'l':
        print('プレイヤーの勝ち')
        p += 1
    elif dealer < player and r == 'l':
        print('プレイヤーの負け')
        d += 1
    if dealer == player:
        print('DROW')
    
    j += 1

print(f'プレイヤーの勝利数は{p}回')
print(f'ディーラーの勝利数は{d}回')
if p > d:
    print('プレイヤーの勝利！')
else:
    print('ディーラーの勝利')