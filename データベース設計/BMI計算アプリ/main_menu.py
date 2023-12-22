import sys
import os
sys.dont_write_bytecode = True
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from user import menu_users
print('################')
print(' BMI計算アプリ')
print('################')
print('')
print('=== メイン メニュー ===')

while True:
    print('1.ユーザ管理')
    print('2.体重管理')
    print('3.終了')
    judgment = input('メニューを選択してください:')
    if judgment == '1':
        menu_users.execute()
    elif judgment == '2':
        print('')
    elif judgment == '3':
        break
    else:
        print('1~3 のみ')
