import sys
sys.dont_write_bytecode = True
from exam_sql import menu_exam
from student_sql import menu_student

while True:
    juge = input('学生登録>>1|成績登録>>2|終了>>3|>>')
    if juge == '1':
        menu_student.execute()
    elif juge == '2':
        menu_exam.execute()
    elif juge == '3':
        break

    else:
        print('1~3')
        continue
