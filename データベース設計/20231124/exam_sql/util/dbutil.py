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
        auth_plugin="mysql_native_password",
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

def find_by_id_subject(cursor,id,subject):
    sql = 'select * from exam where id = %s and subject = %s order by id'
    data = [id,subject]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    return rows

def triming_subject(cursor):
    sql = 'update exam set subject = trim(replace(subject,"　"," "))'
    cursor.execute(sql)