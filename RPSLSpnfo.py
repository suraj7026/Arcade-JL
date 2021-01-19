from tkinter import *

root = Tk()
root.title('Instructions')
root.configure(bg='black')
root.geometry('1500x350')
root.iconbitmap("C:\\JL\\Justice_League_dc_comic_logo_movie-512.ico")

head = Label(root, text='Rock Paper Scissors Lizard Spock(Instructions)', font=('Fixedsys', 40, 'normal'), fg='white', bg='black').pack()
mt = Label(root, text='', bg='black').pack()
pt1 = Label(root, text='ITS  A ONE PLAYER GAME',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt2 = Label(root, text='Scissors cuts Paper',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt3 = Label(root, text='Paper covers Rock',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt4 = Label(root, text='Rock crushes Lizard',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt5 = Label(root, text='Lizard poisons Spock',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt6 = Label(root, text='Spock smashes Scissors',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt7 = Label(root, text='Scissors decapitates Lizard',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt8 = Label(root, text='Lizard eats Paper',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt9 = Label(root, text='Paper disproves Spock',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt10 = Label(root, text='Spock vaporizes Rock',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt11 = Label(root, text='(and as it always has) Rock crushes Scissors',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()




root.mainloop()