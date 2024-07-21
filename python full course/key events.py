from tkinter import *


def doSomething(event):
    print('you pessed: '+event.keysym)



window = Tk()

window.bind('<Key>',doSomething)

window.mainloop()