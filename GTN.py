from tkinter import *
import random as rn
import pickle
root = Tk()
root.title("guess the Number")
root.configure(bg = 'black')
root.geometry("1000x500")
n = 0

heading = Label(root, text="Try to guess the number between 1 - 50", font=("arial",40,"bold"), fg="steelblue",bg = 'black').pack()
sub_heading = Label(root, text="You have 10 Chances to get it right", font=("arial",36,"bold"), fg="steelblue",bg = 'black').pack()


gstxt = Label(root, text="Take your guess", font=("arial", 20),fg="steelblue",bg = 'black')
gstxt.place(x=210,y=200)
entry_box = Entry(root, width=25, fg="steelblue",bg='black')
entry_box.place(x=480,y=210)
Number = rn.randint(1,50)
NOG = 0
def submit():
  global NOG,n,Sub
  NOG += 1
  n += 1
  if n<10:
      num = int(entry_box.get())
      try:
        if num > Number:
          op = Label(root, text=' You are too High ',font=("arial",15),fg="steelblue",bg = 'black')
          op.place(x=360,y=400)
          entry_box.delete(0,"end")
        elif num < Number:
          op = Label(root, text=" You are too Low ",font=("arial",15),fg="steelblue",bg = 'black')
          op.place(x=360,y=400)
          entry_box.delete(0,"end")
        elif num == Number:
          op = Label(root, text=' Yay You got it right !! ',font=("arial",15),fg="steelblue",bg = 'black')
          op.place(x=360,y=400)
          f = open('GTNscore.txt','wb')
          dicti = {'GTN' : n*10}
          pickle.dump(dicti,f)
          f.close()
          entry_box.delete(0,"end")
          txt = Label(root, text="Game over!! Restart the game to play again", font=("arial", 20),fg="steelblue",bg = 'black')
          txt.place(x=360,y=450)
          Sub.configure(state='disabled')
      except ValueError:
        op = Label(root,text="Invalid number",font=("arial",15),fg="steelblue",bg = 'black')
        op.place(x=360,y=400)
        entry_box.delete(0,"end")

  elif n==10:
      num = int(entry_box.get())
      try:
        if num > Number:
          op = Label(root, text=' You are too High ',font=("arial",15),fg="steelblue",bg = 'black')
          op.place(x=360,y=400)
          entry_box.delete(0,"end")
        elif num < Number:
          op = Label(root, text=" You are too Low ",font=("arial",15),fg="steelblue",bg = 'black')
          op.place(x=360,y=400)
          
          entry_box.delete(0,"end")
        elif num == Number:
          op = Label(root, text='Yay You got it right!!',font=("arial",15),fg="steelblue",bg = 'black')
          op.place(x=360,y=400)
          entry_box.delete(0,"end")
          txt = Label(root, text="Game over!! Restart the game to play again", font=("arial", 20),fg="steelblue",bg = 'black')
          txt.place(x=360,y=450)
          Sub.configure(state='disabled')
      except ValueError:
        op = Label(root,text="Invalid number",font=("arial",15),fg="steelblue",bg = 'black')
        op.place(x=360,y=400)
        entry_box.delete(0,"end")
      entry_box.delete(0,"end")
      txt = Label(root, text="Your 10 chances are over!! Restart the game to play again", font=("arial", 20),fg="steelblue",bg = 'black')
      txt.place(x=360,y=450)
      Sub.configure(state='disabled')
        
  

Sub= Button(root, text="Submit", width=10, height=2, bg="steel Blue", fg='white', command=submit)
Sub.place(x=450,y=300)

root.mainloop()