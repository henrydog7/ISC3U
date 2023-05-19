# frog			refers to the frog turtle
# frog_x			the x position of the frog
# frog_y			the y_position of the frog
# cars[]			array to refer to the car turtles
# cars_x[]		array for the x positions of the cars
# cars_y[]		array for the y positions of the cars
# log[]			refers to the log turtles
# rails_y[]	list of values to set the turtle y positions too as they move across the screen
# window, running_instructions
# car_collision		boolean variable set to false until there is a collision with a car
# log_collision		boolean variable set to false until there is a collision with a log
# not_done_program	boolean variable set to true until the program is over
# not_done_game	boolean variable set to true until the game is over
# not_done_level	boolean variable set to true until the level is over
# not_done_round	boolean variable set to true until the round is over
# level			holds the current level the player is on
# points			holds the points of the current game
# lives			holds the lives of the current game

# TODO      timer
# TODO      win round
# TODO      win level
# TODO      display lives points and time
# TODO      only on lilly pads
# TODO      fix  x rail location
# TODO      document
# TODO      end screen
# TODO      top 10


import random
import tkinter as tk
from tkinter import ttk
import turtle
import time


# initializes the variables for the game
def initialize_game():
    global move_speed, screen, frog, frog_x, frog_y, frog_rail_y, frog_rail_x, cars, cars_x, cars_y, cars_time_off,\
        cars_time_on, rails_y, rails_x, start_time, car_collision, log_collision, window, running_instructions,\
        not_done_program, not_done_game, not_done_level, not_done_round, level, points, lives, screen_width,\
        screen_height, info_turtle

    move_speed = 10
    screen = turtle.Screen()
    frog = turtle.Turtle()
    frog_x = 0
    frog_y = 0
    frog_rail_y = 0
    frog_rail_x = 9
    cars = []
    cars_x = []
    cars_y = []
    cars_time_off = []
    cars_time_on = []
    rails_y = []
    rails_x = []
    start_time = 0
    car_collision = False
    log_collision = False
    not_done_program = True
    not_done_game = True
    not_done_level = True
    not_done_round = True
    level = 1
    points = 0
    lives = 3
    frog_x = frog_y = 0
    move_speed = 10
    info_turtle = turtle.Turtle()

    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.destroy()

    screen = turtle.Screen()
    screen.setup(screen_width, screen_height, 0, 0)

    for i in range(7):
        rails_y.append((screen_height*(i-3))//7)
        print(rails_y[i])

    for i in range(18):
        rails_x.append(screen_width // 18 * i - screen_width // 2 + screen_width // 18)

    print(rails_x)


def exit_instructions():
    global window
    window.destroy()
    window.quit()


# displays the game instructions
def display_instructions():
    global window, running_instructions
    running_instructions = True
    window = tk.Tk()
    window.title("Instructions")

    label = tk.Label(
        master=window,
        text="Welcome to Frogger!\n"
             "Move the frog (turtle) with WASD\n"
             "You will lose a life for hitting a car\n"
             "You start off with three lives\n"
             "To Win get four frogs to the green safe zones at the other end\n"
             "Don't fall in the water",
        fg="white",
        bg="black",
        width=50,
        height=15
    )

    label.pack()

    button = tk.Button(
        master=window,
        text="Exit",
        command=exit_instructions,
        width=50,
        height=5
    )
    button.pack()

    window.mainloop()

    running_instructions = False

# displays the welcome screen
def welcome_screen():
    pass


# draws the game background eliments
def draw_screen():
    global screen_width, screen_height
    turtle.hideturtle()
    turtle.speed(0)
    turtle.up()
    for k in range(6):
        turtle.goto(-screen_width / 2, (screen_height*k)//7-screen_height//2)
        turtle.setheading(0)
        if k == 0 or k == 3:
            turtle.fillcolor("green")
        else:
            turtle.down()
            turtle.color("yellow")
            turtle.fillcolor("black")
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(screen_width)
            turtle.setheading(turtle.heading() + 90)
            turtle.forward(screen_height / 7)
            turtle.setheading(turtle.heading() + 90)
        turtle.end_fill()
        turtle.up()
    for j in range(9):
        turtle.goto(screen_width / 9 * j - screen_width / 2, (screen_height*6)//7-screen_height//2)
        if j % 2 == 0:
            turtle.color("blue")
        else:
            turtle.color("green")
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(screen_width / 9)
            turtle.setheading(turtle.heading() + 90)
            turtle.forward(screen_height / 7)
            turtle.setheading(turtle.heading() + 90)
        turtle.end_fill()


# creates the frog
def initialize_frog():
    global move_speed, frog_x, frog_y, frog

    frog = turtle.Turtle()
    # adjust the appearance of the turtle
    frog.hideturtle()
    frog.shape("turtle")
    frog.color("white")
    frog.shapesize(screen_height/350, screen_width/400)
    frog.setheading(90)

    move_speed = 10
    frog_x = (screen_width//18)*9
    frog_y = -200

    frog.penup()
    frog.speed(0)
    frog.goto(frog_x, frog_y)
    frog.showturtle()


def initialize_cars():
    global screen, cars, cars_x, cars_y, cars_time_on, cars_time_off
    image = "greenbugcar.gif"  # This image needs to be placed in the same folder
    larger = tk.PhotoImage(file=image).zoom(screen_height//350, screen_width//400)

    screen.addshape("larger", turtle.Shape("image", larger))

    for i in range(10):
        cars.append(turtle.Turtle("larger"))
        cars_x.append(random.randint(-screen_width/2, screen_width/2))
        cars_y.append(0)
        cars_time_on.append(0)
        cars_time_on.append(0)
        cars[i].penup()
        cars[i].speed(0)
        print(cars_x[i])
        cars[i].goto(cars_x[i], cars_y[i])
        cars[i].showturtle()


# stars the level
def start_level():
    global lives, start_time, end_time
    lives = 3
    start_time = time.time()
    end_time = start_time +60


# starts the round
def star_round():
    pass


def set_up_frog():
    global frog, frog_x, frog_y, frog_rail_y, rails_y
    frog_x = (-screen_width//2) + (screen_width/18)
    frog_rail_y = 0
    frog_y = rails_y[frog_rail_y]
    frog.goto(frog_x, frog_y)


def set_up_cars():
    global cars, cars_y, cars_x, rails_y, start_time, cars_time_on, cars_time_off

    include_rails_y = [1, 2, 4, 5]
    for i in range(len(cars)):
        random_rail = random.choice(include_rails_y)
        cars_y[i] = rails_y[random_rail]
        cars_x[i] = -screen_width//2
        cars_time_on[i] = start_time + (random.randrange(100, 1000) / 100)
        print(cars_x[i])
        print(screen_width)
        cars[i].goto(cars_x[i], cars_y[i])


# increase frog y
def left():
    global frog_rail_x, frog_x
    if frog_rail_y > 0:
        frog_rail_x = frog_rail_x - 1
        frog_x = rails_x[frog_rail_x]


def right():
    global frog_rail_x, frog_x
    if frog_rail_y < 18:
        frog_rail_x = frog_rail_x + 1
        frog_x = rails_x[frog_rail_x]


def down():
    global frog_x, frog_y, frog_rail_y, move_speed
    if frog_rail_y > 0:
        frog_rail_y = frog_rail_y - 1
        frog_y = rails_y[frog_rail_y]


def up():
    global frog_x, frog_y, frog_rail_y, move_speed
    if frog_rail_y < 6:
        frog_rail_y = frog_rail_y + 1
        frog_y = rails_y[frog_rail_y]


def move_frog():
    global frog_x, frog_y, frog
    frog.goto(frog_x, frog_y)


# moves cars to new posision
def move_cars():
    global cars_x, cars_y, cars_time_on, cars, move_speed
    for i in range(len(cars)):
        if cars_time_on[i] < time.time():
            print(i, "---   ", cars_x[i])
            cars_x[i] = cars_x[i] + move_speed
            print(i, ":  ", cars_x[i])
            cars[i].goto(cars_x[i], cars_y[i])


# checks if the frog is in contact with car, log, end, or water
def check_collision():
    global frog_x, frog_y, frog_rail_y,frog_rail_x, frog, cars, lives, points, rails_y, not_done_round

    for i in range(len(cars)):
        car_left_x = cars[i].xcor() - 15
        car_right_x = cars[i].xcor() + 20
        frog_left_x = frog.xcor() - 20
        frog_right_x = frog.xcor() + 20

        car_down_y = cars[i].ycor() - 15
        car_up_y = cars[i].ycor() + 20
        frog_down_y = frog.ycor() - 20
        frog_up_y = frog.ycor() + 20

        y_match = frog_right_x > car_left_x and frog_left_x < car_right_x
        x_match = frog_down_y < car_up_y and frog_up_y > car_down_y
        if y_match and x_match:
            not_done_round = False
            lives = lives - 1
            frog.hideturtle()
            frog_rail_y = 0
            frog_rail_x =9
            frog_y = rails_y[frog_rail_y]
            frog_x = rails_x[frog_rail_y]

    if frog_rail_y == 6:
        touch_pads = []
        touch_pads[0] = frog_rail_x == 2 or frog_rail_x == 3
        touch_pads[1] = frog_rail_x == 6 or frog_rail_x == 7
        touch_pads[2] = frog_rail_x == 10 or frog_rail_x == 11
        touch_pads[3] = frog_rail_x == 14 or frog_rail_x == 15
        if touch_pads[0] or touch_pads[1] or touch_pads[2] or touch_pads[3]:
            points = points +100
            frog.stamp
            not_done_round = False
            frog.hideturtle()
            frog_rail_y = 0
            frog_y = rails_y[frog_rail_y]
            frog_x = 0
        else:
            not_done_round = False
            lives = lives - 1
            frog.hideturtle()
            frog_rail_y = 0
            frog_y = rails_y[frog_rail_y]
            frog_x = 0


def is_car_near(pos):
    global cars, cars_y, cars_x, rails_y, start_time, cars_time_on, cars_time_off
    for i in range(len(cars)):
        if cars_y[i] == cars_y[pos] and i != pos:
            if cars_time_on[i] - 3 <= cars_time_on[pos] <= cars_time_on[i] + 3:
                return True


# check to see car is off screen
def check__car_off_screen():
    global cars, cars_y, cars_x, rails_y, start_time, cars_time_on, cars_time_off

    include_rails_y = [1, 2, 4, 5]
    for i in range(len(cars)):
        if cars_x[i] > screen_width//2 or cars_x[i] < (-screen_width//2)-100:
            random_rail = random.choice(include_rails_y)
            cars_y[i] = rails_y[random_rail]
            cars_time_on[i] = start_time + (random.randrange(500, 10000) / 1000)

            while is_car_near(i):
                random_rail = random.choice(include_rails_y)
                cars_y[i] = rails_y[random_rail]
                cars_time_on[i] = time.time() + (random.randrange(500, 7000) / 1000)

            cars_x[i] = (-screen_width//2)-50
            cars[i].goto(cars_x[i], cars_y[i])


def update_screen():
    global info_turtle
    info_turtle.speed(0)
    info_turtle.up()
    info_turtle.hideturtle()

    info_turtle.goto((screen_width//2)-70, (screen_height//2)-70)
    info_turtle.write("Lives" + str(lives))
    info_turtle.goto(0, (screen_height//2)-40)
    info_turtle.write("Time" + str(lives))
    info_turtle.goto((-screen_width // 2)+70, (screen_height//2)-70)
    info_turtle.write("Points" + str(lives))


# resets frog if off screen, dead, or at end
def reset_frog():
    global frog
    frog.showturtle()


# resets car if off screen
def reset_car():
    pass


# ends the round when frog is at end or dead
def check_end_round():
    global frog_y, rails_y, not_done_round
    if frog_y == rails_y[6]:
        frog.goto(frog_x, frog_y)
        frog.stamp()
        not_done_round = False


# ends level if all frogs make it to the end
def check_end_level():
    global lives, not_done_round
    if lives < 1:
        not_done_round = False


# ends game if all lives are lost or game finished
def check_end_game():
    global lives, not_done_game, not_done_program, turtle
    if lives < 1:
        ask_leave = tk.messagebox.askquestion("End Game", "Would you like to play again")
        if ask_leave == "no":
            not_done_game = False
            not_done_program = False

        else:
            not_done_game = False
            turtle.clear()


# resets for new round
def new_round():
    pass


# resets for new level
def new_level():
    pass


# resets for new game
def new_game():
    pass


# ends the program when the user wishes
def leave_game():
    pass


# main program

not_done_program = True
while not_done_program:

    initialize_game()
    draw_screen()
    initialize_frog()
    initialize_cars()

    display_instructions()
    welcome_screen()

    not_done_game = True
    while not_done_game:

        start_level()
        not_done_level = True
        while not_done_level:
            set_up_cars()
            set_up_frog()
            star_round()

            not_done_round = True
            while not_done_round:
                turtle.onkey(up, "w")
                turtle.onkey(down, "s")
                turtle.onkey(left, "a")
                turtle.onkey(right, "d")
                turtle.listen()
                move_frog()
                move_cars()
                check_collision()
                check__car_off_screen()
                update_screen()
                reset_frog()
                reset_car()
                check_end_round()

            check_end_level()
            if not_done_round == True:
                new_round()

        check_end_game()
        if not_done_game == True:
            new_level()

    # new_game()
    leave_game()
