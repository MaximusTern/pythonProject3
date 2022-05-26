import os
import json

FILE_NAME = 'orders_pickle.json'

history = {}
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'r') as fp:
        history = json.load(fp)


wallet = 0

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню')
    if choice == '1':
        credit = int(input('Введите сумму пополнения: '))
        wallet=wallet+credit
        print ('Ваш счет = ',wallet)
    elif choice == '2':
        sum_package = int(input('Введите сумму покупки: '))
        if sum_package > wallet:
            print('У вас не хватает денег на покупку')
        else:
            package = input('Введите наименование покупки: ')
            wallet = wallet - sum_package
            print('Ваш счет = ', wallet)
            history['Остаток'] = wallet
            history[package] = str(sum_package)
            with open(FILE_NAME, 'w') as fp:
                json.dump(history, fp)
    elif choice == '3':
        print('Ваша история покупок:', history)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')