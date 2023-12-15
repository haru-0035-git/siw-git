def add_user():
    import sys
    import os
    sys.dont_write_bytecode = True
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import mysql.connector
    from util import dbutil
    from util import inpututil
    from db   import dbaccess_users

    cnx = dbutil.connect()
    try:
        cursor = cnx.cursor(dictionary=True)
        print('★★★ユーザ登録★★★')
        while True:
            name = input('ユーザ名を入力してください : ')
            rows = dbutil.find_by_name(cursor,name)
            if len(rows) == 0:
                break
            else:
                print('[Error] そのユーザ名はすでに存在します')
        birthday = inpututil.input_date('生年月日を入力してください [%Y-%m-%d] : ')
        weight = inpututil.input_float('身長を入力してください (cm) : ')
        target_weight = inpututil.input_float('目標の体重を入力してください(kg) : ')
        dbaccess_users.add_user(cursor,name,birthday,weight,target_weight)
        cnx.commit()
        print('ユーザーを登録しました')
    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)
    finally:
        cursor.close()
        cnx.close()

if __name__ == '__main__':
    add_user()