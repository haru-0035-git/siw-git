def execute():
    import sys
    sys.dont_write_bytecode = True
    import mysql.connector
    from util import dbutil
    from util import inpututil

    cnx = dbutil.connect()
    try:
        cursor = cnx.cursor(dictionary=True)
        print('★★★ユーザ登録★★★')
        while True:
            name = input('ユーザ名を入力してください : ')
            birthday = input('生年月日を入力してください [%Y-%m-%d] : ')
            weight = float(input('身長を入力してください (cm) : '))
            targetweight = float(input('目標の体重を入力してください(kg) : '))
    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)
    finally:
        cursor.close()
        cnx.close()

if __name__ == '__main__':
    execute()