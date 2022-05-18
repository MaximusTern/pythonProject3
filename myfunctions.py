"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""


# Задача 1
""" 
   Функция создает красивый резделитель из 10-и звездочек (**********)
   :return: **********
   """
#print(simple_separator() == '**********')  # True

def simple_separator():
    return print("**********")
simple_separator()




# Задача 2

""" 
  создает разделитель из звездочек число которых можно регулировать параметром count
param count: количество звездо
eturn: строка разделитель, примеры использования ниже
 """
#print(long_separator(3) == '***')  # True
#print(long_separator(4) == '****')  # True



def long_separator(count):
    return print(count * '*')

long_separator(3)



# Задача 4
"""
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """

#print(separator('-', 10) == '----------')  # True
#print(separator('#', 5) == '#####')  # True


def separator(simbol, count):
    return print(simbol * count)

separator('-', 4)





# Задача 5
"""
    Функция печатает Hello World в формате:
    **********
    Hello World!
    ##########
    :return: None
    """



'''
**********
Hello World!
##########
'''
#hello_world()

def hello_world():
    print('**********\nHello World!\n##########')

hello_world()


# Задача 6

"""
    Функция печатает приветствие в красивом формате
    **********
    Hello {who}!
    ##########
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """

'''
**********
Hello World!
##########
'''
#hello_who()
'''
**********
Hello Max!
##########
'''
#hello_who('Max')
'''
**********
Hello Kate!
##########
'''
#hello_who('Kate')

def hello_who(who='World'):
    print('**********\nHello '+who+'\n##########')


hello_who('Max')



# Задача 7
"""
    Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления # True -> (1 + 2)**1
    """


#print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
#print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
#print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
#print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
#print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100

def pow_many(power, *args):
    summa = 0
    for i in args:
        summa += i
    return  print(summa ** power)

pow_many(2, 1, 2, 5)




# Задача 8
"""
    Функция выводит переданные параметры в фиде key --> value
    key - имя параметра
    value - значение параметра
    :param kwargs: любое количество именованных параметров
    :return: None
    """

"""
name --> Max
age --> 21
"""
#print_key_val(name='Max', age=21)
"""
animal --> Cat
is_animal --> True
"""
#print_key_val(animal='Cat', is_animal=True)


def print_key_val(**kwargs):
    for k, v in kwargs.items():
        print(str(k)+'='+str(v))


print_key_val(name='Max', age=21)


# Задача 9

"""
    (Усложненое задание со *)
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
    (примеры ниже)
    :param iterable: входаня последовательности
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """

#print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
#print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
#print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
#print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True



def my_filter(iterable, function):
    filter_list = list(filter(lambda x: x > function, iterable))
    return print(filter_list)

my_filter([1, 2, 3, 4, 5],2)
