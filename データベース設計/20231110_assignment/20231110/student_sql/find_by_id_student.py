#
#学生ID検索プログラム
#examテーブルからキーボードで入力したIDを条件にレコ―ドを取得して表示
#
import sys
sys.dont_write_bytecode = True
import mysql.connector
from util import dbutil
from util import inpututil
#
#1)初期処理
#MySQLに接続

cnx = dbutil.connect()

try:
    #カーソルを作成
    cursor = cnx.cursor(dictionary=True)
    #
    #2)キーボードから入力
    #
    while True:    
        id = inpututil.input_int('IDを入力してください>>')
        rows = dbutil.find_by_id_student(cursor,id)
        if len(rows) == 0:
            print(f'ID={id}は存在しません')
            continue
        break


    #
    #3) 検索SQLを作成
    #
    #後から設定したい値は%sに置き換える
    sql = 'select * from student where id = %s order by id'
    #設定したい値はリストにする
    data = [id]

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