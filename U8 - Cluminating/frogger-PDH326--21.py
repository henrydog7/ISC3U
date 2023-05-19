import turtle
#initializes the variables for the game
def initialize_game():
    pass


# displays the game instructions
def display_instructions():
    pass


# displays the welcome screen
def welcome_screen():
    pass


# draws the game background eliments
def draw_screen():
    pass


# creates the frog
def set_up_frog():
    pass

# creates the cars
def set_up_car():
    pass


# stars the level
def start_level():
    pass

# starts the round
def star_round():
    pass


# increase frog y
def up():
    pass


# decreases frog y
def down():
    pass

# decreases frog x
def left():
    pass


# increases frog x
def right():
    pass


# moves frog to new posision
def move_frog():
    pass


# moves cars to new posision
def move_cars():
    pass


# moves logs to new posision
def move_logs():
    pass


# checks if the frog is in contact with car, log, end, or water
def check_collision():
    pass


# checks to see if frog is off screen
def check_frog_off_screen():
    pass


# check to see car is off screen
def check__car_off_screen():
    pass


# checks to see if log is off screen
def check__log_off_screen():
    pass


# resets frog if off screen, dead, or at end
def reset_frog():
    pass


# resets car if off screen
def reset_car():
    pass


# resets cars if off screen
def reset_logs():
    pass


# ends the round when frog is at end or dead
def check_end_round():
    pass


# ends level if all frogs make it to the end
def check_end_level():
    pass


# ends game if all lives are lost or game finished
def check_end_game():
    pass


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
initialize_game()
set_up_frog()
set_up_car()
set_up_logs()

not_done_program = True
while not_done_program:

    display_instructions()
    welcome_screen()
    draw_screen()

    not_done_game = True
    while not_done_game:

        start_level()
        play_level = True
        set_up_frog()
        set_up_car()
        set_up_logs()
        star_round()

        play_round = True
        while play_round:
            turtle.onkey(up, "Up")
            turtle.onkey(down, "Down")
            turtle.onkey(left, "Left")
            turtle.onkey(right, "Right")
            move_frog()
            move_cars()
            move_logs()
            check_collision()
            check_frog_off_screen()
            check__car_off_screen()
            check__log_off_screen()
            reset_frog()
            reset_car()
            reset_logs()
            check_end_round()

            check_end_level()
            if play_level == True:
                new_round()

    check_end_game
    if play_game == True:
        new_level()

    new_game()
    leave_game()
