#
#成績登録プログラム
#examテーブルにキーボードで入力した情報を登録する
#

import mysql.connector
from dbutil import connect

#
#1)初期処理
#
#MySQLに接続
cnx = connect()
#
#2)キーボードから入力
#
print('成績登録')
id = input('IDを入力してください>>')
subject = input('科目を入力してください>>')
score = input('スコアを入力してください>>')

#
#3) 検索SQLを作成
#
#後から設定したい値は%sに置き換える
sql = 'insert into exam (id,subject,score) values (%s,%s,%s)'
#設定したい値はリストにする
data = [id,subject,score]

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

