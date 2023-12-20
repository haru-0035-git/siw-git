from util import dbutil
def select_all(cursor,name):
    sql = 'select * from users where name = %s'
    data = [name]
    cursor.execute(sql,data)
    rows = cursor.fetchall()
    return rows



def add_user(cursor,name,birthday,height,target_weight):
    sql = 'insert into users (name,birthday,height,target_weight) values (%s,%s,%s,%s)'
    data = [name,birthday,height,target_weight]
    cursor.execute(sql,data)

    dbutil.triming_name(cursor)

def updata_weight(cursor,name,height):
    sql = 'update users set height = %s'
    data = [height]
    cursor.execute(sql,data)
    

