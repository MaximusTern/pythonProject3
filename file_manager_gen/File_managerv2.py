import os
from glob import glob
import json

file_history = 'listdir.txt'

history = {}
files_ = []
dirs_=[]

history = (json.load(open(file_history, 'r')) if os.path.exists(file_history) else "")




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
    (os.mkdir(folder) if not os.path.isdir(folder) else "")
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
    for root, dirs, files in os.walk("."):
      for filename in files:
        files_.append(filename)
        history['files'] = files_
        with open(file_history, 'w') as fp:
          json.dump(history, fp)
    for root, dirs, files  in os.walk("."):
      for dir in dirs:
        dirs_.append(dir)
        history['dirs'] = dirs_
        with open(file_history, 'w') as fp:
          json.dump(history, fp)
    print(history)
  elif choice == '6':
    print('Каталоги: ')
    for dirpath, dirnames,files in os.walk("."):
      for dirname in dirnames:
        print(os.path.join(dirpath, dirname))
  elif choice == '7':
    print('Файлы в каталогах')
    for filenames in os.walk("."):
      print(list(filename for filename in filenames if filename != "." ))
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




