import tkinter
import random
import time
import pickle
from tkinter import messagebox 

start=time.time()
root=tkinter.Tk()
root.title(" NUMBER TILES ")
root.geometry("610x610")
root.configure(bg='black')

MATCH_frame=tkinter.Frame(root)
MATCH_frame.pack()

tsc=0
sc=0
count=0
a_list=[]
a_dict={}
mlist=[1,1,2,2,3,3,4,4,5,5,6,6]


def openall():
        global win,MATCH_label,MATCH_frame,mlist
        B1=tkinter.Button(MATCH_frame, text=mlist[0],font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue")
        B2=tkinter.Button(MATCH_frame, text=mlist[1],font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue")
        B3=tkinter.Button(MATCH_frame, text=mlist[2],font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue")
        B4=tkinter.Button(MATCH_frame, text=mlist[3],font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue")
        B5=tkinter.Button(MATCH_frame, text=mlist[4],font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue")
        B6=tkinter.Button(MATCH_frame, text=mlist[5],font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue")
        B7=tkinter.Button(MATCH_frame, text=mlist[6],font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue")
        B8=tkinter.Button(MATCH_frame, text=mlist[7],font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue")
        B9=tkinter.Button(MATCH_frame, text=mlist[8],font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue")
        B10=tkinter.Button(MATCH_frame, text=mlist[9],font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue")
        B11=tkinter.Button(MATCH_frame, text=mlist[10],font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue")
        B12=tkinter.Button(MATCH_frame, text=mlist[11],font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue")

        B1.grid(row=0 , column=0)
        B2.grid(row=0 , column=1)
        B3.grid(row=0 , column=2)
        B4.grid(row=0 , column=3)

        B5.grid(row=1 , column=0)
        B6.grid(row=1 , column=1)
        B7.grid(row=1 , column=2)
        B8.grid(row=1 , column=3)

        B9.grid(row=2 , column=0)
        B10.grid(row=2 , column=1)
        B11.grid(row=2 , column=2)
        B12.grid(row=2 , column=3)
        if win!=6:
                MATCH_label.config(text=" START AGAIN ! ",font=("DigifaceWide", 12),bg="black",fg="white")
                MATCH_label.pack(pady=20)
                MATCH_frame.after(1000,play)
        elif win==6:
                MATCH_label.config(text=" RESET THE GAME TO PLAY AGAIN ! ",font=("DigifaceWide", 12),bg="black",fg="white")                
                MATCH_label.pack(pady=20)
        

def w():
        MATCH_label.config(text=" CONGRATS !!! YOU WIN !!! ",font=("DigifaceWide", 12),bg="black",fg="white")
        MATCH_label.pack(pady=20)

        global B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,tsc,sc
        l=[B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12]
        for z in l:
            z.config(bg="light green")
        global stop,start
        stop=time.time()
        print ("Time taken :",stop-start)
        sc=0
        
        if (stop-start)<=15:
                messagebox.showinfo("Time taken in seconds : ",stop-start)
                messagebox.showinfo("Points scored","50 \n You are a pro in this game")
                sc+=50
                tsc+=sc

        elif (stop-start)>15 and (stop-start)<=20:
                messagebox.showinfo("Time taken in seconds : ",stop-start)
                messagebox.showinfo("Points scored","40 \n Well done")
                sc+=40
                tsc+=sc

        elif (stop-start)>20 and (stop-start)<=30:
                messagebox.showinfo("Time taken in seconds : ",stop-start)
                messagebox.showinfo("Points scored","30 \n Good attempt")
                sc+=30
                tsc+=sc

        elif (stop-start)>30:
                messagebox.showinfo("Time taken in seconds : ",stop-start)
                messagebox.showinfo("Points scored","20 \n Be quick")
                sc+=20
                tsc+=sc

def play():
    global start,win
    start=time.time()
    win=0
    def button_click(b,number):
        global count, a_list, a_dict,mlist,win

        if b["text"]==" " and count<2:
            b["text"]=mlist[number]
            a_list.append(number)
            a_dict[b]=mlist[number]
            count+=1

        if(len(a_list))==2:
            if mlist[a_list[0]]==mlist[a_list[1]]:
                MATCH_label.config(text=" GREAT!! YOU HAVE MATCHED A NUMBER !! ",font=("DigifaceWide", 12),bg="black",fg="white" )
                MATCH_label.pack(pady=20)
                for key in a_dict:
                    key["state"]="disabled"
                count=0
                a_list=[]
                a_dict={}
                win+=1
                if win==6:
                        w()
            else:
                MATCH_label.config(text=" TRY AGAIN ! ",font=("DigifaceWide", 12),bg="black",fg="white")
                MATCH_label.pack(pady=20)
                count=0
                a_list=[]
                messagebox.showerror("ERROR ! ","Incorrect matching! ")
                for key in a_dict:
                    key["text"]=" "
                a_dict={}

                
    global B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12
    B1=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B1,0))
    B2=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B2,1))
    B3=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B3,2))
    B4=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B4,3))
    B5=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B5,4))
    B6=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B6,5))
    B7=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B7,6))
    B8=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B8,7))
    B9=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B9,8))
    B10=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B10,9))
    B11=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B11,10))
    B12=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B12,11))

    B1.grid(row=0 , column=0)
    B2.grid(row=0 , column=1)
    B3.grid(row=0 , column=2)
    B4.grid(row=0 , column=3)

    B5.grid(row=1 , column=0)
    B6.grid(row=1 , column=1)
    B7.grid(row=1 , column=2)
    B8.grid(row=1 , column=3)

    B9.grid(row=2 , column=0)
    B10.grid(row=2 , column=1)
    B11.grid(row=2 , column=2)
    B12.grid(row=2 , column=3)
        
def reset():
    global start,win
    start=time.time()
    win=0
    global mlist
    random.shuffle(mlist)
    
    def button_click(b,number):
        global count, a_list, a_dict,mlist,win

        if b["text"]==" " and count<2:
            b["text"]=mlist[number]
            a_list.append(number)
            a_dict[b]=mlist[number]
            count+=1

        if(len(a_list))==2:
            if mlist[a_list[0]]==mlist[a_list[1]]:
                MATCH_label.config(text=" GREAT!! YOU HAVE MATCHED A NUMBER !! ",font=("DigifaceWide", 12),bg="black",fg="white" )
                MATCH_label.pack(pady=20)
                for key in a_dict:
                    key["state"]="disabled"
                count=0
                a_list=[]
                a_dict={}
                win+=1
                if win==6:
                        w()
            else:
                MATCH_label.config(text=" TRY AGAIN ! ",font=("DigifaceWide", 12),bg="black",fg="white")
                MATCH_label.pack(pady=20)
                count=0
                a_list=[]
                messagebox.showerror("ERROR ! ","Incorrect matching! ")
                for key in a_dict:
                    key["text"]=" "
                a_dict={}
                
    global B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12
    B1=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B1,0))
    B2=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B2,1))
    B3=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B3,2))
    B4=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B4,3))
    B5=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B5,4))
    B6=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B6,5))
    B7=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B7,6))
    B8=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B8,7))
    B9=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B9,8))
    B10=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B10,9))
    B11=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B11,10))
    B12=tkinter.Button(MATCH_frame, text=" ",font=("DigifaceWide", 24) , height=4 , width=6 ,bg="orange",fg="dark blue", command=lambda: button_click(B12,11))

    B1.grid(row=0 , column=0)
    B2.grid(row=0 , column=1)
    B3.grid(row=0 , column=2)
    B4.grid(row=0 , column=3)

    B5.grid(row=1 , column=0)
    B6.grid(row=1 , column=1)
    B7.grid(row=1 , column=2)
    B8.grid(row=1 , column=3)

    B9.grid(row=2 , column=0)
    B10.grid(row=2 , column=1)
    B11.grid(row=2 , column=2)
    B12.grid(row=2 , column=3)

    global MATCH_label
    MATCH_label.config(text=" START MATCHING THE NUMBERS ",font=("DigifaceWide", 12),bg="black",fg="white")
    MATCH_label.pack(pady=20)

MATCH_label= tkinter.Label(root, text=" START MATCHING THE NUMBERS ",font=("DigifaceWide", 12),bg="black",fg="white")
MATCH_label.pack(pady=20)
    
    
MATCH_menu=tkinter.Menu(root)
root.config(menu=MATCH_menu)

options_menu=tkinter.Menu(MATCH_menu, tearoff=False)
MATCH_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)
options_menu.add_command(label="Exit Game", command=quit)
options_menu.add_command(label="Open all", command=openall)

reset()
root.mainloop()

f=open('TILEscore.txt','wb')
dicti={'TILES':tsc}
pickle.dump(dicti,f)
f.close()