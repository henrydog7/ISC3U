def setup_game():
    global screen
    screen = turtle.Screen()
    screen.setup(600, 400, 0, 0)


def initialize_turtle():
    global move_speed, turtle_x, turtle_y, change_x

    # adjust the appearance of the turtle
    turtle.hideturtle()
    turtle.shape("turtle")
    turtle.shapesize(2, 2)
    turtle.setheading(90)

    move_speed = 3
    turtle_x = random.randint(-299, 299)
    turtle_y = random.randint(-199, 199)
    change_x = 0

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
    car_x = random.randint(-200, 200)
    car_y = random.randint(-100, 100)
    car.goto(car_x, car_y)
    car.showturtle()


def left():
    global turtle_x, turtle_y, move_speed
    turtle_x = turtle_x - move_speed


def right():
    global turtle_x, turtle_y, move_speed
    turtle_x = turtle_x + move_speed

def down():
    global turtle_x, turtle_y, move_speed
    turtle_y = turtle_y - move_speed


def up():
    global turtle_x, turtle_y, move_speed
    turtle_y = turtle_y + move_speed


def move_turtle():
    global turtle_x, turtle_y, turtle
    turtle.goto(turtle_x, turtle_y)


def check_hit():
    global turtle_x, turtle, car, not_hit

    car_left_x = car.xcor() - 15
    car_right_x = car.xcor() + 20
    turtle_left_x = turtle.xcor() - 20
    turtle_right_x = turtle.xcor() + 20

    if turtle_right_x > car_left_x and turtle_left_x < car_right_x:
        print("Collision")
        not_hit = False
        turtle.stamp()
        turtle.goto(0, -150)


def check_off_screen():
    global turtle_x, playing
    if turtle_x > 300 or turtle_x < -300 or turtle_y > 200 or turtle_y < -200:
        print("Off the screen")
        playing = False


#### Main Program
import turtle, tkinter.simpledialog, random

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
    check_hit()
    check_off_screen()

# Deactivate the Events
screen.onkey(None, "Left")
screen.onkey(None, "Right")

screen.exitonclick()
