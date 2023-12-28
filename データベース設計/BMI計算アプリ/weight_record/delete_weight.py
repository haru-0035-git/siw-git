def delete_user():
    import sys
    import os
    sys.dont_write_bytecode = True
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import mysql.connector
    from util import dbutil
    from util import inpututil
    from db   import dbaccess_user
    from db   import dbaccess_weightrecord
    import datetime
    cnx = dbutil.connect()
    try:
        cursor = cnx.cursor(dictionary=True)
        print('★★★ユーザ削除★★★')
        while True:
            name = input('ユーザ名を入力してください : ')
            rows = dbaccess_weightrecord.select_score(cursor,name)
            if len(rows) >= 1:
                break
            else:
                print('[Error] そのユーザ名は存在しません')
        while True:
            id = int(input('idを入力してください : '))
            rows = dbaccess_weightrecord.find_by_id(cursor,id)
            if len(rows) == 1:
                break
            else:
                print('[Error] そのidは存在しません')
        rows = dbaccess_user.select_all(cursor,name)
        for row in rows:
            height=float(row["height"])
            target_weight=float(row["target_weight"])
        rows = dbaccess_weightrecord.find_by_id_name(cursor,name,id)
        weight = float(rows[0]["weight"])
        bmi=dbaccess_weightrecord.bmi(height,weight)
        date = datetime.datetime.now()
        date = date.strftime('%Y-%m-%d %H:%M:%S')
        for row in rows:
            print(f'id:{row["id"]}')
            print(f'日付:{date}')
            print(f'身長:{height}cm')
            print(f'体重:{weight}kg')
            print(f'BMI:{bmi[0]}')
            print(f'標準体重:{bmi[2]}kg (あと{round((bmi[2]-weight),1)}kg)')
            print(f'肥満度:{bmi[1]}')
            print(f'目標体重:{target_weight}kg (あと{round((target_weight-weight),1)}kg)')

        juge = input('このデータを全て削除してもよろしいですか? (y/n)>>')
        if juge.lower() == 'y':   
            dbaccess_weightrecord.delete_id(cursor,name,id)
            cnx.commit()
            print('削除しました')
        elif juge.lower() == 'n':
            return None
        else:
            print('y/n のみで')
    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)
    finally:
        cursor.close()
        cnx.close()
if __name__ == '__main__':
    delete_user()