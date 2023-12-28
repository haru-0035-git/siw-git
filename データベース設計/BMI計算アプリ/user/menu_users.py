def execute():
    import sys
    sys.dont_write_bytecode = True
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from db   import dbaccess_user
    from user import create_user
    from user import select_user
    from user import updata_targetweight
    from user import updata_height
    from user import delete_user
    
    print('===ユーザ管理メニュー===')
    while True:
        print('1.ユーザ登録')
        print('2.ユーザ表示')
        print('3.身長更新')
        print('4.目標体重更新')
        print('5.ユーザ削除')
        print('6.終了')
        judgment = input('メニューを選択してください：')
        if judgment == '1':
            create_user.add_user()
        elif judgment == '2':
            select_user.select_allditail()
        elif judgment == '3':
            updata_height.update_height()
        elif judgment == '4':
            updata_targetweight.update_target()
        elif judgment == '5':
            delete_user.delete_user()
        elif judgment == '6':
            break
        else:
            print('1~6まで')
            continue
        


if __name__ == '__main__':
    execute()