try:
    input1 = int(input('enter a number: '))
    input2 = int(input('enter another number: '))
    inputs = input1 // input2
    print(inputs)
except ZeroDivisionError:
    print('You cant divide by zero!')
except ValueError:
    print('write a number!')
except Exception:
    print('something went wrong')