
try:
    with open('test.txt.txt') as file:
        print(file.read())
except FileNotFoundError:
    print('file not found!')