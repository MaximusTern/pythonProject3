import random
users = {'max':'01.01.2002','mary':'02.01.2010','ivan':'05.02.2010',
         'yuri':'15.10.2008','paul':'05.05.2005','tom':'02.04.2011','mick':'05.09.2010',
         'kein':'01.01.2002','ron':'31.12.2002','zoi':'01.01.2006' }

months = {
    '01': 'января',
'02': 'февраля',
'03': 'марта',
'04': 'апреля',
'05': 'мая',
'06': 'июня',
'07': 'июля',
'08': 'августа',
'09': 'сентября',
'10': 'октября',
'11': 'ноября',
'12': 'декабря'
}

days = {    '01': 'первое',
'02': 'второе',
'03': 'третье',
'04': 'четвертое',
'05': 'пятое',
'06': 'шестое',
'07': 'седьмое',
'08': 'восьмое',
'09': 'девятое',
'10': 'десятое',
'11': 'одиннадцатое',
'12': 'двенадцатое',
'13': 'тринадцатое',
'14': 'четырнадцатое',
'15': 'пятнадцатое',
'16': 'шестнадцатое',
'17': 'семнадцатое',
'18': 'восемнадцатое',
'19': 'девятнадцатое',
'20': 'двадцатое',
'21': 'двадцать перовое',
'22': 'двадцать второе',
'23': 'двадцать третье',
'24': 'двадцать четвертое',
'25': 'двадцать пятое',
'26': 'двадцать шестое',
'27': 'двадцать седьмое',
'28': 'двадцать восьмое',
'29': 'двадцать девятое',
'30': 'тридцатое',
'31': 'тридцать первое'
        }


keys = random.sample(list(users),5)
for user in keys:
    print(user)
    birth = input('введите дату рождения: ')
    tr_birth = (users.get(user))
    if birth == tr_birth:
        print('Вы угадали')
    else:
        print('Вы не угадали. Правильная дата: ')
        day, month, year = tr_birth.split('.')
        print(days[day], months[month], year, 'года')
