#
#学生表示プログラム
#studentテーブルからすべてのレコ―ドを取得して表示
#

import mysql.connector

#
#1)初期処理
#
#MySQLに接続

cnx = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = '',
)

#コネクションが切れたときに再接続する
cnx.ping(reconnect=True)

#
#2) 検索SQLを作成
#

sql = ''

#
#3)SQL実行
#

try:
    #カーソルを作成
    cursor = cnx.cursor(dictionary=True)
    
    #SQLを実行する
    cursor.execute(sql)

    #
    #4)取得したレコードを全て表示
    #
    rows = cursor.fetchall()
    for row in rows:
        print(f'{row["id"]}:{row["name"]}:{row["class"]}')

except mysql.connector.Error as e:
    print('エラーが発生しました')
    print(e)


#
#5)終了処理
#

finally:
    cursor.close()
    cnx.close()