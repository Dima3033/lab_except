try:
    num = int(input('Введіть число - '))
    print(f'!{num} =', end= ' ')
    temp = 1
    for i in range(1, num+1):
        if i == num:
            print(i, end = '')
        else:
            print(f'{i} * ', end ='')
        temp*=i
        print(f'= {temp}')
except Exception as ex:
    print(f'Erorr information:')