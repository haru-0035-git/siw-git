#
#成績表示プログラム
#examテーブルから全ての成績を表示する
#

import mysql.connector
from dbutil import connect
#
#1)初期処理
#
#MySQLに接続

cnx = connect()

print('成績表示')
#
#2) 検索SQLを作成
#
#後から設定したい値は%sに置き換える
sql = 'select id,subject,score from exam order by id'
sql_avg = 'select subject,avg(score) as avg from exam group by subject'
#設定したい値はリストにする

#
#3)SQL実行
#

try:
    #カーソルを作成
    cursor = cnx.cursor(dictionary=True)
    
    #SQLを実行する(SQLの文字列、値のリスト)
    cursor.execute(sql)

    #
    #4)結果を表示
    #
    rows = cursor.fetchall()
    for row in rows:
        print(f'{row["id"]}:{row["subject"]} {row["score"]}点')

    cursor.execute(sql_avg)
    rows = cursor.fetchall()
    for row in rows :   
        print(f'{row["subject"]}の平均は{round(row["avg"],1)}点')

except mysql.connector.Error as e:
    print('エラーが発生しました')
    print(e)


#
#5)終了処理
#

finally:
    cursor.close()
    cnx.close()

