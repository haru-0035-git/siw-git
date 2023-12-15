def select_all():
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
        print('★★★ユーザ表示★★★')
        while True:
            name = input('ユーザ名を入力してください:')
            rows = dbutil.find_by_name(cursor,name)
            if len(rows) == 1:
                break
            else:
                print('[Error] そのユーザ名は存在しません')
        rows = dbaccess_users.select_all(cursor,name)
        for row in rows:
            print(f'ユーザ名：{row["name"]}')
            print(f'生年月日：{row["birthday"]}')
            print(f'身長：{row["height"]}')
            print(f'目標体重：{row["target_weight"]}')


    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)
    finally:
        cursor.close()
        cnx.close()

if __name__ == '__main__':
    select_all()