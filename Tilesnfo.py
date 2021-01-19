from tkinter import *

root = Tk()
root.title('Instructions')
root.configure(bg='black')
root.geometry('1000x200')
root.iconbitmap("C:\\JL\\Justice_League_dc_comic_logo_movie-512.ico")

head = Label(root, text='Tiles(Instructions)', font=('Fixedsys', 40, 'normal'), fg='white', bg='black').pack()
mt = Label(root, text='', bg='black').pack()
pt1 = Label(root, text='ITS  A SINGLE PLAYER GAME',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt2 = Label(root, text='All you need to do, is to match numbers!',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt3 = Label(root, text='If you select a tile containing a number, you need to match it to its twin',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt4 = Label(root, text='Winning is possible when all the tiles are matched. GOOD LUCK!',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()


root.mainloop()