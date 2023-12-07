def execute():
    #
    #成績登録プログラム
    #examテーブルにキーボードで入力した情報を登録する
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
    print('成績登録')
    try:
        #カーソルを作成
        cursor = cnx.cursor(dictionary=True)
        
        while True:
            id = inpututil.input_int('IDを入力してください>>')
            student = dbutil.find_by_id_student(cursor,id)
            if len(student) == 0:
                print(f'ID={id}はstudentテーブルに存在しません')
                continue
            subject = input('科目を入力してください>>')
            rows = dbutil.find_by_id_subject(cursor,id,subject)
            if len(rows) > 0:
                print(f'ID={id}の{subject}はすでに存在しています')
                continue
            break
        
        score = inpututil.input_int('スコアを入力してください>>')
        while True:    
            judgment = input(f'{id}:{subject}:{score}を追加しますか? y/n>>')
            if judgment.lower() == 'y':
                break
            elif judgment.lower() == 'n':
                return None
            else:
                continue


        #
        #3) 検索SQLを作成
        #
        #後から設定したい値は%sに置き換える
        sql = 'insert into exam (id,subject,score) values (%s,%s,%s)'
        #設定したい値はリストにする
        data = [id,subject,score]
    
        #SQLを実行する(SQLの文字列、値のリスト)
        cursor.execute(sql, data)

        #
        #5)結果を表示
        #
        dbutil.triming_subject(cursor)
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

if __name__ == '__main__':
    execute()