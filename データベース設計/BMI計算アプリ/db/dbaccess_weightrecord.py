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