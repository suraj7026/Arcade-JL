from tkinter import *

root = Tk()
root.title('Instructions')
root.configure(bg='black')
root.geometry('1000x220')
root.iconbitmap("C:\\JL\\Justice_League_dc_comic_logo_movie-512.ico")

head = Label(root, text='Snake(Instructions)', font=('Fixedsys', 40, 'normal'), fg='white', bg='black').pack()
mt = Label(root, text='', bg='black').pack()
pt1 = Label(root, text="IT'S  A SINGLE PLAYER GAME",  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt2 = Label(root, text='You have small snake at the top left corner of the screen',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt3 = Label(root, text='apples will appear randomly, eat them and grow ',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt4 = Label(root, text='If you hit the wall or eat your self the score will reset ',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()


root.mainloop()