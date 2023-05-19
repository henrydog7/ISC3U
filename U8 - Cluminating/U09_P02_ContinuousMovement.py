import random


def setup_game():
    global screen

    SCREEN_WIDTH = 600
    SCREEN_LENGTH = 400

    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_LENGTH)


def initialize_turtle():
    global move_speed, x_pos, y_pos, change_x, change_y, turtle

    turtle.shape("turtle")
    turtle.shapesize(2, 2)
    turtle.setheading(90)

    move_speed = 3
    x_pos = random.randint(-299, 299)
    y_pos = random.randint(-199, 199)
    change_x = 0
    change_y = 0

    turtle.penup()
    turtle.speed(0)


def left():
    global change_x, change_y, move_speed
    change_x = -move_speed
    change_y = 0
    print(change_x)


def right():
    global change_x, change_y, move_speed
    change_x = move_speed
    change_y = 0
    print(change_x)


def down():
    global change_x, change_y, move_speed
    change_y = -move_speed
    change_x = 0
    print(change_y)


def up():
    global change_x, change_y, move_speed
    change_y = move_speed
    change_x = 0
    print(change_y)


def move_turtle():
    global x_pos, y_pos, change_x, change_y, turtle, screen
    x_pos = x_pos + change_x
    y_pos = y_pos + change_y
    turtle.goto(x_pos, y_pos)


#### Main Program

import turtle

setup_game()
initialize_turtle()

# Activate the Events
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.listen()

playing = True
while playing:
    move_turtle()
    if x_pos > 300 or x_pos < -300 or y_pos > 200 or y_pos < -200:
        playing = False

# Deactivate the Events
screen.onkey(None, "Left")
screen.onkey(None, "Right")
screen.onkey(None, "Up")
screen.onkey(None, "Down")

turtle.exitonclick()
