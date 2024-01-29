# class Person:
#     def __init__(self, name, tel):
#         self.name = name
#         self.tel = tel
# def hash(s): 
#     n = len(s)
#     return ((ord(s[0]) - ord('A')
#         # ハッシュ関数
#         + (ord(s[n//2 - 1]) - ord('A')) * 26
#         + (ord(s[n - 2]) - ord('A')) * 26 * 26) % ModSize)
# TableSize = 1000
# ModSize = 1000
# table = [Person('', '') for i in range(TableSize)] # データ・テーブル
# while (data := input('名前,電話番号？')) != '/':
#     sdata = data.split(',')
#     name = sdata[0]
#     tel = sdata[1]
#     n = hash(name)
#     table[n] = Person(name, tel)
# while (data := input('検索するデータ？')) != '/':
#     n = hash(data)
#     print('{:d} {:s} {:s}'.format(n, table[n].name, table[n].tel))

def quick(a, left, right):
    if left < right:
        s = a[(left + right) // 2] # 中央の値を軸にする
        i = left - 1 # 軸より小さいグループと
        j = right + 1 # 大きいグループに分ける
        while True:
            i += 1
            while a[i] < s:
                i += 1
            j -= 1
            while a[j] > s:
                j -= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]
        quick(a, left, i - 1) # 左部分列に対する再帰呼び出し
        quick(a, j + 1, right) # 右部分列に対する再帰呼び出し
a = [41, 24, 76, 11, 45, 64, 21, 69, 19, 36]
N = len(a)
quick(a, 0, N - 1)
print(a)

