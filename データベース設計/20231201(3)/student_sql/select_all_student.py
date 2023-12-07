def execute():
    #
    #学生表示プログラム
    #studentテーブルからすべてのレコ―ドを取得して表示
    #
    import sys
    sys.dont_write_bytecode = True
    import  os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import mysql.connector
    from util import dbutil
    from db import dbaccess_student

    #
    #1)初期処理
    #
    #MySQLに接続

    cnx = dbutil.connect()

    #コネクションが切れたときに再接続する
    cnx.ping(reconnect=True)



    #
    #3)SQL実行
    #

    try:
        #カーソルを作成
        cursor = cnx.cursor(dictionary=True)
        
        rows = dbaccess_student.select_all(cursor,id)
        for row in rows:
            print(f'{row["id"]}:{row["name"]}')

    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)


    #
    #5)終了処理
    #

    finally:
        cursor.close()
        cnx.close()


if __name__ == '__main__':
    execute()