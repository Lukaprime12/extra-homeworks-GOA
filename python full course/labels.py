from tkinter import *
window = Tk()

photo = PhotoImage('artworks-bIQHFduN5IM9tz2B-sfAUCw-t500x500.jpg')

label = Label(window,
              text="Luka, do you even code?",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack()

window.mainloop()