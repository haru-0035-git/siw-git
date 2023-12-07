def execute():
    #
    #成績表示プログラム
    #examテーブルから全ての成績を表示する
    #

    import mysql.connector
    import sys
    sys.dont_write_bytecode = True
    import  os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import mysql.connector
    from util import dbutil
    from db import dbaccess_exam
    #
    #1)初期処理
    #
    #MySQLに接続

    cnx = dbutil.connect()
    #
    #2) 検索SQLを作成
    #
    # sql_avg = 'select subject,avg(score) as avg from exam group by subject'


    #
    #3)SQL実行
    #

    try:
        #カーソルを作成
        cursor = cnx.cursor(dictionary=True)

        rows = dbaccess_exam.select_all(cursor,id)
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

def output_html(rows):
    with open('all_exam.html',mode='w',encoding='utf-8',newline='\n') as file:
        
        file.write('<html>\n')
        file.write('<head>\n')
        file.write('<title>成績一覧</title>\n')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write('<h1>成績一覧</h1>\n')
        file.write('<hr>\n')
        #テーブルで出力
        file.write('<table border=1>\n') #テーブルの外枠を作る
        file.write('<tr>\n') #テーブルの行を作る
        file.write('<td>ID</td><td>科目</td><td>点数</td>') #行に列を作る
        file.write('</tr>\n')

        #SELECTしたレコードを出力
        for row in rows:
            file.write('<tr>\n')
            file.write(f"<td>{row['id']}</td>\n")
            file.write(f"<td>{row['subject']}</td>\n")
            file.write(f"<td>{row['score']}</td>\n")
        file.write('</table>\n')
        file.write('</body>\n')
        file.write('</html>\n')

if __name__ == '__main__':
    execute()