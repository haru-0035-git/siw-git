# while True:
#     try:
#         price = int(input('price:'))
#         count = int(input('count:'))
#         print(f'price//count={price//count}')
#         print('-'*25)
#         break
#     except ValueError:
#         print('Input an integer!')
#     except ZeroDivisionError:
#         print('The count must be != 0')


# while True:
#     try:
#         price = int(input('price:'))
#         count = int(input('count:'))
#         print(f'price//count={price//count}')
#     except Exception as e:
#         print(e)
#     else:
#         print('Good')
#         break
#     finally:
#         print('-'*25)
try:
    print(1)
    try:
        print(2)
        1/0
        print(3)
    except ValueError:
        print(4)
    finally:
        print(5)
    print(6)
except ZeroDivisionError:
    print(7)
finally:
    print(8)
print(9)