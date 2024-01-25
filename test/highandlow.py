from random import randint

class Deck:
    RANKS = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    def __init__(self):
        self.dealer_rank = randint(0, 12)
        self.player_rank = randint(0, 12)

    def get_dealer_card(self):
        return self.RANKS[self.dealer_rank]

    def get_player_card(self):
        return self.RANKS[self.player_rank]

def convert_rank(card):
    if card == 'A':
        return 1
    elif card == 'J':
        return 11
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    else:
        return card

def compare_cards(dealer, player, user_guess):
    dealer = convert_rank(dealer)
    player = convert_rank(player)

    if dealer < player and user_guess == 'h':
        return 'プレイヤーの勝ち'
    elif dealer > player and user_guess == 'h':
        return 'プレイヤーの負け'
    if dealer > player and user_guess == 'l':
        return 'プレイヤーの勝ち'
    elif dealer < player and user_guess == 'l':
        return 'プレイヤーの負け'
    if dealer == player:
        return 'DROW'

j = 0
d = 0
p = 0

while j < 10:
    deck = Deck()
    dealer = deck.get_dealer_card()
    player = deck.get_player_card()

    while True:
        print('*************')
        print(f'    {dealer}')
        print('*************')
        user_guess = input('high and low? h/l >>')

        if user_guess == 'h' or user_guess == 'l':
            break
        else:
            print('h or l')
            continue

    print('*************')
    print(f'    {player}')
    print('*************')

    result = compare_cards(dealer, player, user_guess)
    print(result)

    if '勝ち' in result:
        p += 1
    elif '負け' in result:
        d += 1

    j += 1

print(f'プレイヤーの勝利数は{p}回')
print(f'ディーラーの勝利数は{d}回')

if p > d:
    print('プレイヤーの勝利！')
else:
    print('ディーラーの勝利')
