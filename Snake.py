import turtle
import time
import random
import pickle
delay = 0.1
sc = 0
hsc = 0

# Screen

win = turtle.Screen()
win.title("Snake")
win.bgcolor('black')
win.setup(width=1080,height=720)
win.tracer(0)

# Snake
Snake = turtle.Turtle()
Snake.speed(0)
Snake.shape("square")
Snake.color("red")
Snake.penup()
Snake.goto(-530,350)
Snake.direction = 'stop'

# Apple
x = random.randint(-530,530)
y = random.randint(-350,350)


apple = turtle.Turtle()
apple.speed(0)
apple.shape("square")
apple.color("green")
apple.penup()
apple.goto(x,y)

BODIES = []

# Scorebar

score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,320)
score.write("Score : 0   High Score : 0", align = 'center', font = ("Fixedsys", 24, 'normal'))




# Functions
def move():
    if Snake.direction == 'up':
        y = Snake.ycor()
        Snake.sety(y+20)

    
    if Snake.direction == 'down':
        y = Snake.ycor()
        Snake.sety(y-20)

    
    if Snake.direction == 'left':
        x = Snake.xcor()
        Snake.setx(x-20)

    
    if Snake.direction == 'right':
        x = Snake.xcor()
        Snake.setx(x+20)

def One_batch():
    if Snake.direction != 'down':
        Snake.direction = "up"

def two_batch():
    if Snake.direction != 'up':
        Snake.direction = "down"

def Penny():
    if Snake.direction != 'right':
        Snake.direction = "left"


def and_dime():
    if Snake.direction != 'left':
        Snake.direction = "right"



#KEYS
win.listen()
win.onkeypress(One_batch,"Up")
win.onkeypress(two_batch,"Down")
win.onkeypress(Penny,"Left")
win.onkeypress(and_dime,"Right")



#Main


while True:
    win.update()

    #Border Dash

    if Snake.xcor() > 530 or Snake.xcor() < -530 or Snake.ycor() > 350 or Snake.ycor() < -350:
        time.sleep(1)
        Snake.goto(-530,350)
        Snake.direction = 'stop'

        for b in BODIES:
            b.goto(10000,10000)
        
        BODIES.clear()
        sc = 0
        score.clear()
        score.write("Score : {}   High Score : {}".format(sc,hsc), align = 'center', font = ("Fixedsys", 24, 'normal'))




    
    #Eating
    if Snake.distance(apple) < 20:
        x = random.randint(-530,530)
        y = random.randint(-350,350)
        apple.goto(x,y)

        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("red")
        body.penup()
        BODIES.append(body)

        #Scoreadding
        sc += 10
        if sc > hsc:
            hsc = sc
        score.clear()
        score.write("Score : {}   High Score : {}".format(sc,hsc), align = 'center', font = ("Fixedsys", 24, 'normal'))

    #Follow
    for i in range(len(BODIES)-1,0,-1):
        x = BODIES[i-1].xcor()
        y = BODIES[i-1].ycor()
        BODIES[i].goto(x,y)

    if len(BODIES) > 0:
        y = Snake.ycor()
        x = Snake.xcor()
        BODIES[0].goto(x,y)









    move()

    for o in BODIES:
        if o.distance(Snake) < 20:
            time.sleep(1)
            Snake.goto(-530,350)
            Snake.direction = 'stop'
            
            for b in BODIES:
                b.goto(10000,10000)
        
            BODIES.clear()

            sc = 0
            score.clear()
            score.write("Score : {}   High Score : {}".format(sc,hsc), align = 'center', font = ("Fixedsys", 24, 'normal'))

    f = open('Snakescore.txt','wb')
    dicti = {'snake' : hsc}
    pickle.dump(dicti,f)
    f.close()

    

    

    



    time.sleep(delay)

win.mainloop()