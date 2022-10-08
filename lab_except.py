try:
    sign = input('знак - ')
    lenght = int(input('lenght - '))
    trigger = input('trigger [вертикально - v |  горизонтально - h] - ')
    for i in range(0, lenght):
        if trigger =='v':
            print(sign)
        elif trigger =='h':
                print(sign, end='')
        else:
            raise Exception(' Incorrect choose of trigger')
except Exception as ex:
   print(f'Erorr information: {ex}')