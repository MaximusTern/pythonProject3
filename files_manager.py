"""После запуска программы пользователь видит меню, состоящее из следующих пунктов:
- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
- выход."""


# смена рабочей директории (*необязательный пункт); - сделал возможность выбирать папку в пункте 4, при копировании

import random
import os
import sys
import shutil


while True:
  print('1. создать папку')
  print('2. удалить папку')
  print('3. удалить файл')
  print('4. копировать папку/файл')
  print('5. просмотр содержимого рабочей директории')
  print('6. посмотреть только папки')
  print('7. посмотреть только файлы')
  print('8. просмотр информации об операционной системе')
  print('9. создатель программы')
  print('10. играть в викторину')
  print('11. мой банковский счет')
  print('12. выход')
  choice = input('Выберите пункт меню')
  if choice == '1':
    folder = input('Введите название папки')
    if not os.path.isdir(folder):
      os.mkdir(folder)
  elif choice == '2':
    f_del = input('Какую папку удалить ? ')
    os.rmdir(f_del)
  elif choice == '3':
    d_file = input('Какой файл удалить ? ')
    os.remove(d_file)
  elif choice == '4':
    copy_folder = input('Введите папку, из которой будете копировать: ')
    copy_file = input('Введите файл для копирования: ')
    paste_folder = input('Введите папку, в которую копируете: ')
    paste_file = input('Введите название нового файла')
    shutil.copy(os.path.join(copy_folder,copy_file), os.path.join(paste_folder, paste_file))
  elif choice == '5':
    print(os.listdir())
  elif choice == '6':
    print('Каталоги: ')
    for dirpath, dirnames in os.walk("."):
      for dirname in dirnames:
        print(os.path.join(dirpath, dirname))
  elif choice == '7':
    print('Файлы в каталогах')
    for filenames in os.walk("."):
      for filename in filenames:
        print(filename)
  elif choice == '8':
    print(os.name)
  elif choice == '9':
    print(os.getlogin())
  elif choice == '10':
    import viktorina
  elif choice == '11':
    import use_function
  elif choice == '12':
    print('До свидания')
    break
