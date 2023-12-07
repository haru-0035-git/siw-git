def execute():
    #
    #成績更新プログラム
    #examテーブルにキーボードで入力した情報を更新する
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
    print('成績更新')
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
            break
        score = input('点数を入力してください>>')
        while True    :
            judgment = input(f'{score}点に更新しますか？ y/n>>')
            if judgment.lower() == 'y':
                break
            elif judgment.lower() == 'n':
                print('終了しました')
                sys.exit()
            else:
                print('y/nのみ')
                continue

        #
        #3) 検索SQLを作成
        #
        #後から設定したい値は%sに置き換える
        sql = 'update exam set score = %s where id = %s and subject = %s'
        #設定したい値はリストにする
        data = [subject,score,id]

        
        #SQLを実行する(SQLの文字列、値のリスト)
        cursor.execute(sql, data)

        #
        #5)結果を表示
        #
        dbutil.triming_subject(cursor)
        cnx.commit()
        print(f'ID={id}を更新しました')
    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)


    #
    #5)終了処理
    #

    finally:
        cursor.close()
        cnx.close()

