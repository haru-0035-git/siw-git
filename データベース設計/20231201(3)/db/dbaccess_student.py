#studentテーブルをidで検索して結果を返す
def find_by_id_student(cursor,id):
    sql = 'select * from student where id = %s order by id'
    data = [id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    return rows


def select_all(cursor,id):
    #
    #2) 検索SQLを作成
    #

    sql = 'select * from student order by id asc'
    #SQLを実行する
    cursor.execute(sql)
    #
    #4)取得したレコードを全て表示
    #
    rows = cursor.fetchall()

    return rows
