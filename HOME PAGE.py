from tkinter import *

import os

root = Tk()
root.title("Arcade")
root.geometry('1440x720')
root.iconbitmap("C:\\JL\\Justice_League_dc_comic_logo_movie-512.ico")
root.configure(bg='black')


t = 0

arcade = Label(root,text='Arcade', font=('Fixedsys', 70,'bold'), fg='white', bg='black').pack()
JLg = Label(root,text='  -By JL Games', font=('Fixedsys', 20,'bold'), fg='white', bg='black').pack()


# TICTACTOE
def tic_tac_toe():
    os.system('python TICTACTOE.py')
    
tictactoe = Button(root,text='TIC TAC TOE',font=('Fixedsys', 12), width = 12, height = 3, bg='white', command=tic_tac_toe)
tictactoe.place(x = 500,y = 240)

def tttinf():
    os.system('python TICTACTOEINS.py')
    
tictactoei = Button(root,text='i',font=('Fixedsys', 12), width = 2, height = 3, bg='white', command=tttinf)
tictactoei.place(x = 605,y = 240)
    

#GTN
def guessthenumber():
    os.system('python GTN.py')
    
GTn = Button(root,text='GTN',font=('Fixedsys', 12), width = 12, height = 3, bg='white', command=guessthenumber)
GTn.place(x=200, y=240)
def GTNinfo():
    os.system('python GTNfo.py')
    
GTnfo = Button(root,text='i',font=('Fixedsys', 12), width = 2, height = 3, bg='white', command=GTNinfo)
GTnfo.place(x=305, y=240)


#Snake
def snake():
    os.system('python Snake.py')
    

snakes = Button(root,text='Snake',font=('Fixedsys', 12), width = 12, height = 3, bg='white', command=snake)
snakes.place(x = 200,y = 440)


def Insnake():
    os.system('python Snakefo.py')
    
snakesy = Button(root,text='i',font=('Fixedsys', 12), width = 2, height = 3, bg='white', command=Insnake)
snakesy.place(x = 305,y = 440)


#Collector
def Collector():
    os.system('python COLLECTOR.py')
    

collect = Button(root,text='Collector',font=('Fixedsys', 12), width = 12, height = 3, bg='white', command=Collector)
collect.place(x = 800,y = 440)

def Collecto():
    os.system('python COllecto.py')
    
collect0 = Button(root,text='i',font=('Fixedsys', 12), width = 2, height = 3, bg='white', command=Collecto)
collect0.place(x = 905,y = 440)


#RPSLSp
def RPSp():
    os.system('python rockpy.py')



rpslsp = Button(root,text='RPSLSp',font=('Fixedsys', 12), width = 12, height = 3, bg='white', command=RPSp)
rpslsp.place(x = 1100,y = 440)

def rockinfo():
    ### jbvbxbfhgbf
    print()
scorei = Button(root,text='i',font=('Fixedsys', 12), width = 2, height = 3, bg='white', command=rockinfo)
scorei.place(x = 1205,y = 440)


#TILES
def Tiles():
    os.system('python TILES.py')

tiles = Button(root,text='Tiles',font=('Fixedsys', 12), width = 12, height = 3, bg='white', command=Tiles)
tiles.place(x = 1100,y = 240)

def Tilesinfo():
    os.system('python Tilesnfo.py')

Tilesi = Button(root,text='i',font=('Fixedsys', 12), width = 2, height = 3, bg='white', command=Tilesinfo)
Tilesi.place(x = 1205,y = 240)
#Frogger

def frogger():
    os.system('python Froggy.py')
    

ng = Button(root,text='Frogger',font=('Fixedsys', 12), width = 12, height = 3, bg='white', command=frogger)
ng.place(x = 800,y = 240)

def nginfo():
    os.system('python hangnfo.py')
    

ngi = Button(root,text='i',font=('Fixedsys', 12), width = 2, height = 3, bg='white', command=nginfo)
ngi.place(x = 905,y = 240)

#PONG
def PONG():
    os.system('python Pong.py')
    

pongs = Button(root,text='Pong',font=('Fixedsys', 12), width = 12, height = 3, bg='white', command=PONG)
pongs.place(x = 500,y = 440)

def PONGinfo():
    os.system('python Pongnfo.py')
    

pongs = Button(root,text='i',font=('Fixedsys', 12), width = 2, height = 3, bg='white', command=PONGinfo)
pongs.place(x = 605,y = 440)


#Score board
def Score_b():
    os.system('python Scoreboard.py')
    

scores = Button(root,text='Score Board',font=('Fixedsys', 12), width = 12, height = 3, bg='white', command=Score_b)
scores.place(x = 650,y = 590)

def scoreinfo():
    os.system('python Scoreinfo.py')
   

scorei = Button(root,text='i',font=('Fixedsys', 12), width = 2, height = 3, bg='white', command=scoreinfo)
scorei.place(x = 755,y = 590)


root.mainloop()