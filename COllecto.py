from tkinter import *

root = Tk()
root.title('Instructions')
root.configure(bg='black')
root.geometry('1000x220')
root.iconbitmap("C:\\JL\\Justice_League_dc_comic_logo_movie-512.ico")

head = Label(root, text='COLLECTOR(Instructions)', font=('Fixedsys', 40, 'normal'), fg='white', bg='black').pack()
mt = Label(root, text='', bg='black').pack()
pt1 = Label(root, text='ITS  A SINGLE PLAYER GAME',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt2 = Label(root, text='You have bin at the bottom of the screen',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt3 = Label(root, text='Trash will fall from the sky and you have to collect it ',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt4 = Label(root, text='If you miss any one, the game will reset',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt4 = Label(root, text="REAL LIFE ADVICE: Don't LITTER, Keep your surroundings clean." , font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()

root.mainloop()