def execute():
    #
    #学生出力プログラム
    #studentテーブルからすべてのレコ―ドを取得してHTML形式で出力
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
        #データベースから学生情報を全件取得
        rows = dbaccess_student.select_all(cursor,id)

        #HTML形式でファイル出力
        output_html(rows)

    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)


    #
    #5)終了処理
    #

    finally:
        cursor.close()
        cnx.close()


#HTMLファイルに出力
def output_html(rows):
    with open('all_student.html',mode='w',encoding='utf-8',newline='\n') as file:
        
        file.write('<html>\n')
        file.write('<head>\n')
        file.write('<title>学生一覧</title>\n')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write('<h1>学生一覧</h1>\n')
        file.write('<hr>\n')
        #テーブルで出力
        file.write('<table border=1>\n') #テーブルの外枠を作る
        file.write('<tr>\n') #テーブルの行を作る
        file.write('<td>ID</td><td>名前</td><td>生年月日</td><td>クラス</td>') #行に列を作る
        file.write('</tr>\n')

        #SELECTしたレコードを出力
        for row in rows:
            file.write('<tr>\n')
            file.write(f"<td>{row['id']}</td>\n")
            file.write(f"<td>{row['name']}</td>\n")
            file.write(f"<td>{row['birthday']}</td>\n")
            file.write(f"<td>{row['class']}</td>\n")
        file.write('</table>\n')
        file.write('</body>\n')
        file.write('</html>\n')


if __name__ == '__main__':
    execute()