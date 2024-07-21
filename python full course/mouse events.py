from tkinter import *


def doSmth(event):
    print('Mouse coordinates: ' + str(event.x) + ',' + str(event.y))
window = Tk()

window.bind('<Button>', doSmth)
# window.bind('<Button2>', doSmth)
# window.bind('<Button3>', doSmth)

window.mainloop()