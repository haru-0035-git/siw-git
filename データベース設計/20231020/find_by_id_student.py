#
#学生ID検索プログラム
#studentテーブルからキーボードで入力したIDを条件にレコ―ドを取得して表示
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
    database = 'school',
)

#コネクションが切れたときに再接続する
cnx.ping(reconnect=True)

#
#2)キーボードから入力
#

student_id = input('学生のIDを入力してください>>')

#
#3) 検索SQLを作成
#
#後から設定したい値は%sに置き換える
sql = 'select * from student where id = %s order by id'
#設定したい値はリストにする
data = [student_id]

#
#4)SQL実行
#

try:
    #カーソルを作成
    cursor = cnx.cursor(dictionary=True)
    
    #SQLを実行する
    cursor.execute(sql, data)

    #
    #4)取得したレコードを全て表示
    #
    rows = cursor.fetchall()
    if len(rows) != 0 :
        for row in rows:
            print(f'{row["id"]}:{row["name"]}:{row["class"]}')
            break
    else:
        print('そのIDはありません')
        
except mysql.connector.Error as e:
    print('エラーが発生しました')
    print(e)


#
#5)終了処理
#

finally:
    cursor.close()
    cnx.close()