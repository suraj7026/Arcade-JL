from tkinter import *

root = Tk()
root.title('Instructions')
root.configure(bg='black')
root.geometry('1000x200')
root.iconbitmap("C:\\JL\\Justice_League_dc_comic_logo_movie-512.ico")

head = Label(root, text='Tiles(Instructions)', font=('Fixedsys', 40, 'normal'), fg='white', bg='black').pack()
mt = Label(root, text='', bg='black').pack()
pt1 = Label(root, text='ITS  A TWO PLAYER GAME',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt2 = Label(root, text='X chooses the tile first, then O does',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt3 = Label(root, text='Whoever connects three tiles in a straight line wins',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()



root.mainloop()