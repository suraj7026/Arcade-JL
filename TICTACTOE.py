import tkinter
from tkinter import messagebox


root=tkinter.Tk()
root.title(" Tic-Tac-Toe!!! ")
root.configure(bg='black')

root.geometry("460x610")

click=True
count=0

tic_tac_toe_frame=tkinter.Frame(root)
tic_tac_toe_frame.pack()

def disable():
    b0.config(state="disabled")
    b1.config(state="disabled")
    b2.config(state="disabled")
    b3.config(state="disabled")
    b4.config(state="disabled")
    b5.config(state="disabled")
    b6.config(state="disabled")
    b7.config(state="disabled")
    b8.config(state="disabled")

def checkifwon():
    global win
    win=False
    
    #FOR X 
    if b0["text"]=="X" and b1["text"]=="X" and b2["text"]=="X":
        b0.config(bg="red")
        b1.config(bg="red")
        b2.config(bg="red")
        win=True
        messagebox.showinfo(" Tic Tac Toe!!!", "CONGRATULATIONS!!!  X Wins!! ")
        disable()

    elif b3["text"]=="X" and b4["text"]=="X" and b5["text"]=="X":
        b3.config(bg="red")
        b4.config(bg="red")
        b5.config(bg="red")
        win=True
        messagebox.showinfo(" Tic Tac Toe!!!", "CONGRATULATIONS!!!  X Wins!! ")
        disable()

    elif b6["text"]=="X" and b7["text"]=="X" and b8["text"]=="X":
        b6.config(bg="red")
        b7.config(bg="red")
        b8.config(bg="red")
        win=True
        messagebox.showinfo(" Tic Tac Toe!!!", "CONGRATULATIONS!!!  X Wins!! ")
        disable()

    elif b0["text"]=="X" and b3["text"]=="X" and b6["text"]=="X":
        b0.config(bg="red")
        b3.config(bg="red")
        b6.config(bg="red")
        win=True
        messagebox.showinfo(" Tic Tac Toe!!!", "CONGRATULATIONS!!!  X Wins!! ")
        disable()

    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        win=True
        messagebox.showinfo(" Tic Tac Toe!!!", "CONGRATULATIONS!!!  X Wins!! ")
        disable()

    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        win=True
        messagebox.showinfo(" Tic Tac Toe!!!", "CONGRATULATIONS!!!  X Wins!! ")
        disable()

    elif b0["text"]=="X" and b4["text"]=="X" and b8["text"]=="X":
        b0.config(bg="red")
        b4.config(bg="red")
        b8.config(bg="red")
        win=True
        messagebox.showinfo(" Tic Tac Toe!!!", "CONGRATULATIONS!!!  X Wins!! ")
        disable()

    elif b2["text"]=="X" and b4["text"]=="X" and b6["text"]=="X":
        b2.config(bg="red")
        b4.config(bg="red")
        b6.config(bg="red")
        win=True
        messagebox.showinfo(" Tic Tac Toe!!!", "CONGRATULATIONS!!!  X Wins!! ")
        disable()

    #FOR O
    if b0["text"]=="O" and b1["text"]=="O" and b2["text"]=="O":
        b0.config(bg="red")
        b1.config(bg="red")
        b2.config(bg="red")
        win=False
        messagebox.showinfo(" Tic Tac Toe!!!", "CONGRATULATIONS!!!  O Wins!! ")
        disable()

    elif b3["text"]=="O" and b4["text"]=="O" and b5["text"]=="O":
        b3.config(bg="red")
        b4.config(bg="red")
        b5.config(bg="red")
        win=True
        messagebox.showinfo(" Tic Tac Toe!!!", "CONGRATULATIONS!!!  O Wins!! ")
        disable()

    elif b6["text"]=="O" and b7["text"]=="O" and b8["text"]=="O":
        b6.config(bg="red")
        b7.config(bg="red")
        b8.config(bg="red")
        win=True
        messagebox.showinfo(" Tic Tac Toe!!!", "CONGRATULATIONS!!!  O Wins!! ")
        disable()

    elif b0["text"]=="O" and b3["text"]=="O" and b6["text"]=="O":
        b0.config(bg="red")
        b3.config(bg="red")
        b6.config(bg="red")
        win=True
        messagebox.showinfo(" Tic Tac Toe!!!", "CONGRATULATIONS!!!  O Wins!! ")
        disable()

    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        win=True
        messagebox.showinfo(" Tic Tac Toe!!!", "CONGRATULATIONS!!!  O Wins!! ")
        disable()

    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        win=True
        messagebox.showinfo(" Tic Tac Toe!!!", "CONGRATULATIONS!!!  O Wins!! ")
        disable()

    elif b0["text"]=="O" and b4["text"]=="O" and b8["text"]=="O":
        b0.config(bg="red")
        b4.config(bg="red")
        b8.config(bg="red")
        win=True
        messagebox.showinfo(" Tic Tac Toe!!!", "CONGRATULATIONS!!!  O Wins!! ")
        disable()

    elif b2["text"]=="O" and b4["text"]=="O" and b6["text"]=="O":
        b2.config(bg="red")
        b4.config(bg="red")
        b6.config(bg="red")
        win=True
        messagebox.showinfo(" Tic Tac Toe!!!", "CONGRATULATIONS!!!  O Wins!! ")
        disable()

    elif count==9 and win==False:
         messagebox.showinfo(" Tic Tac Toe!!!"," It's a tie!!! \n No one wins!!! " )
         disable()
def button_click(b):
    global click,count,tic_tac_toe_label
    if b["text"] == " " and click==True:
        b["text"]="X"
        tic_tac_toe_label.config(text="O's TURN",font=("DigifaceWide", 12),bg="black",fg="gold")
        click=False
        count+=1
        checkifwon()
    elif b["text"] == " " and click==False:
        b["text"]="O"
        tic_tac_toe_label.config(text="X's TURN",font=("DigifaceWide", 12),bg="black",fg="gold")
        click=True
        count+=1
        checkifwon()
    else: 
        messagebox.showerror("Tic Tac Toe!!!", "Hey! That box has already been used \n Try choosing another box....")
        
def reset():
    global b0,b1,b2,b3,b4,b5,b6,b7,b8
    global click, count
    click=True
    count=0
    
    b0=tkinter.Button(tic_tac_toe_frame, text=" ",font=("Fixedsys", 24) , height=4 , width=6 ,bg="cyan",fg="dark blue", command=lambda: button_click(b0))
    b1=tkinter.Button(tic_tac_toe_frame, text=" ",font=("Fixedsys", 24), height=4 , width=6 ,bg="cyan",fg="dark blue", command=lambda: button_click(b1))
    b2=tkinter.Button(tic_tac_toe_frame, text=" ",font=("Fixedsys", 24) , height=4 , width=6 ,bg="cyan",fg="dark blue", command=lambda: button_click(b2))
    b3=tkinter.Button(tic_tac_toe_frame, text=" ",font=("Fixedsys", 24) , height=4 , width=6 ,bg="cyan",fg="dark blue", command=lambda: button_click(b3))
    b4=tkinter.Button(tic_tac_toe_frame, text=" ",font=("Fixedsys", 24) , height=4 , width=6 ,bg="cyan",fg="dark blue", command=lambda: button_click(b4))
    b5=tkinter.Button(tic_tac_toe_frame, text=" ",font=("Fixedsys", 24) , height=4 , width=6 ,bg="cyan",fg="dark blue", command=lambda: button_click(b5))
    b6=tkinter.Button(tic_tac_toe_frame, text=" ",font=("Fixedsys", 24) , height=4 , width=6 ,bg="cyan",fg="dark blue", command=lambda: button_click(b6))
    b7=tkinter.Button(tic_tac_toe_frame, text=" ",font=("Fixedsys", 24) , height=4 , width=6 ,bg="cyan",fg="dark blue", command=lambda: button_click(b7))
    b8=tkinter.Button(tic_tac_toe_frame, text=" ",font=("Fixedsys", 24) , height=4 , width=6 ,bg="cyan",fg="dark blue", command=lambda: button_click(b8))
    
    b0.grid(row=0 , column=0)
    b1.grid(row=0 , column=1)
    b2.grid(row=0 , column=2)

    b3.grid(row=1 , column=0)
    b4.grid(row=1 , column=1)
    b5.grid(row=1 , column=2)

    b6.grid(row=2 , column=0)
    b7.grid(row=2 , column=1)
    b8.grid(row=2 , column=2)

    global tic_tac_toe_label
    tic_tac_toe_label.config(text=" Tic Tac Toe!!! X SHOULD START PLAYING FIRST!!! ",font=("DigifaceWide", 12),bg="black",fg="gold")
     
    
tic_tac_toe_label=tkinter.Label(root,text=" Tic Tac Toe!!! X SHOULD START PLAYING FIRST!!! ",font=("DigifaceWide", 12),bg="black",fg="gold")
tic_tac_toe_label.pack(pady=20)

tic_tac_toe_menu=tkinter.Menu(root)
root.config(menu=tic_tac_toe_menu)

options_menu=tkinter.Menu(tic_tac_toe_menu, tearoff=False)
tic_tac_toe_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)
options_menu.add_command(label="Exit Game", command=quit)
reset()
root.mainloop()