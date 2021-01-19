from tkinter import *

root = Tk()
root.title('Instructions')
root.configure(bg='black')
root.geometry('800x200')
root.iconbitmap("C:\\JL\\Justice_League_dc_comic_logo_movie-512.ico")

head = Label(root, text='Frogger(Instructions)', font=('Fixedsys', 40, 'normal'), fg='white', bg='black').pack()
mt = Label(root, text='', bg='black').pack()
pt1 = Label(root, text='ITS  A ONE PLAYER GAME',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt2 = Label(root, text='Get your frog across the obstacles to the victory line to WIN',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()




root.mainloop()