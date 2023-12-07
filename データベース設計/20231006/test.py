# h = int(input('身長(cm)>>>')) / 100
# w = int(input('体重(kg)>>>'))
# bmi = w / (h ** 2)
# if bmi < 18.5:
#     print('やせ')
# elif bmi >= 18.5 and bmi < 25:
#     print('普通')
# elif bmi >= 25 and bmi < 30:
#     print('やや肥満')
# else :
#     print('肥満')
# print(f'貴方のBMIは{round(bmi,1)}')

# print(F'適正体重は{round((h**2)*22,1)}')

# def sintyo():
#     h = input('身長>>>')
#     if h.isdigit():
#         h = float(h) / 100
#         return h
#     else:
#         print('数字を入れてください')
#         return sintyo()
# def taiju():
#     w = input('体重>>>')
#     if w.isdigit():
#         w = float(w)
#         return w
#     else:
#         print('数字を入れてください')
#         return taiju()
# h = sintyo()
# w = taiju()
# bmi = w / (h ** 2)
# if bmi < 18.5:
#     print('やせ')
# elif bmi >= 18.5 and bmi < 25:
#     print('普通')
# elif bmi >= 25 and bmi < 30:
#     print('やや肥満')
# else :
#     print('肥満')
# print(f'貴方のBMIは{round(bmi,1)}')

# print(F'適正体重は{round((h**2)*22,1)}')

def func_float(l,k):
    while True:
        try:
            x = float(input(f'{l}({k})を入力してください'))
            return x
        except:
            print('数字を入れて')
h = func_float('身長','cm') / 100
w = func_float('体重','kg')
bmi = w / (h ** 2)
if bmi < 18.5:
    print('やせ')
elif bmi < 25:
    print('普通')
elif bmi < 30:
    print('やや肥満')
else :
    print('肥満')
print(f'貴方のBMIは{round(bmi,1)}')

print(F'適正体重は{round((h**2)*22,1)}kg')
