#
#成績表示プログラム
#examテーブルからキーボードで入力した条件で情報を表示する
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
    print('成績表示')
    while True:    
        id = inpututil.input_int('学生のIDを入力ください>>')
        rows = dbutil.find_by_id_student(cursor,id)
        if len(rows) == 0:
            print(f'ID={id}は存在しません')
            continue
        break

    #
    #3) 検索SQLを作成
    #
    #後から設定したい値は%sに置き換える
    sql = 'select id,subject,score from exam where id = %s order by id'
    #設定したい値はリストにする
    data = [id]
    #
    #4)SQL実行
    #

    
    #SQLを実行する(SQLの文字列、値のリスト)
    cursor.execute(sql,data)

    #
    #5)結果を表示
    #
    rows = cursor.fetchall()
    if len(rows) != 0:    
        for row in rows:
            print(f'{row["id"]}:{row["subject"]} {row["score"]}点')
    else:
        print(f'ID={id}は見つかりません')

except mysql.connector.Error as e:
    print('エラーが発生しました')
    print(e)


#
#5)終了処理
#

finally:
    cursor.close()
    cnx.close()

