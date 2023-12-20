def execute():
    import sys
    sys.dont_write_bytecode = True
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from db import dbaccess_users
    from user import create_user
    from user import select_all
    from user import updata_weight
    
    print('===ユーザ管理メニュー===')
    print('1.ユーザ登録')
    print('2.ユーザ表示')
    print('3.身長更新')
    print('4.目標体重更新')
    print('5.ユーザ削除')
    print('6.終了')
    while True:
        judgment = input('メニューを選択してください：')
        if judgment == '1':
            create_user.add_user()
        elif judgment == '2':
            select_all.select_all()
        elif judgment == '3':
            updata_weight.update_weight()
        elif judgment == '4':
            select_all.select_all()
        elif judgment == '5':
            select_all.select_all()
        else:
            break
        


if __name__ == '__main__':
    execute()