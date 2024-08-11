import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Score
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Paddle movement flags
paddle_a_up_moving = False
paddle_a_down_moving = False
paddle_b_up_moving = False
paddle_b_down_moving = False

# Function to move paddle A up
def paddle_a_up():
    global paddle_a_up_moving
    paddle_a_up_moving = True

def paddle_a_down():
    global paddle_a_down_moving
    paddle_a_down_moving = True

def paddle_b_up():
    global paddle_b_up_moving
    paddle_b_up_moving = True

def paddle_b_down():
    global paddle_b_down_moving
    paddle_b_down_moving = True

# Functions to stop paddles
def stop_paddle_a_up():
    global paddle_a_up_moving
    paddle_a_up_moving = False

def stop_paddle_a_down():
    global paddle_a_down_moving
    paddle_a_down_moving = False

def stop_paddle_b_up():
    global paddle_b_up_moving
    paddle_b_up_moving = False

def stop_paddle_b_down():
    global paddle_b_down_moving
    paddle_b_down_moving = False

def reset_ball():
    ball.goto(0, 0)
    ball.dx = 0.15
    ball.dy = 0.15
    ball.color("white")

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeyrelease(stop_paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeyrelease(stop_paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeyrelease(stop_paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeyrelease(stop_paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move paddle A
    if paddle_a_up_moving and paddle_a.ycor() < 250:
        paddle_a.sety(paddle_a.ycor() + 0.5)  # Adjusted to 10 units per step
    if paddle_a_down_moving and paddle_a.ycor() > -240:
        paddle_a.sety(paddle_a.ycor() - 0.5)  # Adjusted to 10 units per step

    # Move paddle B
    if paddle_b_up_moving and paddle_b.ycor() < 250:
        paddle_b.sety(paddle_b.ycor() + 0.5)  # Adjusted to 10 units per step
    if paddle_b_down_moving and paddle_b.ycor() > -240:
        paddle_b.sety(paddle_b.ycor() - 0.5)  # Adjusted to 10 units per step

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        reset_ball()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        reset_ball()

    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1  # Reverse direction
        ball.dx *= 1.10  # Increase speed by 10%
        ball.dy *= 1.10  # Increase speed by 10%
        ball.color("yellow")  # Change color to yellow on collision with paddle B

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1  # Reverse direction
        ball.dx *= 1.10  # Increase speed by 10%
        ball.dy *= 1.10  # Increase speed by 10%
        ball.color("blue")  # Change color to blue on collision with paddle A

