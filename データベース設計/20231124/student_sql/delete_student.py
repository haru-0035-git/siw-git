def execute():
    #
    #学生削除プログラム
    #studentテーブルにキーボードで入力した条件で情報を更新する
    #

    import sys
    sys.dont_write_bytecode = True
    import mysql.connector
    from util import dbutil
    from util import inpututil

    #
    #1)初期処理
    #
    #MySQLに接続

    cnx = dbutil.connect()

    try:
        #カーソルを作成
        cursor = cnx.cursor(dictionary=True)
        #
        #2)キーボードから入力
        #
        print('学生削除')
        while True:
            student_id = inpututil.input_int('IDを入力してください>>')
            rows = dbutil.find_by_id_student(cursor,student_id)
            if len(rows) == 0:
                print(f'ID={student_id}は存在しません')
                continue
            while True:
                judgment = input('削除しますか？ y/n>>')
                if judgment.lower() == 'y':
                    break
                elif judgment.lower() == 'n':
                    print('終了しました')
                    return None
                else:
                    print('Y/nのみ')
                    continue
            break
        #
        #3) 検索SQLを作成
        #
        #後から設定したい値は%sに置き換える
        sql = 'delete from student where id = %s'
        #設定したい値はリストにする
        data = [student_id]

        #
        #4)SQL実行
        #

        
        #SQLを実行する(SQLの文字列、値のリスト)
        cursor.execute(sql, data)

        #
        #5)結果を表示
        #
        cnx.commit()
        print(f'ID={student_id}を削除しました')
    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)


    #
    #5)終了処理
    #

    finally:
        cursor.close()
        cnx.close()