from tkinter import *

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar)
menubar.add_cascade(label='file', menu=fileMenu)

window.mainloop()