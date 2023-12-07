import mysql.connector
"""
データベースに接続
"""

#MySQLに接続
def connect():
    cnx = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'password',
        database = 'school',
    )

    #コネクションが切れたときに再接続する
    cnx.ping(reconnect=True)

    return cnx


#studentテーブルをidで検索して結果を返す
def find_by_id_student(cursor,id):
    sql = 'select * from student where id = %s order by id'
    data = [id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    return rows
