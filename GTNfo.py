from tkinter import *

root = Tk()
root.title('Instructions')
root.configure(bg='black')
root.geometry('1000x215')
root.iconbitmap("C:\\JL\\Justice_League_dc_comic_logo_movie-512.ico")

head = Label(root, text='Guess the Number(Instructions)', font=('Fixedsys', 40, 'normal'), fg='white', bg='black').pack()
mt = Label(root, text='', bg='black').pack()
pt1 = Label(root, text='The computer has chosen a number at random in the range (1 - 50)',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt2 = Label(root, text='You have 10 chances to guess the number ',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt3 = Label(root, text='After every entry the entry box will be cleared',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt4 = Label(root, text='Hints will be displayed on the bottom',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt5 = Label(root, text='May the force be with you!',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()

root.mainloop()