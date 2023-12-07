def execute():
    #
    #学生ID検索プログラム
    #examテーブルからキーボードで入力したIDを条件にレコ―ドを取得して表示
    #
    import sys
    sys.dont_write_bytecode = True
    import os
    import mysql.connector
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from util import inpututil
    from db import dbaccess_student
    from util import dbutil
    #
    #1)初期処理
    #MySQLに接続

    cnx = dbutil.connect()

    try:
        #カーソルを作成
        cursor = cnx.cursor(dictionary=True)
        #
        #2)キーボードから入力
        #
        while True:    
            id = inpututil.input_int('IDを入力してください>>')
            rows = dbaccess_student.find_by_id_student(cursor,id)
            if len(rows) == 0:
                print(f'ID={id}は存在しません')
                continue
            break


            


        #
        #4)取得したレコードを全て表示
        #
        rows = dbaccess_student.find_by_id_student(cursor,id)
        for row in rows:
            print(f'{row["id"]}:{row["name"]}:{row["class"]}')
            
    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)


    #
    #5)終了処理
    #

    finally:
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    execute()