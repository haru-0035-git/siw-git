#
#学生登録プログラム
#studentテーブルにキーボードで入力した情報を登録する
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
print('学生登録')
student_id = input('学生のIDを入力してください>>')
student_name = input('学生の氏名を入力してください>>')
student_birthday = input('学生の生年月日を入力してください>>')
student_class = input('学生のクラスを入力してください>>')

#
#3) 検索SQLを作成
#
#後から設定したい値は%sに置き換える
sql = 'insert into student (id,name,birthday,class) values (%s,%s,%s,%s)'
#設定したい値はリストにする
data = [student_id,student_name,student_birthday,student_class]

#
#4)SQL実行
#

try:
    #カーソルを作成
    cursor = cnx.cursor(dictionary=True)
    
    #SQLを実行する(SQLの文字列、値のリスト)
    cursor.execute(sql, data)

    #
    #5)結果を表示
    #
    cnx.commit()
    print(f'ID={student_id}を登録しました')
except mysql.connector.Error as e:
    print('エラーが発生しました')
    print(e)


#
#5)終了処理
#

finally:
    cursor.close()
    cnx.close()

