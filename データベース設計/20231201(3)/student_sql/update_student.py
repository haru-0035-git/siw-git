def execute():
    #
    #学生登録プログラム
    #studentテーブルにキーボードで入力した条件で情報を更新する
    #

    import sys
    sys.dont_write_bytecode = True
    import mysql.connector
    from util import dbutil
    from util import inpututil
    import sys

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
        print('学生更新')
        while True:
            student_id = inpututil.input_int('IDを入力してください>>')
            rows = dbutil.find_by_id_student(cursor,student_id)
            if len(rows) == 1:
                break
            print(f'ID={student_id}は存在しません')
        student_name = input('氏名を入力してください>>')
        student_birthday = inpututil.input_date('生年月日を入力してください>>')
        student_class = input('クラスを入力してください>>')
        while True    :
            judgment = input(f'{student_id}:{student_name}:{student_birthday}:{student_class}に更新しますか？ y/n>>')
            if judgment.lower() == 'y':
                break
            elif judgment.lower() == 'n':
                print('終了しました')
                return None
            else:
                print('y/nのみ')
                continue

        #
        #3) 検索SQLを作成
        #
        #後から設定したい値は%sに置き換える
        sql = 'update student set name = %s , birthday = %s , class = %s where id = %s'
        #設定したい値はリストにする
        data = [student_name,student_birthday,student_class,student_id]

        #
        #4)SQL実行
        #

        
        #SQLを実行する(SQLの文字列、値のリスト)
        cursor.execute(sql, data)

        #
        #5)結果を表示
        #
        dbutil.triming_name(cursor)
        dbutil.triming_class(cursor)
        cnx.commit()
        print(f'ID={student_id}を更新しました')
    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)


    #
    #5)終了処理
    #

    finally:
        cursor.close()
        cnx.close()