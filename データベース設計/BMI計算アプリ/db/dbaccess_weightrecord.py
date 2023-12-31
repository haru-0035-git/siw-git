def create_weight(cursor,name,height,weight,target_weight,datetime):
    sql = 'insert into weight_records (user_name,height,weight,target_weight,datetime) values(%s,%s,%s,%s,%s)' 
    date = [name,height,weight,target_weight,datetime]
    cursor.execute(sql,date)

def bmi(height,weight):
    bmi = round((weight / (height / 100) ** 2),1)
    standard = ((height / 100) ** 2) *22
    if bmi < 18.5:
        bmi_j = '痩せ'
        return bmi,bmi_j,standard
    elif bmi < 25:
        bmi_j = '普通'
        return bmi,bmi_j,standard
    elif bmi < 30:
        bmi_j = '肥満度(1)'
        return bmi,bmi_j,standard
    elif bmi < 35:
        bmi_j = '肥満度(2)'
        return bmi,bmi_j,standard
    elif bmi < 40:
        bmi_j = '肥満度(3)'
        return bmi,bmi_j,standard
    elif bmi >= 40:
        bmi_j = '肥満度(4)'
        return bmi,bmi_j,standard

def select_score(cursor,name):
    sql = 'select * from weight_records where user_name = %s' 
    data = [name]
    cursor.execute(sql,data)
    rows = cursor.fetchall()
    return rows

def find_by_id(cursor,id):
    sql = 'select * from weight_records where id = %s' 
    data = [id]
    cursor.execute(sql,data)
    rows = cursor.fetchall()
    return rows

def find_by_id_name(cursor,name,id):
    sql = 'select * from weight_records where id = %s and user_name = %s' 
    data = [id,name]
    try:
        cursor.execute(sql,data)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print(e)

def delete_id(cursor,name,id):
    sql = 'delete from weight_record where user_name = %s and id = %s'
    data = [name,id]
    cursor.execute(sql,data)

def show_score(cursor,day,name):
    sql = 'SELECT * from weight_records WHERE date_format(datetime,"%Y-%m") = %s AND user_name = %s order by id asc'
    date = [day,name]
    cursor.execute(sql,date)
    rows = cursor.fetchall()
    return rows


def output_html(rows,name):
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
        cursor = cnx.cursor(dictionary=True)
        with open('display_score.html',mode='w',encoding='utf-8',newline='\n') as file:

            file.write('<html>\n')
            file.write('<head>\n')
            file.write('<title>記録出力</title>\n')
            file.write('</head>\n')
            file.write('<body>\n')
            file.write('<h1>記録出力</h1>\n')
            file.write('<hr>\n')
            #テーブルで出力
            file.write('<table border=1>\n') #テーブルの外枠を作る
            file.write('<tr>\n') #テーブルの行を作る
            file.write('<td>ID</td><td>日付</td><td>身長</td><td>体重</td><td>BMI</td><td>標準体重</td><td>肥満度</td><td>目標体重</td>') #行に列を作る
            file.write('</tr>\n')

            #selectしたレコードを出力
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
                file.write('<tr>\n')
                file.write(f'<td>{row["id"]}</td>\n')
                file.write(f'<td>{row["datetime"]}</td>\n')
                file.write(f'<td>{height}cm</td>\n')
                file.write(f'<td>{weight[k]}kg</td>\n')
                file.write(f'<td>{bmi[k][0]}</td>\n')
                file.write(f'<td>{round((bmi[k][2]),1)}kg (あと{round((bmi[k][2]-weight[k]),1)}kg)</td>\n')
                file.write(f'<td>{bmi[k][1]}</td>\n')
                file.write(f'<td>{target_weight}kg (あと{round((target_weight-weight[k]),1)}kg)</td>\n')
                k += 1