import turtle
import time
import random
import pickle


#Score
score = 0
high_score = 0


win = turtle.Screen()
win.title("Collector")
win.bgcolor('black')

win.setup(width=1440,height=700)
win.tracer(0)

#BINS
bins = turtle.Turtle()
bins.speed(0)
bins.shape('square')
bins.shapesize(stretch_wid=1,stretch_len=5,outline=0.1)
bins.color('gray')
bins.penup()
bins.goto(0,-320)

#trash
x = random.randint(-710,710)


trash = turtle.Turtle()
trash.speed(0)
trash.shape("circle")
trash.color("gray")
trash.penup()
trash.goto(x,340)
trash.dy = 1.0


#Scoreboard

sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0,320)
sc.color('gray')
sc.write("Score : 0   High Score : 0", align = 'center', font = ("Fixedsys", 24, 'normal'))


#Function
def collector_right():
    x = bins.xcor()
    x += 30
    bins.setx(x)

def collector_left():
    x = bins.xcor()
    x -= 30
    bins.setx(x)


#navigation
win.listen()
win.onkeypress(collector_right,'Right')
win.onkeypress(collector_left,'Left')

while True:
    win.update()

    trash.sety(trash.ycor() - trash.dy)


    if score < 10:
        trash.dy = 0.5
    else:
        trash.dy = 1.0
    #collection
    if trash.ycor() < bins.ycor() and trash.xcor() < bins.xcor() + 50 and trash.xcor() > bins.xcor() - 50:
        x = random.randint(-710,710)
        trash.goto(x,340)
        score += 10
        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("Score : {}   High Score : {}".format(score,high_score), align = 'center', font = ("Fixedsys", 24, 'normal'))
    
    #oops you left it 
    if trash.ycor() < -340:
        time.sleep(1)
        x = random.randint(-710,710)
        trash.goto(x,340)
        score = 0
        sc.clear()
        sc.write("Score : {}   High Score : {}".format(score,high_score), align = 'center', font = ("Fixedsys", 24, 'normal'))
        bins.goto(0,-320)
    

    f = open('Collectscore.txt','wb')
    dicti = {'Collector' : high_score}
    pickle.dump(dicti,f)
    f.close()

win.mainloop()