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
#
#2)キーボードから入力
#
print('学生登録')
student_id = inpututil.input_int('IDを入力してください>>')
student_name = input('氏名を入力してください>>')
student_birthday = inpututil.input_date('生年月日を入力してください>>')
student_class = input('クラスを入力してください>>')

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

