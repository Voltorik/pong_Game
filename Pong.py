# A Simple Pong game using the turtle module
# By Voltorik
# Liberal use of comments is done for my own sake, so that I better understand how the code operates
# Apologies to anyone who reads this :)

import turtle
import winsound

wn = turtle.Screen()  # make window
wn.title("Simple Pong by Voltorik")  # window title
wn.bgcolor("black")  # window background color
wn.setup(width=800, height=600)  # window size
wn.tracer(0)  # disable automatic window update

# Score
score_a = 0  # set initial score
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()  # Creates new class Turtle from module turtle
paddle_a.speed(0)   # Set animation speed to maximum
paddle_a.shape("square")    # Set paddle shape to square
paddle_a.color("white")     # Set paddle color to white
paddle_a.shapesize(stretch_wid=5, stretch_len=1)    # Stretch size to make square into rectangle
paddle_a.penup()  # Bring up pen to not leave a line to the origin of the pen
paddle_a.goto(-350, 0)  # Set placement of paddle at left side of the window

# Paddle B
paddle_b = turtle.Turtle()  # Creates new class Turtle from module turtle
paddle_b.speed(0)   # Set animation speed to maximum
paddle_b.shape("square")    # Set paddle shape to square
paddle_b.color("white")     # Set paddle color to white
paddle_b.shapesize(stretch_wid=5, stretch_len=1)    # Stretch size to make square into rectangle
paddle_b.penup()  # Bring up pen to not leave a line to the origin of the pen
paddle_b.goto(350, 0)  # Set placement of paddle at right side of the window

# Ball
ball = turtle.Turtle()  # Creates new class Turtle from module turtle
ball.speed(0)   # Set animation speed to maximum
ball.shape("square")    # Set ball shape to square
ball.color("white")     # Set ball color to white
ball.penup()  # Bring up pen to not leave a line to the origin of the pen
ball.goto(0, 0)  # Set ball at center of window
ball.dx = 0.10  # Move ball 2 pixels on x-axis
ball.dy = 0.10  # Move ball 2 pixels on y-axis

# Pen
pen = turtle.Turtle()  # Creates new class Turtle from module turtle
pen.speed(0)  # Set animation speed to maximum
pen.color("white")  # set ball color to white
pen.penup()  # Bring up pen to not leave a line to the origin of the pen
pen.hideturtle()  # Hide pen
pen.goto(0, 260)  # Set pen starting pos
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))  # Write initial score


# Functions
# paddle_a movement
def paddle_a_up():
    y = paddle_a.ycor()  # Assign paddle's y coordinate to y
    y += 20  # Add 20 pixels to y coord
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()  # Assign paddle's y coordinate to y
    y -= 20  # Subtract 20 pixels to y coord
    paddle_a.sety(y)


# paddle_b movement
def paddle_b_up():
    y = paddle_b.ycor()  # Assign paddle's y coordinate to y
    y += 20  # Add 20 pixels to y coord
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()  # Assign paddle's y coordinate to y
    y -= 20  # Subtract 20 pixels to y coord
    paddle_b.sety(y)


# Keyboard binding
wn.listen()  # Listen for key input
wn.onkeypress(paddle_a_up, "w")  # On key press "w" call paddle_a_up
wn.onkeypress(paddle_a_down, "s")  # On key press "s" call paddle_a_down
wn.onkeypress(paddle_b_up, "Up")  # On key press "Up" call paddle_b_up
wn.onkeypress(paddle_b_down, "Down")  # On key press "Down" call paddle_b_down

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # Set ball's x coord to current x coord + ball.dx
    ball.sety(ball.ycor() + ball.dy)  # Set ball's y coord to current y coord + ball.dy

    # Border checking
    if ball.ycor() > 290:  # 290 pixels on y-axis is the top edge of screen
        ball.sety(290)  # Reset ball within screen bounds
        ball.dy *= -1  # Multiply dy by -1 to set dy negative and make ball travel the opposite direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # Play bounce sound on collision

    if ball.ycor() < -290:  # -290 pixels on y-axis is the bottom edge of screen
        ball.sety(-290)  # Reset ball within screen bounds
        ball.dy *= -1  # Multiply dy by -1 to set dy positive and make ball travel the opposite direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # Play bounce sound on collision

    if ball.xcor() > 390:  # 390 pixels on x coord indicates a goal scored on right side
        ball.goto(0, 0)  # if a goal is scored ball is reset at center
        ball.dx *= -1  # dx is reversed to move toward the previous scorer's side
        score_a += 1  # Add 1 to score
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # Play bounce sound on collision
        pen.clear()  # Clear previous pen drawings
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))  # Write new score

    if ball.xcor() < -390:  # -390 pixels on x coord indicates a goal scored on left side
        ball.goto(0, 0)  # if a goal is scored ball is reset at center
        ball.dx *= -1  # dx is reversed to move toward the previous scorer's side
        score_b += 1  # Add 1 to score
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # Play bounce sound on collision
        pen.clear()  # Clear previous pen drawings
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))  # Write new score

    # Paddle and ball collisions
    # if ball is between the same values as the position of paddle_b
    if 340 < ball.xcor() < 350 and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)  # Set x-coord of ball to edge of paddle
        ball.dx *= -1  # Change ball's direction by inverting dx
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # Play bounce sound on collision

    # if ball is between the same values as the position of paddle_a
    if -340 > ball.xcor() > -350 and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)  # Set x-coord of ball to edge of paddle
        ball.dx *= -1  # Change ball's direction by inverting dx
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # Play bounce sound on collision


