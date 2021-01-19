from tkinter import *

root = Tk()
root.title('Instructions')
root.configure(bg='black')
root.geometry('1200x250')
root.iconbitmap("C:\\JL\\Justice_League_dc_comic_logo_movie-512.ico")

head = Label(root, text='PONG(Instructions)', font=('Fixedsys', 40, 'normal'), fg='white', bg='black').pack()
mt = Label(root, text='', bg='black').pack()
pt1 = Label(root, text='IT’S A TWO PLAYER GAME. IT CAN ALSO BE PLAYED ALSO BE PLAYED ALONE (you just need to have good hand eye coordination :))',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt2 = Label(root, text='Each player will be assigned a bar which can be controlled with arrows(right) or the keys W FOR UP AND S FOR DOWN(left)',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt3 = Label(root, text='If the person does not defend the ball when it approaches them, the opponent gets a point.',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()
pt4 = Label(root, text='It’s a fun game played by people of all ages. HAVE FUN',  font=('Fixedsys', 15, 'normal'), fg='white', bg='black').pack()


root.mainloop()