from tkinter import *

root = Tk()
root.title('Instructions')
root.configure(bg='black')
root.geometry('1000x200')
root.iconbitmap("C:\\JL\\Justice_League_dc_comic_logo_movie-512.ico")

head = Label(root, text='Score Board(Instructions)', font=('Fixedsys', 40, 'normal'), fg='white', bg='black').pack()
mt = Label(root, text='', bg='black').pack()
pt1 = Label(root, text='Just press the button adjacent to this one ',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt2 = Label(root, text='By the way not all games have scores',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()




root.mainloop()