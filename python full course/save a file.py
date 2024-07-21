from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir='C:\\Users\\User\\Desktop\\extra homeworks\\python full course\\save a file.py',
                                    filetypes=[
                                        ("text file",".txt"),
                                        ("HTML file",".html"),
                                        ("ALL files",".*")
                                    ])
    filedialog.asksaveasfile()
    # filetext = str(text.get(1.0,END))
    filetext = input('enter some text: ')
    file.write(filetext)

window = Tk()
button = Button(text='save',command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()