def show_weight():
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
        print('★★★記録表示★★★')
        while True:
            name = input('ユーザ名を入力してください : ')
            rows = dbutil.find_by_name(cursor,name)
            if len(rows) == 1:
                break
            else:
                print('[Error] そのユーザは存在しません')
                continue
        rows = dbaccess_user.select_all(cursor,name)
        bmi = []
        weight = []
        i=0
        for row in rows:
            height=float(row["height"])
            target_weight = float(row["target_weight"])
        rows = dbaccess_weightrecord.select_score(cursor,name)
        for row in rows:
            weight.append(float(row["weight"]))
            bmi.append(dbaccess_weightrecord.bmi(height,weight[i]))
            i+=1
        k=0
        for row in rows:
            print(f'id:{row["id"]}')
            print(f'日付:{row["datetime"]}')
            print(f'身長:{height}cm')
            print(f'体重:{weight[k]}kg')
            print(f'BMI:{bmi[k][0]}')
            print(f'標準体重:{round((bmi[k][2]),1)}kg (あと{round((bmi[k][2]-weight[k]),1)}kg)')
            print(f'肥満度:{bmi[k][1]}')
            print(f'目標体重:{target_weight}kg (あと{round((target_weight-weight[k]),1)}kg)')
            k += 1
    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)
    finally:
        cursor.close()
        cnx.close()

if __name__ == '__main__':
    show_weight()