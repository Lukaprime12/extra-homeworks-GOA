import os

path = "C:\\Users\\User\\Desktop\\folder"

if os.path.exists(path):

    print('this file exists!')
    if os.isfile(path):
        print('that is a file!')
    elif os.path.isdir(path):
        print('that is a dirrectory!')
else:

    print('this file doesnt exists!')