from tkinter import *
import pickle

list = []
with open('Snakescore.txt','rb') as scb:
    l = pickle.load(scb)
    
    list.append(l)

with open('Collectscore.txt','rb') as cscb:
    m = pickle.load(cscb)
    
    list.append(m)

with open('GTNscore.txt','rb') as Gscb:
    n = pickle.load(Gscb)
    
    
    list.append(n)


with open('TILEscore.txt','rb') as Tscb:
    o = pickle.load(Tscb)
    
    list.append(o)



root = Tk()
root.title("SCORE BOARD")
root.configure(bg='black')
root.geometry('400x400')
root.iconbitmap("C:\\JL\\Justice_League_dc_comic_logo_movie-512.ico")
title = Label(root, text='SCORE BOARD', font=('Fixedsys', 35, 'normal'), fg='white', bg='black').pack()
Gtn = Label(root, text='Guess the Number : {}'.format(n['GTN']), font=('Fixedsys', 15, 'normal'), fg='white', bg='black')
Gtn.place(x = 80, y = 120)
tiles = Label(root, text='Tiles            : {}'.format(o['TILES']), font=('Fixedsys', 15, 'normal'), fg='white', bg='black')
tiles.place(x = 80, y = 170)
Snake = Label(root, text='Snake            : {}'.format(l['snake']), font=('Fixedsys', 15, 'normal'), fg='white', bg='black')
Snake.place(x = 80, y = 220)
Collector = Label(root, text='Collector        : {}'.format(m['Collector']), font=('Fixedsys', 15, 'normal'), fg='white', bg='black')
Collector.place(x = 80, y = 270)
 

root.mainloop()