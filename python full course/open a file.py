from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir='C:\Users\User\Desktop\extra homeworks\python full course\__pycache__',
                                          title = 'open a file okay? ',
                                          filetypes=(('text files', + '.txt')
                                          ('all files')))
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()
button = Button(text="open", command=openFile)
button.pack()
window.mainloop()