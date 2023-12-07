def execute():
    #
    #学生登録プログラム
    #studentテーブルにキーボードで入力した情報を登録する
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
        print('学生登録')
        while True:
            id = inpututil.input_int('IDを入力してください>>')
            #入力したIDがテーブルに存在するかチェック
            rows = dbutil.find_by_id_student(cursor,id)
            if len(rows) == 0:
                break #入力したIDは存在しない

            #入力したIDが存在する
            print(f'ID={id}は存在しています')
        name = input('氏名を入力してください>>')
        birthday = inpututil.input_date('生年月日を入力してください>>')
        clas = input('クラスを入力してください>>')
        while True:
            judgment = input(f'{id}:{name}:{birthday}:{clas}を追加しますか?y/n>>')
            if judgment.lower() == 'y':
                break
            elif judgment.lower() == 'n':
                print('終了しました')
                return None
            else:
                print('Y/nのみ')
                continue
        #
        #3) 検索SQLを作成
        #
        #後から設定したい値は%sに置き換える
        sql = 'insert into student (id,name,birthday,class) values (%s,%s,%s,%s)'
        #設定したい値はリストにする
        data = [id,name,birthday,clas]

        
        #SQLを実行する(SQLの文字列、値のリスト)
        cursor.execute(sql, data)

        #
        #5)結果を表示
        #
        dbutil.triming_name(cursor)
        dbutil.triming_class(cursor)
        cnx.commit()
        print(f'ID={id}を登録しました')
    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)


    #
    #5)終了処理
    #

    finally:
        cursor.close()
        cnx.close()

