def ribo(loan,interest_rate,repayment_amount):
    i = 0
    principal = loan
    while True:
        loan = (loan + (loan * (interest_rate / 12)) - repayment_amount) 
        if loan <= 0:
            print(f'{round(principal)}円借りて、月々{round(repayment_amount)}円返済した場合{i + 1}回で返済できます')
            break
        else:
            i += 1
            if i == 100:
                print(f'{round(principal)}円借りて、月々{round(repayment_amount)}円返済した場合,永久に返済できません')
                break
            continue

def input_float(prompt):
    while True:
        try:
            str = float(input(prompt))
            return str
        except ValueError:
            print('数字を入れてください')
            continue

def input_int(prompt):
    while True:
        try:
            str = int(input(prompt))
            return str
        except ValueError:
            print('数字を入れてください')
            continue

def ribopay():
    loan = input_float('借入金額を入れてください : ')
    interest_rate = input_int('金利を入れてください(%) : ') / 100
    repayment_amount = input_float('返済額を入れてください : ')
    ribo(loan,interest_rate,repayment_amount)

ribopay()

# def loan_repayment(principal, interest_rate, repayment_amount):
#     months = 0
#     while principal > 0:
#         principal = principal + (principal * (interest_rate / 12)) - repayment_amount
#         months += 1
#         if months == 100:
#             print(f'{round(principal, 0)}円借りて、月々{round(repayment_amount, 0)}円返済した場合、永久に返済できません')
#             break
#     else:
#         print(f'{round(principal + repayment_amount)}円借りて、月々{round(repayment_amount)}円返済した場合{months}回で返済できます')

# def input_float(prompt):
#     while True:
#         try:
#             input_value = float(input(prompt))
#             return input_value
#         except ValueError:
#             print('数字を入れてください')

# def input_int(prompt):
#     while True:
#         try:
#             input_value = int(input(prompt))
#             return input_value
#         except ValueError:
#             print('数字を入れてください')

# def loan_payment():
#     loan = input_float('借入金額を入れてください: ')
#     interest_rate = input_int('金利を入れてください(%): ') / 100
#     repayment_amount = input_float('返済額を入れてください: ')
#     loan_repayment(loan, interest_rate, repayment_amount)

# loan_payment()
