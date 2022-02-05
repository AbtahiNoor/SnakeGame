import turtle as t
#import os


win = t.Screen()    # creating a window
win.title("Snake Game") # Giving name to the game.
win.bgcolor('black')    # providing color to the HomeScreen
win.setup(width=800,height=600) # Size of the game panel 
win.tracer(0)   # which speed up's the game.


ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
#ball.penup()
ball.goto(0,0)
#ball_dx = 0.5 # Setting up the pixels for the ball movement.
#ball_dy = 0.5

def paddle_up():
    y = ball.ycor()
    y = y + 15
    ball.sety(y)

# Moving the left paddle down

def paddle_down():
    y = ball.ycor()
    y = y - 15
    ball.sety(y)

# Moving the right paddle up

def paddle_right():
    x = ball.xcor()
    x = x + 15
    ball.setx(x)

# Moving right paddle down

def paddle_left():
    x = ball.xcor()
    x = x - 15
    ball.setx(x)

win.listen()
win.onkeypress(paddle_up,"Up")
win.onkeypress(paddle_down,"Down")
win.onkeypress(paddle_right,"Right")
win.onkeypress(paddle_left,"Left")

while True:
    win.update() # This methods is mandatory to run any game

    # Moving the ball
    #ball.setx(ball.xcor() + ball_dx)
    #ball.sety(ball.ycor() + ball_dy)

