try:
    num = int(input('number - '))
    print(f'!{num} =', end= ' ')
    t=1
    for i in range(1, num+1):
        if i == num:
            print(i, end= '')
        else:
            print(f'{i} *', end='')
        t=i
        print(f'= {t}')
except Exception as ex:
    print(f'Erorr information:')