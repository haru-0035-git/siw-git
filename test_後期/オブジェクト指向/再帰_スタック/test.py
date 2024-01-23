# # 固定長スタックStackの利用例

# from enum import Enum
# from stack import Stack

# Menu = Enum('Menu', ['プッシュ', 'ポップ', 'ピーク', '探索', 'ダンプ', '終了'])

# def select_menu() -> Menu:
#     """メニュー選択"""
#     s = [f'({m.value}){m.name}' for m in Menu]
#     while True:
#         print(*s, sep='  ', end='')
#         n = int(input('：'))
#         if 1 <= n <= len(Menu):
#             return Menu(n)

# s = Stack(64)      # 最大64個プッシュできるスタック

# while True:
#     print(f'現在のデータ数：{len(s)} / {s.capacity}')
#     menu = select_menu()                            # メニュー選択

#     if menu == Menu.プッシュ:                       # プッシュ
#         x = int(input('データ：'))
#         try:
#             s.push(x)
#         except IndexError:
#             print('スタックが満杯です。')

#     elif menu == Menu.ポップ:                       # ポップ
#         try:
#             x = s.pop()
#             print(f'ポップしたデータは{x}です。')
#         except IndexError:
#             print('スタックが空です。')

#     elif menu == Menu.ピーク:                       # ピーク
#         try:
#             x = s.peek()
#             print(f'ビークしたデータは{x}です。')
#         except IndexError:
#             print('スタックが空です。')

#     elif menu == Menu.探索:                         # 探索
#         x = int(input('値：'))
#         if x in s:
#             print(f'{s.count(x)}個含まれ先頭の位置は{s.find(x)}です。')
#         else:
#             print('その値は含まれません。')
#     elif menu == Menu.ダンプ:                       # ダンプ
#         s.dump()

#     else:
#         break

def move(no: int, x: int, y: int) -> None:
    """no枚の円盤をx軸からy軸へ移動"""
    if no > 1:
        move(no - 1, x, 6 - x - y)

    print(f'円盤[{no}]を{x}軸から{y}軸へ移動')

    if no > 1:
        move(no - 1, 6 - x - y, y)

print('ハノイの塔')
n = int(input('円盤の枚数：'))

move(n, 1, 3)   # 第1軸に積まれたn枚を第3軸に移動