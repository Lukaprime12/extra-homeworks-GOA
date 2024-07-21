import os

path = 'text.txt'

try:
    os.remove(path)
except FileNotFoundError:
    print('This file does not exist !')
except PermissionError:
    print('you do not have permission to delete that file !')
else:
    print(path +' was removed')