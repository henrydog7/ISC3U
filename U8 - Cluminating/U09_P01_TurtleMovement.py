import random
def setup_game():
    global screen

    # this assures that the size of the screen will always be 600x400 ...
    SCREEN_WIDTH = 600
    SCREEN_LENGTH = 400
    TOP_LEFT_X = 0
    TOP_LEFT_Y = 0

    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_LENGTH, TOP_LEFT_X, TOP_LEFT_Y)


def initialize_turtle():
    global move_speed, x_pos, y_pos

    # adjust the appearance of the turtle
    turtle.shape("turtle")
    turtle.shapesize(2, 2)
    turtle.setheading(90)

    move_speed = tkinter.simpledialog.askinteger('Movement', 'Enter the size of the steps: ')

    x_pos = random.randint(-300+move_speed, 300-move_speed)
    y_pos = random.randint(-200+move_speed, 200-move_speed)
    turtle.penup()
    turtle.speed(0)
    turtle.goto(x_pos, y_pos)


def left():
    global x_pos, y_pos

    if x_pos - move_speed > -300:
        x_pos = x_pos - move_speed
        turtle.goto(x_pos, y_pos)


def right():
    global x_pos, y_pos
    print(x_pos)
    if x_pos + move_speed < 300:
        x_pos = x_pos + move_speed
        turtle.goto(x_pos, y_pos)

def up():
    global x_pos, y_pos
    if y_pos + move_speed < 200:
        y_pos = y_pos + move_speed
        turtle.goto(x_pos, y_pos)

def down():
    global x_pos, y_pos
    if y_pos - move_speed > -200:
        y_pos = y_pos - move_speed
        turtle.goto(x_pos, y_pos)

#### Main Program

import turtle, tkinter

setup_game()
initialize_turtle()

# Events
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.listen()

turtle.exitonclick()
