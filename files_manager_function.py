

import os
def dir():
  return print(list(os.listdir()))

c= dir()

def catal():
  print('Каталоги: ')
  for dirpath, dirnames in os.walk("."):
    for dirname in dirnames:
       print(os.path.join(dirpath, dirname))