import sys
sys.dont_write_bytecode = True
import select_all_student
import find_by_id_student
import update_student 
import delete_student
import creat_student2
while True:
    select_sql = input('一覧表示>>1,ID検索>>2,登録>>3,更新>>4,削除>>5,終了>>6|>>')
    if select_sql == '2':
        find_by_id_student.execute()
    elif select_sql == '3' :
        creat_student2.execute()
    elif select_sql == '4' :
        update_student.execute()
    elif select_sql == '5':
        delete_student.execute()
    elif select_sql == '1':
        select_all_student.execute()
    elif select_sql == '6':
        print('終了')
        break
    else:
        continue
    