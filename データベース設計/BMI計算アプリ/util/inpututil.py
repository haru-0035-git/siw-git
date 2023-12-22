import datetime

#キーボードの入力内容を整数で返す
def input_int(prompt):    
    while True:
        str = input(prompt)
    # 数値チェック
        if not str.isdigit():
            print('エラー！！:整数を入力してください')
            # exit(1)#1は異常終了　0は正常終了
            continue
        break
    return int(str)

#キーボードの入力内容をfloatで返す
def input_float(prompt):    
    while True:
    # 数値チェック
        try:
            str = float(input(prompt))
            return str
        except ValueError:
            print('数字で入力してください')
            continue


#キーボードの入力内容を日付で返す
def input_date(prompt):
    while True:
        str = input(prompt)
        #日付チェック
        try:
            datetime.datetime.strptime(str,'%Y-%m-%d')
        except ValueError:
            print('エラー！！！：日付で入力してください')
            continue
        break
    return str