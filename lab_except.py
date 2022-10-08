try:
    num_1 = int(input("Введіть число 1 : "))
    num_2 = int(input('Введіть число 2 : '))
    sum = 0
    counter = num_2-num_1+1
    for i in range(num_1, num_2 + 1):
        sum += i
    ar = sum/counter
    print(f'{sum} \n {ar}')
except Exception as ex:
    print(f'Erorr information: {ex}')
finally:
    print('Exite...')

