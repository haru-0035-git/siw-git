def execute():
    import sys
    sys.dont_write_bytecode = True
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from db import dbaccess_weightrecord
    from weight_record import create_weight
    from weight_record import delete_weight
    from weight_record import show_score
    from weight_record import display_score
    while True:
        print('====体重管理メニュー===')
        print('1. 体重管理')
        print('2. 記録表示')
        print('3. 記録削除')
        print('4. 記録出力')
        print('5. 終了')
        judgment = input('メニューを選択してください : ')
        if judgment == '1':
            create_weight.add_weight()
        elif judgment == '2':
            show_score.show_weight()
        elif judgment == '3':
            delete_weight.delete_user()
        elif judgment == '4':
            display_score.show_weight()
        elif judgment == '5':
            break
        else:
            print('1~5まで')
            continue

if __name__ == '__main__':
    execute()