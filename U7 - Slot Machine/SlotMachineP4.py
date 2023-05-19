########################################
# Slot Machine Program

# Lucas Balog
# Creation date: Oct. 21, 2020
# Modified date: Nov. 4, 2020

# SlotMachineP4.py
# other files: SaveHighScores.dat
#               SaveSlotGame(username).dat # multiple files for each user that saves

# The program runs a slot machine game. The user will be asked for a user name. They
# can load a game saved with the same user name or start a new game. The user is asked to enter an amount of
# virtual money to bet. Three numbers are randomly generated and displayed until the user presses space.
# If there are any designated sequences the user is awarded their winnings in their virtual bank account. If there
# are not losses the bet is subtracted from their account. The user stars with 200$. The user can save after every spin.
# If the user looses all their money they must quit or start a new game.
# UPDATE: completed documentation

# Documented Errors
# none

# Variable List
# not_done_game         boolean variable used to determine weather to run game or end program
# not_done_spin         boolean variable used to determine weather to spin slots or end loop
# not_done_gba          boolean variable used to determine weather program has received the bet amount
# slot1                 holds the number between 1 and 10 that has been randomly generated
# slot2                 holds the number between 1 and 10 that has been randomly generated
# slot3                 holds the number between 1 and 10 that has been randomly generated
# bet_amount            holds the amount the user bet
# bank                  holds the amount of virtual money the user has
# winnings              holds the amount the user won each round
# high_scores           list used to remember the high scores
# score_names           list used to remember the names of the users with the high scores
# bool_to_change        used by end_section() function to change the bool of this name to False
# window                variable used to control the turtle window
# name                  Holds the name of the current user
# prompt_turtle         Refers to the turtle used while drawing the slot 3 value
# bet_turtle            Refers to the turtle used while drawing durting the get_bet() function
# instructions_turtle   Refers to the turtle used while drawing the game instructions
# machine_turtle        Refers to the turtle used while drawing the slot machine
# slot1_turtle          Refers to the turtle used while drawing the slot 1 value
# slot2_turtle          Refers to the turtle used while drawing the slot 2 value
# slot3_turtle          Refers to the turtle used while drawing the slot 3 value
# save_turtle           Refers to the turtle used while drawing the instructions to save
# bank_turtle           Refers to the turtle used while drawing the bank amount
# bet_amount_turtle     Refers to the turtle used while drawing the bet amount
# run_screen            boolean variable used to determine weather to run the intro_screen() loop or exit
# run_ask_load          boolean variable used to determine weather to run the check_save() loop or exit
# root                  refers the tkinter window used to get the username for the game
# name_input            refers to the entry widget in the root window that allows the user to input the username
# FONT_SIZE             constant variable used to set the standard font size
# FONT_TYPE             constant variable used to set the standard font type
# FONT_COLOUR           constant variable used to set the standard font colour
# FONT_COLOUR_ALT       constant variable used to set the standard font alternate colour
# BG_COLOUR             constant variable used to set the back ground colour
########################################


import random
import time
import tkinter
import turtle


########################################
# The initialize_game function declares and initializes all the global variables
########################################


def initialize_game():
    global slot1, slot2, slot3, bet_amount, bank, winnings, high_scores, score_names, \
        window, bool_to_change, name, \
        bank_turtle, prompt_turtle, bet_turtle, instructions_turtle, machine_turtle, slot1_turtle, \
        slot2_turtle, slot3_turtle, save_turtle, bank_turtle, bet_amount_turtle, \
        FONT_SIZE, FONT_TYPE, FONT_COLOUR, FONT_COLOUR_ALT, BG_COLOUR

    slot1 = slot2 = slot3 = winnings = 0
    bet_amount = 5
    bank = 200
    high_scores = []
    score_names = []
    bool_to_change = ""
    name = ""

    FONT_SIZE = "46"
    FONT_TYPE = "Arial"
    FONT_COLOUR = "gold4"
    FONT_COLOUR_ALT = "gray72"
    BG_COLOUR = "black"

    window = turtle.Screen()
    window.bgcolor(BG_COLOUR)
    turtle.setup(1000, 1000, 0, 0)

    turtle.hideturtle()
    turtle.up()
    turtle.speed(0)

    bank_turtle = turtle.Turtle()
    bank_turtle.hideturtle()
    bank_turtle.up()
    bank_turtle.speed(0)

    prompt_turtle = turtle.Turtle()
    prompt_turtle.penup()
    prompt_turtle.hideturtle()

    bet_turtle = turtle.Turtle()
    bet_turtle.up()
    bet_turtle.hideturtle()
    bet_turtle.speed(0)

    instructions_turtle = turtle.Turtle()
    instructions_turtle.up()
    instructions_turtle.hideturtle()
    instructions_turtle.speed(0)

    machine_turtle = turtle.Turtle()
    machine_turtle.hideturtle()
    machine_turtle.penup()
    machine_turtle.speed(0)

    slot1_turtle = turtle.Turtle()
    slot1_turtle.hideturtle()
    slot1_turtle.up()
    slot1_turtle.speed(0)

    slot2_turtle = turtle.Turtle()
    slot2_turtle.hideturtle()
    slot2_turtle.up()
    slot2_turtle.speed(0)

    slot3_turtle = turtle.Turtle()
    slot3_turtle.hideturtle()
    slot3_turtle.up()
    slot3_turtle.speed(0)

    save_turtle = turtle.Turtle()
    save_turtle.hideturtle()
    save_turtle.hideturtle()
    save_turtle.speed(0)

    bank_turtle = turtle.Turtle()
    bank_turtle.hideturtle()
    bank_turtle.up()
    bank_turtle.speed(0)

    bet_amount_turtle = turtle.Turtle()
    bet_amount_turtle.hideturtle()
    bet_amount_turtle.up()
    bet_amount_turtle.speed(0)


########################################
# The store_name() function is used by the get_name() function to store the value
# of the name_input widget in the root window. this is sotored as name
########################################


def store_name(event):
    global name, root, name_input
    name = name_input.get()
    root.quit()
    root.destroy()


########################################
# The get_name() function draws a tkinter window (root) with an entry widget(name_input)
# when enter is pressed store_name is called and the mainloop is left
########################################


def get_name():
    global name, root, name_input
    root = tkinter.Tk()
    root.title("Enter Name")
    tkinter.Label(root, text="User Name").grid(row=0)
    root.geometry('200x100-900+400')
    name_input = tkinter.Entry(root)

    name_input.grid(row=0, column=1)

    root.bind('<Return>', store_name)
    root.protocol("WM_DELETE_WINDOW", store_name)

    root.mainloop()


########################################
# The check_save() function checks to see if there is a game saved. The user can only load a game if their username
# is the same of that of a saved game. If there is a saved game the program will as the user if they would like
# to load the game. If they answer yes("y") load_game() is called and the game bank balance is loaded.

# Local Variable List
# save_file             refers to the SaveSLotGame(username).dat file
# saved_bank            used to hold the bank balance read from SaveSlotGame(username).dat
########################################


def check_save():
    global bool_to_change, run_ask_load

    try:
        save_file = open("SaveSlotGame" + name + ".dat", "r")
        saved_bank = save_file.readline().strip()
        save_file.close()

        bool_to_change = "run_ask_load"
        turtle.onkey(end_section, "n")
        turtle.onkey(load_game, "y")
        turtle.listen()

        run_ask_load = True
        while run_ask_load:
            turtle.color(FONT_COLOUR)
            turtle.write("Saved game detected\nBank:" + saved_bank + "$\nwould you like to load? y/n",
                         font=(FONT_TYPE, FONT_SIZE), align="center")
            time.sleep(0.5)
            turtle.color(FONT_COLOUR_ALT)
            turtle.write("Saved game detected\n"
                         "Bank:" + saved_bank + "$\n"
                                                "would you like to load? y/n",
                         font=(FONT_TYPE, FONT_SIZE), align="center")
            time.sleep(0.5)

        turtle.onkey(None, "n")
        turtle.onkey(None, "y")
        turtle.clear()

    except FileNotFoundError:
        pass


########################################
# The end_section() function is used to end while loops. it uses the name of bool variable that is stored as a string
# in bool_to_change. the bool value is changed to false and the while loop is ended.
# this function is used with the .onkey() function
########################################


def end_section():
    globals()[bool_to_change] = False


########################################
# The load_game() function opens the SaveSlotGame.dat file reads the saved bank value and sets the
# game bank value to the saved value. it also ends the run_ask_load while loop in check_save() function
# Local Variable List
# save_file             refers to the SaveSlotGame.dat file
########################################


def load_game():
    global run_ask_load, bank
    save_file = open("SaveSlotgame" + name + ".dat", "r")
    bank = int(save_file.readline())
    run_ask_load = False
    save_file.close()


########################################
# The instructions_screen() function draws the set of instructions to the screen. it clears and
# continues when enter is pressed.
########################################


def instructions_screen():
    global bool_to_change, not_done_instructions
    align_x = -475

    turtle.color(FONT_COLOUR)
    turtle.setpos(align_x, 350)
    turtle.write("Welcome to the game!",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")
    turtle.setpos(align_x, 300)
    turtle.write("Players will be able to load a previous save game (with the same username) or star a new game.",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")
    turtle.setpos(align_x, 270)
    turtle.write("At the beginning of each round you will be asked to place a bet.",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")
    turtle.setpos(align_x, 240)
    turtle.write("Bets must be made in five dollar intervals (ie. 5$,10$,15$)",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")
    turtle.setpos(align_x, 210)
    turtle.write("After the bet is placed the machine will be show and the it will star to spin",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")
    turtle.setpos(align_x, 180)
    turtle.write("Press space bar to stop spinning",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")
    turtle.setpos(align_x, 150)
    turtle.write("After the slots stop the winnings will be",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")
    turtle.setpos(align_x, 120)
    turtle.write("Calculate based on the fallowing sequences",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")
    turtle.setpos(align_x, 90)
    turtle.write("Description             Example         Payoff",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")
    turtle.setpos(align_x, 60)
    turtle.write("Three of a kind           4   4   4       10 x bet",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")
    turtle.setpos(align_x, 30)
    turtle.write("Outside match           4   5   4        3 x bet",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")
    turtle.setpos(align_x, 0)
    turtle.write("Side by side match    4   4   6               ",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")
    turtle.setpos(align_x, -30)
    turtle.write("                                  4   5   5        2 x bet",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")
    turtle.setpos(align_x, -60)
    turtle.write("Straight in sequence(any increasing straight) ",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")
    turtle.setpos(align_x, -90)
    turtle.write("                                  4   5   6               ",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")
    turtle.setpos(align_x, -120)
    turtle.write("                                  1   2   3               ",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")
    turtle.setpos(align_x, -150)
    turtle.write("                                  3   4   5        5 x bet",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")
    turtle.setpos(align_x, -180)
    turtle.write("Fallow instructions to play again or leave",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="left")

    bool_to_change = "not_done_instructions"
    turtle.onkey(end_section, "Return")
    turtle.listen()

    turtle.goto(0, -270)
    not_done_instructions = True
    while not_done_instructions:
        turtle.color(FONT_COLOUR)
        turtle.write("Press enter to continue", font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.5)
        turtle.color(FONT_COLOUR_ALT)
        turtle.write("Press enter to continue", font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.5)

    turtle.onkey(None, "Return")
    turtle.clear()


########################################
# The intro_screen() function displays a welcome message for the game and continues when enter is pressed
########################################


def intro_screen():
    global run_screen, bool_to_change

    bool_to_change = "run_screen"
    window.onkey(end_section, "Return")
    window.listen()

    turtle.setpos(0, 200)
    turtle.color(FONT_COLOUR)
    turtle.write("Welcome to the game!",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 20)), align="center")

    prompt_turtle.setpos(0, -300)

    run_screen = True
    while run_screen:
        prompt_turtle.color(FONT_COLOUR)
        prompt_turtle.write("Press enter to begin", font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.5)
        prompt_turtle.clear()
        prompt_turtle.color(FONT_COLOUR_ALT)
        prompt_turtle.write("Press enter to begin", font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.5)
        prompt_turtle.clear()

    window.onkey(None, "Return")
    turtle.clear()


########################################
# The bet_up() function increases the monitary bet amout (bet_amount) by 5 and updates the screen.
# This only happens if the bet ammount is less than the bank balance
########################################


def bet_up():
    global bet_amount, bet_turtle, bank

    if bet_amount < bank:
        bet_amount = bet_amount + 5
        bet_turtle.clear()
        bet_turtle.setpos(0, 0)
        bet_turtle.write(str(bet_amount) + "$", font=(FONT_TYPE, FONT_SIZE), align="center")


########################################
# The bet_down() function decreases the monitary bet amout (bet_amount) by 5 and updates the screen.
# this only happens if the bet ammount is less greater than 5
########################################


def bet_down():
    global bet_amount, bet_turtle

    if bet_amount > 5:
        bet_amount = bet_amount - 5
        bet_turtle.clear()
        bet_turtle.setpos(0, 0)
        bet_turtle.write(str(bet_amount) + "$", font=(FONT_TYPE, FONT_SIZE), align="center")


########################################
# The get_bet_amount() function displays the current bet ammount and allows the user to change
# it in five dollar intervals to the ammout they wish.
########################################


def get_bet_amount():
    global bet_amount, bool_to_change, bet_turtle, not_done_gba

    # set up bet turtle
    bet_turtle.color(FONT_COLOUR)

    # set up instructions turtle

    # set up onkey() functions
    bool_to_change = "not_done_gba"
    turtle.onkey(end_section, "Return")
    turtle.onkey(bet_up, "Up")
    turtle.onkey(bet_down, "Down")
    turtle.listen()

    # set up canvas
    bet_amount = 5
    bet_turtle.clear()
    bet_turtle.setpos(0, 0)
    bet_turtle.write(str(bet_amount) + "$", font=(FONT_TYPE, FONT_SIZE), align="center")

    # write instructions to enter bet
    instructions_turtle.setpos(0, -200)

    not_done_gba = True
    while not_done_gba:
        instructions_turtle.color(FONT_COLOUR)
        instructions_turtle.write("Place Bet\n"
                                  "Press enter to select\n"
                                  "Arrows to move up or down",
                                  font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.5)
        instructions_turtle.clear()
        instructions_turtle.color(FONT_COLOUR_ALT)
        instructions_turtle.write("Place Bet \n"
                                  "Press enter to select\n"
                                  "Arrows to move up or down",
                                  font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.5)

    turtle.onkey(None, "Return")
    turtle.onkey(None, "Up")
    turtle.onkey(None, "Down")
    bet_turtle.clear()
    instructions_turtle.clear()


########################################
# The draw_machine() function draws the slot machine to the screen when called. it uses the global machine_turtle
# to draw all immages so it can be cleared by machine_turtle.clear() from anywhere in the program
########################################


def draw_machine():
    global machine_turtle

    machine_turtle.color("red")
    machine_turtle.setpos(250, -500)
    machine_turtle.setheading(0)

    machine_turtle.begin_fill()
    for i in range(2):
        machine_turtle.setheading(machine_turtle.heading() + 90)
        machine_turtle.forward(750)
        machine_turtle.setheading(machine_turtle.heading() + 90)
        machine_turtle.forward(500)

    machine_turtle.end_fill()

    machine_turtle.color(FONT_COLOUR_ALT)
    machine_turtle.setpos(-60, 0)
    machine_turtle.setheading(0)
    machine_turtle.begin_fill()
    for i in range(2):
        machine_turtle.setheading(machine_turtle.heading() + 90)
        machine_turtle.forward(75)
        machine_turtle.setheading(machine_turtle.heading() + 90)
        machine_turtle.forward(80)
    machine_turtle.end_fill()

    machine_turtle.setpos(40, 0)
    machine_turtle.begin_fill()
    machine_turtle.setheading(0)
    for i in range(2):
        machine_turtle.setheading(machine_turtle.heading() + 90)
        machine_turtle.forward(75)
        machine_turtle.setheading(machine_turtle.heading() + 90)
        machine_turtle.forward(80)
    machine_turtle.end_fill()

    machine_turtle.setpos(140, 0)
    machine_turtle.begin_fill()
    machine_turtle.setheading(0)
    for i in range(2):
        machine_turtle.setheading(machine_turtle.heading() + 90)
        machine_turtle.forward(75)
        machine_turtle.setheading(machine_turtle.heading() + 90)
        machine_turtle.forward(80)
    machine_turtle.end_fill()


time.sleep(3)


########################################
# The stop_spin() function changes the not_done_spin variable to False to end the spin_slot loop
########################################


def stop_spin():
    global not_done_spin
    not_done_spin = False


########################################
# The spin_slots() function randomly generates three numbers and displays them to the screen (slot1, slot2, slot3)
# all number are between 1 and 10 and individualy cleared and redrawn. this continues untill space is pressed
########################################


def spin_slots():
    global slot1, slot2, slot3, not_done_spin
    not_done_spin = True

    turtle.clear()

    slot1_turtle.color(FONT_COLOUR)
    slot2_turtle.color(FONT_COLOUR)
    slot3_turtle.color(FONT_COLOUR)

    turtle.onkey(stop_spin, "space")
    turtle.listen()
    turtle.setpos(0, -300)
    turtle.color(FONT_COLOUR)
    turtle.write("Press space bar to stop", font=(FONT_TYPE, FONT_SIZE), align="center")

    while not_done_spin:
        slot1_turtle.setpos(-100, 0)
        slot1_turtle.clear()
        slot1 = random.randint(1, 10)
        slot1_turtle.write(str(slot1), font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.1)

        slot2_turtle.clear()
        slot2_turtle.setpos(0, 0)
        slot2 = random.randint(1, 10)
        slot2_turtle.write(str(slot2), font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.1)

        slot3_turtle.setpos(100, 0)
        slot3_turtle.clear()
        slot3 = random.randint(1, 10)
        slot3_turtle.write(str(slot3), font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.1)

    turtle.onkey(None, "space")
    turtle.clear()
    slot1_turtle.clear()
    slot2_turtle.clear()
    slot3_turtle.clear()


########################################
# The calculate_winnings() function calculates how much the user won or lost(winnings) in a round based on
# their bet amount(bet_amount) and any sequences in the slots
########################################


def calculate_winnings():
    global slot1, slot2, slot3, bet_amount, winnings, bank

    turtle.setpos(0, 50)

    winnings = 0

    if slot1 == slot2 == slot3:
        turtle.write("Three of a kind", font=(FONT_TYPE, FONT_SIZE), align="center")
        winnings = bet_amount * 10
    elif slot2 == slot1 + 1 and slot3 == slot2 + 1:
        turtle.write("straight", font=(FONT_TYPE, FONT_SIZE), align="center")
        winnings = bet_amount * 5
    elif slot1 == slot3:
        turtle.write("outside match", font=(FONT_TYPE, FONT_SIZE), align="center")
        winnings = bet_amount * 3
    elif slot1 == slot2 or slot2 == slot3:
        turtle.write("side by side match", font=(FONT_TYPE, FONT_SIZE), align="center")
        winnings = bet_amount * 2
    else:
        turtle.write("no match", font=(FONT_TYPE, FONT_SIZE), align="center")
        winnings = -bet_amount

    bank = bank + winnings


########################################
# The end_screen() function writes the values of the three slots, winnings, and bank to the turtle screen
########################################


def end_screen():
    global slot1, slot2, slot3, bank, winnings

    turtle.setpos(-250, 200)
    turtle.write("Slot 1: " + str(slot1), font=(FONT_TYPE, FONT_SIZE), align="center")
    turtle.setpos(0, 200)
    turtle.write("Slot 2:" + str(slot2), font=(FONT_TYPE, FONT_SIZE), align="center")
    turtle.setpos(250, 200)
    turtle.write("Slot 3:" + str(slot3), font=(FONT_TYPE, FONT_SIZE), align="center")
    turtle.setpos(0, -25)
    turtle.write('Winnings/losses: ' + str(winnings), font=(FONT_TYPE, FONT_SIZE), align="center")
    turtle.setpos(0, -100)
    turtle.write('Bank: ' + str(bank), font=(FONT_TYPE, FONT_SIZE), align="center")


########################################
# The end_program() changes the variables not_done_check, not_done_game, not_done_main to end the program
########################################


def end_program():
    global not_done_game, not_done_check, not_done_main
    not_done_game = False
    not_done_check = False
    not_done_main = False


########################################
# The continue_game() changes the variable not_done_check to exit the while loop in
# check_end_game to play again
########################################


def continue_game():
    global not_done_check
    not_done_check = False


########################################
# The start_game() changes the variable not_done_check to exit the while loop in check_end_game() and
# changes not_done_game to false to end the game and start a new one
########################################


def start_new_game():
    global not_done_game, not_done_check
    not_done_game = False
    not_done_check = False


########################################
# The check_end_game() function checks if the user wishes to end the game or continue.
# If the game user wishes to end the game or their bank balance is less than 0 the game is ended
########################################


def check_end_game():
    global not_done_check
    if bank > 0:

        turtle.setpos(0, 290)
        turtle.color(FONT_COLOUR_ALT)
        turtle.write("Round Complete", font=(FONT_TYPE, FONT_SIZE), align="center")
        turtle.onkey(end_program, "q")
        turtle.onkey(continue_game, "Return")
        turtle.listen()
        turtle.setpos(0, -300)

        not_done_check = True
        while not_done_check:
            turtle.color(FONT_COLOUR)
            turtle.write("Press q to quit,\nEnter to play again", font=(FONT_TYPE, FONT_SIZE), align="center")
            time.sleep(0.25)
            turtle.color(FONT_COLOUR_ALT)
            turtle.write("Press q to quit,\nEnter to play again", font=(FONT_TYPE, FONT_SIZE), align="center")
            time.sleep(0.25)
    else:
        turtle.setpos(0, 290)
        turtle.color(FONT_COLOUR_ALT)
        turtle.write("Game Over", font=(FONT_TYPE, FONT_SIZE), align="center")
        turtle.onkey(end_program, "q")
        turtle.onkey(start_new_game, "Return")
        turtle.listen()

        turtle.setpos(0, -300)

        not_done_check = True
        while not_done_check:
            turtle.color(FONT_COLOUR)
            turtle.write("Press q to quit,\n Enter to start new game", font=(FONT_TYPE, FONT_SIZE), align="center")
            time.sleep(0.25)
            turtle.color(FONT_COLOUR_ALT)
            turtle.write("Press q to quit,\n Enter to start new game", font=(FONT_TYPE, FONT_SIZE), align="center")
            time.sleep(0.25)

    turtle.onkey(None, "q")
    turtle.onkey(None, "Return")

    turtle.clear()


########################################
# The calculate_high_score() function sorts the top ten scores from SlotHighScores.dat and adds them to the
# list (high_scores) of the current bank is in the top 10 it is added to the list and the values are reentered to the
# file. a parallel array (score_names) holds the names of the scorers to be saved to the list
# Local Variables
# my_file               refers to the "SlotsHighScores.dat" file
# not_done_sort         boolean variable set to True while there are still numbers to compare and sort
# position              remembers the current position in the list while sorting
########################################


def calculate_high_score():
    global name, high_scores, score_names
    my_file = open("SlotHighScores.dat", 'r')

    for i in range(10):
        score_names.append(my_file.readline().strip())
        score = my_file.readline()
        score = int(score.strip())
        high_scores.append(score)

    my_file.close()

    not_done_sort = True
    position = 9

    # find position where new_number is lower and select the posision before knowing new_number is higher
    while not_done_sort:
        if bank >= high_scores[position]:
            if position != 0:  # check next number
                position = position - 1
            else:  # positions <= any score on the list
                not_done_sort = False

        else:  # not higher then current position
            not_done_sort = False
            position = position + 1

    # if new_number should be on list add it and remove lowest
    if position < 10:
        high_scores.insert(position, bank)
        del (high_scores[10])

        score_names.insert(position, name)
        del (score_names[10])

    my_file = open("SlotHighScores.dat", 'w')

    for i in range(10):
        my_file.writelines(score_names[i] + "\n")
        my_file.writelines(str(high_scores[i]) + "\n")

    my_file.close()


########################################
# The save_game() function save te current bank ballance to SaveSlotGame.dat
########################################


def save_game():
    global not_done_check
    not_done_check = False
    save_file = open("SaveSlotGame" + name + ".dat", "w")
    save_file.write(str(bank) + "\n")
    save_file.close()


########################################
# check_save_game() function asks the user if they would like to save their game.
# If so it calls save_game() if not it calls continue_game()
########################################


def check_save_game():
    global not_done_check

    if bank > 0:
        not_done_check = True

        turtle.onkey(save_game, "s")
        turtle.onkey(continue_game, "Return")
        turtle.listen()

        save_turtle.setpos(0, 0)
        while not_done_check:
            save_turtle.color(FONT_COLOUR)
            save_turtle.write("Press s to save game,\n"
                              "Enter to exit without saving",
                              font=(FONT_TYPE, FONT_SIZE), align="center")
            time.sleep(0.5)
            save_turtle.clear()
            save_turtle.color(FONT_COLOUR_ALT)
            save_turtle.write("Press s to save game,\n"
                              "Enter to exit without saving",
                              font=(FONT_TYPE, FONT_SIZE), align="center")
            time.sleep(0.5)
            save_turtle.clear()

        turtle.onkey(None, "s")
        turtle.onkey(None, "Return")
        turtle.clear()


########################################
# The display_bank_amount() function writes the balance of the bank to the screen at the x and y coordinates
# specified by the parameters
########################################


def display_bank_amount(x, y):
    bank_turtle.color(FONT_COLOUR)
    bank_turtle.color(FONT_COLOUR)
    bank_turtle.setpos(x, y)
    bank_turtle.clear()
    bank_turtle.write('Bank: ' + str(bank), font=(FONT_TYPE, str((int(FONT_SIZE) - 20))), align="center")


########################################
# The display_bet_amount() function writes the amount bet to the screen at the x and y coordinates
# specified by the parameters
########################################


def display_bet_amount(x, y):
    global bet_amount, bet_amount_turtle
    bet_amount_turtle.color(FONT_COLOUR)
    bet_amount_turtle.setpos(x, y)
    bet_amount_turtle.clear()
    bet_amount_turtle.write('Bet: ' + str(bet_amount), font=(FONT_TYPE, str((int(FONT_SIZE) - 20))), align="center")


########################################
# The display_high_scores() function displays the list of high scores to the screen
########################################


def display_high_scores():
    global bool_to_change, not_done_instructions, high_scores, score_names

    turtle.color(FONT_COLOUR)
    turtle.setpos(0, 250)
    turtle.write("High Scores\n"
                 "Name:________________Score:",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="Center")

    for i in range(len(high_scores)):
        turtle.goto(0, i*30-100)
        turtle.write(score_names[i] + "________________"  + str(high_scores[i]),
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 25)), align="Center")


# main  program
not_done_main = True

while not_done_main:
    initialize_game()
    instructions_screen()
    time.sleep(1)
    while name == "":
        get_name()
    check_save()
    intro_screen()

    not_done_game = True

    while not_done_game:
        get_bet_amount()
        display_bank_amount(-100, 350)
        display_bet_amount(100, 350)
        draw_machine()
        spin_slots()
        machine_turtle.clear()
        calculate_winnings()
        end_screen()
        bet_amount_turtle.clear()
        display_bank_amount(-100, 350)
        display_bet_amount(100, 350)
        check_end_game()

        if not_done_game == False:
            display_bank_amount(-100, 350)
            display_bet_amount(100, 350)
            calculate_high_score()
            check_save_game()

    display_bank_amount(-100, 350)
    display_bet_amount(100, 350)

display_high_scores()
turtle.exitonclick()
