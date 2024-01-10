for i in range(1,16):
    if (i % 3 == 0) and (i % 5 == 0):
        print(f'{i} fizz-buzz')
    elif (i % 3 == 0):
        print(f'{i} : fizz')
    elif (i % 5 == 0):
        print(f'{i} : buzz')
    else:
        print(f'{i} : None')