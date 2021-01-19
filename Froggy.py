import turtle
import time

#Screen
win  = turtle.Screen()
win.title("Frogger")
win.bgcolor('black')
win.setup(height=700,width=1080)


#Frog
frog = turtle.Turtle()
frog.speed(0)
frog.shape('square')
frog.shapesize(stretch_wid=2,stretch_len=2,outline=0.1)
frog.color('green')
frog.penup()
frog.goto(0,-320)


#movement
def jump_forward():
    y = frog.ycor()
    y += 40
    frog.sety(y)

def jump_backward():
    y = frog.ycor()
    y -= 40
    frog.sety(y)
 
def jump_right():
    x = frog.xcor()
    x += 40
    frog.setx(x)

def jump_left():
    x = frog.xcor()
    x -= 40
    frog.setx(x)

win.listen()
win.onkeypress(jump_forward,'Up')
win.onkeypress(jump_backward,'Down')
win.onkeypress(jump_right,'Right')
win.onkeypress(jump_left,'Left')

#Obsacle 1
ob1 = turtle.Turtle()
ob1.speed(0)
ob1.shape('square')
ob1.shapesize(stretch_wid=2,stretch_len=10,outline=0.1)
ob1.color('burlywood4')
ob1.penup()
ob1.goto(-435,-160)
ob1.dx = 120

#Obsacle 2
ob2 = turtle.Turtle()
ob2.speed(0)
ob2.shape('square')
ob2.shapesize(stretch_wid=2,stretch_len=10,outline=0.1)
ob2.color('burlywood4')
ob2.penup()
ob2.goto(435,-40)
ob2.dx = 135

#Obsacle 3
ob3 = turtle.Turtle()
ob3.speed(0)
ob3.shape('square')
ob3.shapesize(stretch_wid=2,stretch_len=10,outline=0.1)
ob3.color('burlywood4')
ob3.penup()
ob3.goto(-435,80)
ob3.dx = 140

#Obsacle 4
ob4 = turtle.Turtle()
ob4.speed(0)
ob4.shape('square')
ob4.shapesize(stretch_wid=2,stretch_len=10,outline=0.1)
ob4.color('burlywood4')
ob4.penup()
ob4.goto(435,200)
ob4.dx = 155




#Victory line
vic = turtle.Turtle()
vic.speed(0)
vic.shape('square')
vic.shapesize(stretch_wid=2,stretch_len=105,outline=0.1)
vic.color('white')
vic.penup()
vic.goto(510,327)


#Mainloop
while True:
    win.update()

    
    #Obstacles movement

    ob1.setx(ob1.xcor() + ob1.dx)
    ob2.setx(ob2.xcor() - ob2.dx)
    ob3.setx(ob3.xcor() + ob3.dx)
    ob4.setx(ob4.xcor() - ob4.dx)
    

    #Border
    if ob1.xcor() > 430:
        ob1.setx(430)
        ob1.dx *= -1

    elif ob1.xcor() < -430:
        ob1.setx(-430)
        ob1.dx *= -1

    if ob2.xcor() > 430:
        ob2.setx(430)
        ob2.dx *= -1

    elif ob2.xcor() < -430:
        ob2.setx(-430)
        ob2.dx *= -1


    if ob3.xcor() > 430:
        ob3.setx(430)
        ob3.dx *= -1

    elif ob3.xcor() < -430:
        ob3.setx(-430)
        ob3.dx *= -1


    if ob4.xcor() > 430:
        ob4.setx(430)
        ob4.dx *= -1

    elif ob4.xcor() < -430:
        ob4.setx(-430)
        ob4.dx *= -1


    

    if frog.xcor() <= -520:
        frog.setx(-520)
    
    elif frog.xcor() >= 520:
        frog.setx(520)
    

    #Collisions
    if ob1.distance(frog) < 35:
        frog.goto(0,500)
        ob1.goto(0,500)
        ob2.goto(0,500)
        ob3.goto(0,500)
        ob4.goto(0,500)
        vic.goto(0,500)

        score1 = turtle.Turtle()
        score1.speed(0)
        score1.shape("square")
        score1.color("white")
        score1.hideturtle()
        score1.penup()
        score1.goto(0,0)
        score1.write("You were squashed like a bug on a windsheild", align = 'center', font = ("Fixedsys", 29, 'normal'))
        time.sleep(3)
        score1.clear()
        score1.write("Restart the game", align = 'center', font = ("Fixedsys", 29, 'normal'))
        break

    if ob2.distance(frog) < 35:
        frog.goto(0,500)
        ob1.goto(0,500)
        ob2.goto(0,500)
        ob3.goto(0,500)
        ob4.goto(0,500)
        vic.goto(0,500)

        score1 = turtle.Turtle()
        score1.speed(0)
        score1.shape("square")
        score1.color("white")
        score1.hideturtle()
        score1.penup()
        score1.goto(0,0)
        score1.write("You were squashed like a bug on a windsheild", align = 'center', font = ("Fixedsys", 29, 'normal'))
        time.sleep(3)
        score1.clear()
        score1.write("Restart the game", align = 'center', font = ("Fixedsys", 29, 'normal'))
        break

    if ob3.distance(frog) < 35:
        frog.goto(0,500)
        ob1.goto(0,500)
        ob2.goto(0,500)
        ob3.goto(0,500)
        ob4.goto(0,500)
        vic.goto(0,500)

        score1 = turtle.Turtle()
        score1.speed(0)
        score1.shape("square")
        score1.color("white")
        score1.hideturtle()
        score1.penup()
        score1.goto(0,0)
        score1.write("You were squashed like a bug on a windsheild", align = 'center', font = ("Fixedsys", 29, 'normal'))
        time.sleep(3)
        score1.clear()
        score1.write("Restart the game", align = 'center', font = ("Fixedsys", 29, 'normal'))
        break
    
    if ob4.distance(frog) < 35:
        frog.goto(0,500)
        ob1.goto(0,500)
        ob2.goto(0,500)
        ob3.goto(0,500)
        ob4.goto(0,500)
    
        vic.goto(0,500)

        score1 = turtle.Turtle()
        score1.speed(0)
        score1.shape("square")
        score1.color("white")
        score1.hideturtle()
        score1.penup()
        score1.goto(0,0)
        score1.write("You were squashed like a bug on a windsheild", align = 'center', font = ("Fixedsys", 29, 'normal'))
        time.sleep(3)
        score1.clear()
        score1.write("Restart the game", align = 'center', font = ("Fixedsys", 29, 'normal'))
        break



    #Victory
    y = frog.ycor()
    if y >= 320:
        frog.goto(0,500)
        ob1.goto(0,500)
        ob2.goto(0,500)
        ob3.goto(0,500)
        ob4.goto(0,500)
        
        vic.goto(0,500)

        score = turtle.Turtle()
        score.speed(0)
        score.shape("square")
        score.color("white")
        score.hideturtle()
        score.penup()
        score.goto(0,0)
        score.write("VICTORY!!!", align = 'center', font = ("Fixedsys", 44, 'normal'))
        break



win.mainloop()