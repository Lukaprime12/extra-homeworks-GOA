import os

source = "new file.txt"
destination = "C:\\Users\\User\\Desktop\\new file.txt"

try:
    if os.path.exists(destination):
        print('file already exists!')
    else:
        os.replace(source,destination)
        print(source + ' was moved')
except FileNotFoundError:
    print(source + ' not found')