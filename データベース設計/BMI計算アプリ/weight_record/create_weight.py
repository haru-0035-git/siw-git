def add_weight():
    import sys
    import os
    sys.dont_write_bytecode = True
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import mysql.connector
    from util import dbutil
    from util import inpututil
    from db   import dbaccess_weightrecord
    from db   import dbaccess_user
    import datetime

    cnx = dbutil.connect()
    try:
        cursor = cnx.cursor(dictionary=True)
        print('★★★体重登録★★★')
        while True:
            name = input('ユーザ名を入力してください : ')
            rows = dbutil.find_by_name(cursor,name)
            if len(rows) == 1:
                break
            else:
                print('[Error] そのユーザは存在しません')
                continue
        weight = inpututil.input_float('体重を入力してください(kg):')
        rows = dbaccess_user.select_all(cursor,name)
        for row in rows:
            height=float(row["height"])
            target_weight=float(row["target_weight"])
        bmi=dbaccess_weightrecord.bmi(height,weight)
        date = datetime.datetime.now()
        date = date.strftime('%Y-%m-%d %H:%M:%S')
        dbaccess_weightrecord.create_weight(cursor,name,height,weight,target_weight,date)
        cnx.commit()
        rows = dbaccess_weightrecord.select_score(cursor,name)
        for row in rows:
            print(f'id:{row["id"]}')
            print(f'日付:{date}')
            print(f'身長:{height}cm')
            print(f'体重:{weight}kg')
            print(f'BMI:{bmi[0]}')
            print(f'標準体重:{round((bmi[2]),1)}kg (あと{round((bmi[2]-weight),1)}kg)')
            print(f'肥満度:{bmi[1]}')
            print(f'目標体重:{target_weight}kg (あと{round((target_weight-weight),1)}kg)')
        print('体重を記録しました')
    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)
    finally:
        cursor.close()
        cnx.close()

if __name__ == '__main__':
    add_weight()