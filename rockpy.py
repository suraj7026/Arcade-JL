from tkinter import *
import random

rpy = Tk()
rpy.title("Rock Paper Scissors Lizard Spock")


click = True    

hrock = PhotoImage(file='rock.png')
hpaper = PhotoImage(file='Pap.png')
hscissors = PhotoImage(file='SCi.png')
hlizard = PhotoImage(file='Liz.png')
hspock = PhotoImage(file='Spock.png')

rock = PhotoImage(file='ROCKS.png')
paper = PhotoImage(file='APER.png')
scissors = PhotoImage(file='SCISS.png')
lizard = PhotoImage(file='Lizaard.png')
spock = PhotoImage(file='SPOCKH.png')
filr = PhotoImage(file='blank.png')

win = PhotoImage(file='WIN.png')
Loss = PhotoImage(file='LOSS.png')
tie = PhotoImage(file="TIE.png")

r = ''
p = ''
s = ''
l = ''
sp = ''


def game():
    global r,p,s,l,sp

    r = Button(rpy, image=hrock, command = lambda:user('rock'))
    r.grid(row=0,column=0)
    p = Button(rpy, image=hpaper, command = lambda:user('paper'))
    p.grid(row=0,column=1)
    s = Button(rpy, image=hscissors, command = lambda:user('scissors'))
    s.grid(row=0,column=2)
    l = Button(rpy, image=hlizard, command = lambda:user('lizard'))
    l.grid(row=0,column=3)
    sp = Button(rpy, image=hspock, command = lambda:user('spock'))
    sp.grid(row=0,column=4)

def comp():
    ch = random.choice(['rock','paper','scissors','lizard','spock'])
    return ch

def user(ychoice):
    global click

    computer = comp()

    if click == True:
        if ychoice == 'rock':
            r.configure(image = rock)
            if computer == 'rock':
                p.configure(image = rock)
                s.configure(image = filr)
                l.configure(image = filr)
                sp.configure(image = tie)
                click = False 
            elif computer == 'paper':
                p.configure(image = paper)
                s.configure(image = filr)
                l.configure(image = filr)
                sp.configure(image = Loss)
                click = False 
            elif computer == 'spock':
                p.configure(image = spock)
                s.configure(image = filr)
                l.configure(image = filr)
                sp.configure(image = Loss)
                click = False 
            elif computer == 'scissors':
                p.configure(image = scissors)
                s.configure(image = filr)
                l.configure(image = filr)
                sp.configure(image = win)
                click = False 
            elif computer == 'lizard':
                p.configure(image = lizard)
                s.configure(image = filr)
                l.configure(image = filr)
                sp.configure(image = win)
                click = False

        elif ychoice == 'paper':
            p.configure(image = paper)
            if computer == 'paper':
               s.configure(image = paper)
               r.configure(image = filr)
               l.configure(image = filr)
               sp.configure(image = tie)
               click = False 
            elif computer == 'scissors':
                s.configure(image = scissors)
                r.configure(image = filr)
                l.configure(image = filr)
                sp.configure(image = Loss)
                click = False 
            elif computer == 'lizard':
                s.configure(image = lizard)
                r.configure(image = filr)
                l.configure(image = filr)
                sp.configure(image = Loss)
                click = False 
            elif computer == 'rock':
                s.configure(image = rock)
                r.configure(image = filr)
                l.configure(image = filr)
                sp.configure(image = win)
                click = False 
            elif computer == 'spock':
                s.configure(image = spock)
                r.configure(image = filr)
                l.configure(image = filr)
                sp.configure(image = win)
                click = False

        elif ychoice == 'scissors':
            s.configure(image = scissors)
            if computer == 'scissors':
                l.configure(image = scissors)
                r.configure(image = filr)
                p.configure(image = filr)
                sp.configure(image = tie)
                click = False 
            elif computer == 'rock':
                l.configure(image = rock)
                r.configure(image = filr)
                p.configure(image = filr)
                sp.configure(image = Loss)
                click = False 
            elif computer == 'spock':
                l.configure(image = spock)
                r.configure(image = filr)
                p.configure(image = filr)
                sp.configure(image = Loss)
                click = False 
            elif computer == 'paper':
                l.configure(image = paper)
                r.configure(image = filr)
                p.configure(image = filr)
                sp.configure(image = win)
                click = False 
            elif computer == 'lizard':
                l.configure(image = lizard)
                r.configure(image = filr)
                p.configure(image = filr)
                sp.configure(image = win)
                click = False

        elif ychoice == 'lizard':
            l.configure(image = lizard)
            if computer == 'lizard':
                sp.configure(image = lizard)
                s.configure(image = filr)
                p.configure(image = filr)
                r.configure(image = tie)
                click = False 
            elif computer == 'scissors':
                sp.configure(image = scissors)
                s.configure(image = filr)
                p.configure(image = filr)
                
                r.configure(image = Loss)
                click = False 
            elif computer == 'rock':
                sp.configure(image = rock)
                s.configure(image = filr)
                p.configure(image = filr)
                r.configure(image = Loss)
                click = False 
            elif computer == 'spock':
                sp.configure(image = spock)
                s.configure(image = filr)
                p.configure(image = filr)
                r.configure(image = win)
                click = False 
            elif computer == 'paper':
                sp.configure(image = paper)
                r.configure(image = win)
                s.configure(image = filr)
                p.configure(image = filr)
                click = False

        elif ychoice == 'spock':
            sp.configure(image = spock)
            if computer == 'spock':
               l.configure(image = spock)
               s.configure(image = filr)
               p.configure(image = filr)                
               r.configure(image = tie)
               click = False 
            elif computer == 'paper':
                l.configure(image = paper)
                s.configure(image = filr)
                p.configure(image = filr) 
                r.configure(image = Loss)
                click = False 
            elif computer == 'lizard':
                l.configure(image = lizard)
                s.configure(image = filr)
                p.configure(image = filr) 
                r.configure(image = Loss)
                click = False 
            elif computer == 'scissors':
                l.configure(image = scissors)
                s.configure(image = filr)
                p.configure(image = filr) 
                r.configure(image = win)
                click = False 
            elif computer == 'rock':
                l.configure(image = rock)
                s.configure(image = filr)
                p.configure(image = filr) 
                r.configure(image = win)
                click = False
    else:
        if ychoice == 'rock' or ychoice == 'paper' or ychoice == 'scissors' or ychoice == 'lizard' or ychoice == 'spock':
            r.configure(image = hrock)
            p.configure(image = hpaper)
            s.configure(image = hscissors)
            l.configure(image = hlizard)
            sp.configure(image = hspock)
            click = True

            

            







game()


rpy.mainloop()