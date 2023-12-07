def select_all(cursor,id):
    sql = 'select * from exam order by id'
    cursor.execute(sql)

    #
    #4)結果を表示
    #
    rows = cursor.fetchall()

    return rows