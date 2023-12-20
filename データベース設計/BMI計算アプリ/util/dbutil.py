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
        database = 'BMI_calculation',
        auth_plugin="mysql_native_password",
    )

    #コネクションが切れたときに再接続する
    cnx.ping(reconnect=True)

    return cnx

def find_by_name(cursor,name):
    sql = 'select * from users where name = %s order by id'
    data = [name]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    return rows

# def find_by_id(cursor,id):
#     sql = 'select * from users where id = %s order by id'
#     data = [id]
#     cursor.execute(sql,data)
#     rows = cursor.fetchall()
#     return rows

# def triming_subject(cursor):
#     sql = 'update exam set subject = trim(replace(subject,"　"," "))'
#     cursor.execute(sql)

def triming_name(cursor):
    sql = 'update users set name = trim(replace(name,"　"," "))'
    cursor.execute(sql)

# def triming_class(cursor):
#     sql = 'update student set class = trim(replace(class,"　"," "))'
#     cursor.execute(sql)
