# while 10>5:
#     name = input('what is your name: ')
#     if name != '':
#         break

number = '123-456-7890'
for i in number:
    if i == '-':
        continue
    print(i, end='')

# for i in range(1, 21):
#     if i == 13:
#         pass
#     else:
#         print(i)