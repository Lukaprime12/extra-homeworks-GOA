def hello(**kwargs):
    print("Hello")
    for key,value in kwargs.items():
        print(value)

hello(first='Luka',middle='code',last='Mtchedlidze')