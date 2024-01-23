def show_weight():
    import sys
    import os
    sys.dont_write_bytecode = True
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import mysql.connector
    from util import dbutil
    from util import inpututil
    from db import dbaccess_user
    from db import dbaccess_weightrecord
    cnx = dbutil.connect()
    try:
        cursor = cnx.cursor(dictionary=True)
        print('★★★記録出力★★★')
        while True:
            name = input('ユーザ名を入力してください : ')
            rows = dbutil.find_by_name(cursor,name)
            if len(rows) == 1:
                break
            else:
                print('[Error] そのユーザは存在しません')
                continue
        date = inpututil.input_datetime('出力する年月を入力してください [%Y-%m]: ')
        rows=dbaccess_weightrecord.show_score(cursor,date,name)
        dbaccess_weightrecord.output_html(rows,name)
        print()
        print()
        print('ファイルに出力しました')
    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)
    finally:
        cursor.close()
        cnx.close()

if __name__ == '__main__':
    show_weight()

