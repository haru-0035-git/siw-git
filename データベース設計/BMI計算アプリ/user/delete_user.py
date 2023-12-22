def delete_user():
    import sys
    import os
    sys.dont_write_bytecode = True
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import mysql.connector
    from util import dbutil
    from util import inpututil
    from db   import dbaccess_user

    cnx = dbutil.connect()
    try:
        cursor = cnx.cursor(dictionary=True)
        print('★★★ユーザ削除★★★')
        while True:
            name = input('ユーザ名を入力してください : ')
            rows = dbutil.find_by_name(cursor,name)
            if len(rows) == 1:
                break
            else:
                print('[Error] そのユーザ名は存在しません')
        rows = dbaccess_user.select_all(cursor,name)
        for row in rows:
            print(f'ユーザ名：{row["name"]}')
            print(f'生年月日：{row["birthday"]}')
            print(f'身長：{row["height"]}')
            print(f'目標体重：{row["target_weight"]}')
##############################################################################
        juge = input('このデータを全て削除してもよろしいですか? (y/n)>>')
        if juge.lower() == 'y':   
            dbaccess_user.delete_user(cursor,name)
            cnx.commit()
            print('削除しました')
        elif juge.lower() == 'n':
            return None
        else:
            print('y/n のみで')
    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)
    finally:
        cursor.close()
        cnx.close()

if __name__ == '__main__':
    delete_user()