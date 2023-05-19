def setup_game():
    global screen
    screen = turtle.Screen()
    screen.setup(600, 400, 0, 0)


def initialize_turtle():
    global move_speed, turtle_x, turtle_y

    # adjust the appearance of the turtle
    turtle.hideturtle()
    turtle.shape("turtle")
    turtle.shapesize(2, 2)
    turtle.setheading(90)

    move_speed = 10
    turtle_x = 0
    turtle_y = -200

    turtle.penup()
    turtle.speed(0)
    turtle.goto(turtle_x, turtle_y)
    turtle.showturtle()


def initialize_car():
    global screen, car, car_x, car_y
    image = "greenbugcar.gif"  # This image needs to be placed in the same folder
    screen.register_shape(image)
    car = turtle.Turtle(shape=image)
    car.hideturtle()
    car.penup()
    car_x = random.randint(-300, 300)
    car_y = 0
    car.goto(car_x, car_y)
    car.showturtle()


def left():
    global turtle_x, turtle_y, move_speed
    if turtle_x - move_speed > -300:
        turtle_x = turtle_x - move_speed


def right():
    global turtle_x, turtle_y, move_speed
    if turtle_x + move_speed < 300:
        turtle_x = turtle_x + move_speed


def down():
    global turtle_x, turtle_y, move_speed
    if turtle_y - move_speed > -200:
        turtle_y = turtle_y - move_speed


def up():
    global turtle_x, turtle_y, move_speed
    if turtle_y + move_speed < 200:
        turtle_y = turtle_y + move_speed


def move_turtle():
    global turtle_x, turtle_y, turtle
    turtle.goto(turtle_x, turtle_y)


def move_car():
    global car_x, car_y, car, move_speed
    car_x = car_x + move_speed
    car.goto(car_x, car_y)


def check_hit():
    global turtle_x, turtle, car, not_hit

    car_left_x = car.xcor() - 15
    car_right_x = car.xcor() + 20
    turtle_left_x = turtle.xcor() - 20
    turtle_right_x = turtle.xcor() + 20

    car_down_y = car.ycor() - 15
    car_up_y = car.ycor() + 20
    turtle_down_y = turtle.ycor() - 20
    turtle_up_y = turtle.ycor() + 20

    y_match = turtle_right_x > car_left_x and turtle_left_x < car_right_x
    x_match = turtle_down_y < car_up_y and turtle_up_y > car_down_y
    if y_match and x_match:
        print("Collision")
        not_hit = False
        turtle.stamp()
        turtle.hideturtle()
        turtle.color("gold4")
        turtle.goto(0, 140)
        turtle.write("Finished", font=("Arial", 40), align="center")


def check_off_screen():
    global car_x, car_y, playing

    if car_x > 300:
        print("Car Off the screen")
        car_x = -300
        car.hideturtle()
        car.goto(car_x, car_y)
        car.showturtle()


#### Main Program

import turtle, time, random

setup_game()
initialize_turtle()
initialize_car()

# Events
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.listen()

# Game Loop
playing = True
not_hit = True
while playing and not_hit:
    move_turtle()
    move_car()
    check_hit()
    check_off_screen()
    #time.sleep(0.1)

# Deactivate the Events
screen.onkey(None, "Left")
screen.onkey(None, "Right")
screen.onkey(None, "Up")
screen.onkey(None, "Down")

screen.exitonclick()
