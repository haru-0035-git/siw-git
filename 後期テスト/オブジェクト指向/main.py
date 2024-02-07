import sys
sys.dont_write_bytecode = True
from menu import Menu,Omurais,Hanbarg,Sterk
from resturant import Cooking
import time
cook = Cooking()
menu_list = []
while True:
    print('1 : オムライス')
    print('2 : ステーキ')
    print('3 : ハンバーグ')
    print('4 : 終了')
    choice = input('から選んでください : ')
    if choice == '1': 
        menu_list.append(choice)
        cook.add_menu(Omurais(1))
    elif choice == '2' :
        menu_list.append(choice)
        cook.add_menu(Sterk(2))
    elif choice == '3':
        menu_list.append(choice)
        cook.add_menu(Hanbarg(3))
    elif choice == '4':
        break
    else:
        print('1~4から選んでください')

for i in range(len(menu_list)):
    if menu_list[i] == '1':
        print(' ')
        cooking1 = cook.menus[i]
        cooking1.attend_omu()
        print(' ')
    elif menu_list[i] == '2':
        print(' ')
        cooking2 = cook.menus[i]
        cooking2.attend_ste()
        print(' ')
    elif menu_list[i] == '3':
        print(' ')
        cooking3 = cook.menus[i]
        cooking3.attend_hun()
        print(' ')

if len(menu_list) == 0:
    print('注文がキャンセルされました')
else:
    time.sleep(3)
    print('料理が完成しました')

# from menu import Menu,Omurais,Hanbarg,Sterk
# from resturant import Cooking
# cook = Cooking()
# menu_list = []
# while True:
#     print('1 : オムライス')
#     print('2 : ステーキ')
#     print('3 : ハンバーグ')
#     print('4 : 終了')
#     choice = input('から選んでください : ')
#     if choice == '4':
#         break
#     elif choice == '1' or choice == '2' or choice == '3':
#         menu_list.append(choice)
#     else:
#         print('1~4から選んでください')

# for i in range(len(menu_list)):
#     if menu_list[i] == '1':
#         print(' ')
#         cook.add_menu(Omurais(1))
#         cooking1 = cook.menus[i]
#         cooking1.attend_omu()
#         print(' ')
#     elif menu_list[i] == '2':
#         print(' ')
#         cook.add_menu(Sterk(2))
#         cooking2 = cook.menus[i]
#         cooking2.attend_ste()
#         print(' ')
#     elif menu_list[i] == '3':
#         print(' ')
#         cook.add_menu(Hanbarg(3))
#         cooking3 = cook.menus[i]
#         cooking3.attend_hun()
#         print(' ')

# if len(menu_list) == 0:
#     print('注文がキャンセルされました')
# else:
#     print('調理が完成しました')
