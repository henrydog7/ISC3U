########################################
# Slot Machine Program

# Lucas Balog
# Creation date: Oct. 21, 2020
# Modified date:

# SlotMachineP2-2.0.py
# other files: SaveSlotGame.dat

# The program runs a lot machine game. The user is asked to bet on a number between 1 and 10 and to enter an
# amount of virtual money to bet. three numbers are rondomly genrated and displayed unill the user pressed space.
# if there are any designated sequances the user is awarded their winnigns in their virtual bank acount. if there
# are not losses the bet is subtracted from their account. the user stars with 200$. the user can save after every spin.
# if the user looses all their money they must quit or start a new game.

# Documented Errors
# none

# Variable List
# not_done_game         boolean variable used to determine wearther to run game or end program
# not_done_spin         boolean variable used to determine wearther to spin slots or end loop
# not_done_gba          boolean variable used to determine wearther program has recived the bet amount
# slot1                 holds the number between 1 and 10 that has been randomly generated
# slot2                 holds the number between 1 and 10 that has been randomly generated
# slot3                 holds the number between 1 and 10 that has been randomly generated
# bet_num               holds the number the user bet on
# bet_amount            holds the amount the user bet
# bank                  holds the amount of virtual money the user has
# winnings              holds the amount the user won each round
# high_scores           list used to remeber the high scores of the user
# window                variable used to control the turtle window
# run_screen            boolean variable used to determine weather to run the intro_screen() loop or exit
# run_ask_load          boolean variable used to determine weather to run the check_save() loop or exit
# bool_to_change        used by end_section() function to change the bool of this name to False
# FONT_SIZE             constant variable used to set the standard font size
# FONT_TYPE             constant variable used to set the standard font type
# FONT_COLOUR           constant variable used to set the standard font colour
# FONT_COLOUR_ALT       constant variable used to set the standard font alternet colour
# BG_COLOUR             constant variable used to set the back gorund colour
########################################


import random
import time
import tkinter
import turtle


########################################
# The initialize_game function delaris and initalizes all the gloabl variables
########################################


def initialize_game():
    global slot1, slot2, slot3, bet_num, bet_amount, bank, winnings, high_scores, \
        window, bool_to_change, FONT_SIZE, FONT_TYPE, FONT_COLOUR, FONT_COLOUR_ALT, BG_COLOUR

    slot1 = slot2 = slot3 = bet_num = winnings = 0
    bet_amount = 5
    bank = 200
    high_scores = []
    bool_to_change = ""

    FONT_SIZE = "46"
    FONT_TYPE = "Arial"
    FONT_COLOUR = "gold4"
    FONT_COLOUR_ALT = "gray72"
    BG_COLOUR = "black"

    window = turtle.Screen()
    window.bgcolor(BG_COLOUR)
    turtle.setup(1000, 1000, 0, 0)
    turtle.setheading(270)
    turtle.hideturtle()
    turtle.up()


########################################
# The check_save game function checks to see if there is a game saved in SaveSlotGame.dat. if so it ask if the user
# would like to load the game. if they awnser yes("y") load_game() is called and the game bank ballance is loaded.

# Local Variable List
# save_file             refers to the SaveSLotGame.dat file
# saved_bank            used to hold the bank ballance read from SaveSlotgame.dat
########################################


def check_save():
    global window, bool_to_change, run_ask_load

    save_file = open("SaveSlotGame.dat", "r")
    saved_bank = save_file.readline()
    save_file.close()

    if saved_bank != "":

        bool_to_change = "run_ask_load"
        turtle.onkey(end_section, "n")
        turtle.onkey(load_game, "y")
        turtle.listen()

        run_ask_load = True
        while run_ask_load:
            turtle.color(FONT_COLOUR)
            turtle.write("Saved game detected\nwould you like to load? y/n", font=(FONT_TYPE, FONT_SIZE),
                         align="center")
            time.sleep(0.5)
            turtle.color(FONT_COLOUR_ALT)
            turtle.write("Saved game detected\nwould you like to load? y/n", font=(FONT_TYPE, FONT_SIZE),
                         align="center")
            time.sleep(0.5)

        turtle.clear()


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
    save_file = open("SaveSlotgame.dat", "r")
    bank = int(save_file.readline())
    run_ask_load = False
    save_file.close()


########################################
# The intro_screen() function displays instruction for the game and continues when enter is pressed
########################################


def intro_screen():
    global run_screen, bool_to_change
    run_screen = True

    bool_to_change = "run_screen"
    window.onkey(end_section, "Return")
    window.listen()

    turtle.setpos(0, 200)
    turtle.color(FONT_COLOUR)
    turtle.write("Welcome to the game!\n"
                 "once started select number to bet on and amount of money to bet\n"
                 "press space to stop spinning\n"
                 "fallow instructions to play again or leave",
                 font=(FONT_TYPE, str(int(FONT_SIZE) - 20)), align="center")

    prompt_turtle = turtle.Turtle()
    prompt_turtle.setpos(0, -300)
    prompt_turtle.penup()
    prompt_turtle.hideturtle()
    while run_screen:
        prompt_turtle.color(FONT_COLOUR)
        prompt_turtle.write("Press enter to begin", font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.5)
        prompt_turtle.clear()
        prompt_turtle.color(FONT_COLOUR_ALT)
        prompt_turtle.write("Press enter to begin", font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.5)
        prompt_turtle.clear()
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
        bet_turtle.write(str(bet_amount), font=(FONT_TYPE, FONT_SIZE), align="center")


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
        bet_turtle.write(str(bet_amount), font=(FONT_TYPE, FONT_SIZE), align="center")


########################################
# The get_bet_amount() function has the user input the number they are betting on (bet_num) and
# the amount they bet(bet_amount) in a multiple of 5. The inputs are error checked and the user
# is asked to re enter if necessary
# Local Variable List
# bet_turtle                    refers to the turtle used to draw the on bet amount on screen
# instructions_turtle           refers to the turtle used to draw the on screen instructions
########################################


def get_bet_amount():
    global bet_amount, bool_to_change, bet_turtle, not_done_gba

    # set up bet turtle
    bet_turtle = turtle.Turtle()
    bet_turtle.up()
    bet_turtle.color(FONT_COLOUR)
    bet_turtle.hideturtle()

    # set up instructions turtle
    instructions_turtle = turtle.Turtle()
    instructions_turtle.up()
    instructions_turtle.hideturtle()

    # set up onkney() functions
    bool_to_change = "not_done_gba"
    turtle.onkey(end_section, "Return")
    turtle.onkey(bet_up, "Up")
    turtle.onkey(bet_down, "Down")
    turtle.listen()

    # set up canvas
    bet_turtle.clear()
    bet_turtle.setpos(0, 0)
    bet_turtle.write(str(bet_amount), font=(FONT_TYPE, FONT_SIZE), align="center")

    # write instructions to entert bet
    instructions_turtle.setpos(0, -200)

    not_done_gba = True
    while not_done_gba:
        instructions_turtle.color(FONT_COLOUR)
        instructions_turtle.write("Press enter to select\n"
                                  "Arrows to move up or down",
                                  font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.5)
        instructions_turtle.color(FONT_COLOUR_ALT)
        instructions_turtle.write("Press enter to select\n"
                                  "Arrows to move up or down",
                                  font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.5)

    bet_turtle.clear()
    instructions_turtle.clear()


########################################
# The stop_spin() function changes the not_done_spin variable to False to end the spin_slot loop
########################################


def stop_spin():
    global not_done_spin
    not_done_spin = False


########################################
# The spin_slots() function randomly generates three numbers and displays them to the screen (slot1, slot2, slot3)
# all number are between 1 and 10 and individualy cleared and redrawn. this continues untill space is pressed

# Local Variable List
# slot1_turtle          used to draw and clear the slot 1 value
# slot2_turtle          used to draw and clear the slot 2 value
# slot3_turtle          used to draw and clear the slot 3 value
########################################


def spin_slots():
    global slot1, slot2, slot3, not_done_spin
    not_done_spin = True
    slot1_turtle = turtle.Turtle()
    slot2_turtle = turtle.Turtle()
    slot3_turtle = turtle.Turtle()
    turtle.clear()

    slot1_turtle.color(FONT_COLOUR)
    slot2_turtle.color(FONT_COLOUR)
    slot3_turtle.color(FONT_COLOUR)

    slot1_turtle.hideturtle()
    slot2_turtle.hideturtle()
    slot3_turtle.hideturtle()

    slot1_turtle.up()
    slot2_turtle.up()
    slot3_turtle.up()

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
# The display_results() function wites the values of the three slots, winnings, and bank to the turtle screen
########################################


def display_results():
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
# The end_game() changes the variables not_done_check, not_done_game, not_done_main to end the program
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

        turtle.setpos(0, 300)
        turtle.color(FONT_COLOUR_ALT)
        turtle.write("Round Compleate", font=(FONT_TYPE, FONT_SIZE), align="center")
        turtle.onkey(end_program, "q")
        turtle.onkey(continue_game, "Return")
        turtle.listen()
        turtle.setpos(0, -300)

        not_done_check = True
        while not_done_check:
            turtle.color(FONT_COLOUR)
            turtle.write("Press q to quit,\n Enter to play again", font=(FONT_TYPE, FONT_SIZE), align="center")
            time.sleep(0.25)
            turtle.color(FONT_COLOUR_ALT)
            turtle.write("Press q to quit,\n Enter to play again", font=(FONT_TYPE, FONT_SIZE), align="center")
            time.sleep(0.25)
    else:
        turtle.setpos(0, 300)
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
    turtle.clear()


########################################
# The save_game() function save te current bank ballance to SaveSlotGame.dat
########################################


def save_game():
    global not_done_check
    not_done_check = False
    save_file = open("SaveSlotGame.dat", "w")
    save_file.write(str(bank) + "\n")
    save_file.close()


########################################
# check_save_game() functon asks the user if they would like to save their game.
# If so it calls save_game() if not it calls continue_game()
########################################


def check_save_game():
    global not_done_check

    if bank > 0:
        not_done_check = True

        turtle.onkey(save_game, "s")
        turtle.onkey(continue_game, "Return")
        turtle.listen()
        turtle.setpos(0, 0)
        while not_done_check:
            turtle.color(FONT_COLOUR)
            turtle.write("Press s to save game,\n"
                         "Enter to exit without saving",
                         font=(FONT_TYPE, FONT_SIZE), align="center")
            time.sleep(0.25)
            turtle.color(FONT_COLOUR_ALT)
            turtle.write("Press s to save game,\n"
                         "Enter to exit without saving",
                         font=(FONT_TYPE, FONT_SIZE), align="center")
            time.sleep(0.25)

    turtle.clear()


########################################
# The calculate_high_score() function sort the top ten socres and adds them to the list

# this component is in development and not used in this version
########################################


def calculate_high_score():
    global high_scores
    my_file = open("SlotHighScores.dat", 'r')

    for i in range(10):
        high_scores.append(int(my_file.readline()))

    my_file.close()

    not_done_sort = True
    position = 9

    # find posision where new_number is lower and select the posision before knowing new_number is higher
    while not_done_sort:
        if winnings >= high_scores[position]:
            if position != 0:  # check next number
                position = position - 1
            else:  # positions <= any score on the list
                not_done_sort = False

        else:  # not higher then current position
            not_done_sort = False
            position = position + 1

    # if new_number shoudld be on list add it and remove lowest
    if position < 9:
        scores.insert(position, new_score)
        names.insert(position, new_name)
        del (scores[9])
        del (names[9])


########################################
# The display_bank_amount() function wites the balance of the bank to the screen
########################################


def display_bank_amount():
    global bank
    turtle.setpos(0, 400)
    turtle.write('Bank: ' + str(bank), font=(FONT_TYPE, str((int(FONT_SIZE) - 20))), align="center")


# main  program

not_done_main = True

while not_done_main:
    initialize_game()
    check_save()
    intro_screen()

    not_done_game = True

    while not_done_game:
        get_bet_amount()
        spin_slots()
        calculate_winnings()
        display_results()
        check_end_game()
        if not_done_game == False:
            display_bank_amount()
            check_save_game()

    display_bank_amount()
turtle.exitonclick()
