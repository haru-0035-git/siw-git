def execute():
    #
    #成績削除プログラム
    #examテーブルのキーボードで入力した条件で情報を削除する
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

    #
    #2)キーボードから入力
    #
    print('成績削除')
    try:
        #カーソルを作成
        cursor = cnx.cursor(dictionary=True)
        while True:        
            id = inpututil.input_int('IDを入力してください>>')
            rows = dbutil.find_by_id_student(cursor,id)
            if len(rows) == 0:
                print(f'ID={id}は存在しません')
                continue
            subject = input('科目を入力してください>>')
            rows = dbutil.find_by_id_subject(cursor,id,subject)
            if len(rows) == 0:
                print(f'ID={id}の{subject}は存在しません')
                continue
            for row in rows:
                print(f'{row["id"]}:{row["subject"]} {row["score"]}点')
            while True    :
                judgment = input('削除しますか？ y/n>>')
                if judgment.lower() == 'y':
                    break
                elif judgment.lower() == 'n':
                    print('終了しました')
                    sys.exit()
                else:
                    print('Y/nのみ')
                    continue
            break
        #
        #3) 検索SQLを作成
        #
        #後から設定したい値は%sに置き換える
        sql = 'delete from exam where id = %s and subject = %s'
        #設定したい値はリストにする
        data = [id,subject]

        
        #SQLを実行する(SQLの文字列、値のリスト)
        cursor.execute(sql, data)

        #
        #5)結果を表示
        #
        cnx.commit()
        print(f'ID={id}の{subject}を削除しました')
    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)


    #
    #5)終了処理
    #

    finally:
        cursor.close()
        cnx.close()

