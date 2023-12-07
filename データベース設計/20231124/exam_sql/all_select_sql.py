import sys
sys.dont_write_bytecode = True
import select_all_exam
import create_exam
import update_exam
import delete_exam
import find_by_id_exam

while True:
    select_sql = input('一覧表示>>1,ID検索>>2,登録>>3,更新>>4,削除>>5,終了>>6|>>')
    if select_sql == '2':
        find_by_id_exam.execute()
        break
    elif select_sql == '3':
        create_exam.execute()
        break
    elif select_sql == '4':
        update_exam.execute()
        break
    elif select_sql == '5':
        delete_exam.execute()
        break
    elif select_sql == '6':
        print('終了')
        break
    elif select_sql == '1':
        select_all_exam.execute()
        break
    else:
        continue
