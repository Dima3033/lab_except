try:
    num_1 = int(input("Введіть число 1 : "))
    num_2 = int(input('Введіть число 2 : '))
    sum = 0
    counter = 0
    for i in range(num_1, num_2 + 1):
        print(f'{sum} +{i} = ', end=' ')
        sum += i
        print(f'{sum}')
        print(f'Sum = {sum}')
        counter+=1
    s = (num_1+num_2)/counter
    print(s)
except Exception as ex:
    print(f'Erorr information: {ex}')
finally:
    print('Exite...')

