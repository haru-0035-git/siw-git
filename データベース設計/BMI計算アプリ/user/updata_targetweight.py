def update_target():
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
        print('★★★目標体重更新★★★')
        while True:
            name = input('ユーザ名を入力してください : ')
            rows = dbutil.find_by_name(cursor,name)
            if len(rows) == 1:
                break
            else:
                print('[Error] そのユーザ名は存在しません')
        weight = inpututil.input_float('目標体重を入力してください (cm) : ')
        dbaccess_user.updata_targetweight(cursor,name,weight)
        cnx.commit()
        print('ユーザーの目標体重を更新しました')
    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)
    finally:
        cursor.close()
        cnx.close()

if __name__ == '__main__':
    update_target()