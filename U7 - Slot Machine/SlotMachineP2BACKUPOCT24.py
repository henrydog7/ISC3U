########################################
# Slot Machine Program

# Lucas Balog
# Creation date: Oct. 21, 2020
# Modified date:

# SlotMachineP3.py
# other files: none

# The program

# Documented Errors
#

# Variable List
# not_done_game         boolean variable used to determin wearther to run game or end program
# not_done_spin         boolean variable used to determin wearther to spin slots or end loop
# slot1                 holds the number between 1 and 10 that has been randomly generated
# slot2                 holds the number between 1 and 10 that has been randomly generated
# slot3                 holds the number between 1 and 10 that has been randomly generated
# bet_num               holds the number the user bet on
# bet_amount            holds the amount the user bet
# bank                  holds the amount of virtual money the user has
# winnings              holds the amount the user won each round
# high_scores           list used to remeber the high scores of the user
# window                variable used to control the turtle window
# run_screen            boolean variable used to determin weather to run the intro_screen() loop or exit
# run_ask_load          boolean variable used to determin weather to run the check_save() loop or exit
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
# TODO
# The get_info() function has the user input the names and ages.
# ages is check to make sure if is an int
# Local Variable List
# not_done          boolean variable used by while loop to determine if input loop needs to run again due to an error
########################################


def initialize_game():
    global slot1, slot2, slot3, bet_num, bet_amount, bank, winnings, high_scores,\
        window, FONT_SIZE, FONT_TYPE, FONT_COLOUR, FONT_COLOUR_ALT, BG_COLOUR

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
# TODO
# The get_info() function has the user input the names and ages.
# ages is check to make sure if is an int
# Local Variable List
# not_done          boolean variable used by while loop to determine if input loop needs to run again due to an error
########################################


def check_save():
    global  window, bool_to_change, run_ask_load

    save_file = open("SaveSlotGame.dat", "r")
    saveed_bank = save_file.readline()
    save_file.close()

    if saveed_bank != "":

        bool_to_change = "run_ask_load"
        turtle.onkey(end_section, "n")
        turtle.onkey(load_game, "y")
        turtle.listen()

        run_ask_load = True
        while run_ask_load:
            turtle.color(FONT_COLOUR)
            turtle.write("Saved game detected\nwould you like to load? y/n", font=(FONT_TYPE, FONT_SIZE), align="center")
            time.sleep(0.5)
            turtle.color(FONT_COLOUR_ALT)
            turtle.write("Saved game detected\nwould you like to load? y/n", font=(FONT_TYPE, FONT_SIZE), align="center")
            time.sleep(0.5)

        turtle.clear()
        print(bank)


########################################
# TODO
# The end_intro_screen() function changes the run_screen variable to False to end the intro_screen loop
########################################


def end_section():
    globals()[bool_to_change] = False


########################################
# TODO
# The end_intro_screen() function changes the run_screen variable to False to end the intro_screen loop
########################################

def load_game():
    global run_ask_load
    save_file = open("SaveSlotgame.dat","r")
    bank = str(save_file.readline())
    run_ask_load = False

########################################
# The intro_screen() function displays instruction for the game and continues when enter is pressed
########################################


# TODO write instructions
# TODO make look better
def intro_screen():
    global run_screen, bool_to_change
    run_screen = True

    bool_to_change = "run_screen"
    window.onkey(end_section, "Return")
    window.listen()
    while run_screen:
        turtle.color(FONT_COLOUR)
        turtle.write("Press enter to begin", font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.5)
        turtle.color(FONT_COLOUR_ALT)
        turtle.write("Press enter to begin", font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.5)
    turtle.clear()
    # turtle.bye()


########################################
# TODO
# The get_bets() function has the user input the number they are betting on (bet_num) and
# the amount they bet(bet_amount) in a multiple of 5. The inputs are error checked an
########################################


def get_bet_num():
    global bet_num, bool_to_change, bet_turtle

    not_done_gbn= True

    while not_done_gbn:
        bet_num = tkinter.simpledialog.askinteger("Bet", "Please enter your bet")
        if bet_num <= 10 and bet_num >= 1:
            not_done_gbn = False
        else:
            tkinter.messagebox.showwarning("Number out of range", "Number must be between 1 and 10")

    turtle.clear()


########################################
# TODO
# The get_bets() function has the user input the number they are betting on (bet_num) and
# the amount they bet(bet_amount) in a multiple of 5. The inputs are error checked an
########################################


def bet_up():
    global bet_amount, bet_turtle

    bet_amount = bet_amount + 5
    bet_turtle.clear()
    bet_turtle.setpos(0, 0)
    bet_turtle.write(str(bet_amount), font=(FONT_TYPE, FONT_SIZE), align="center")


########################################
# TODO
# The bet_down() function has the user input the number they are betting on (bet_num) and
# the amount they bet(bet_amount) in a multiple of 5. The inputs are error checked an
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
# is asked to re enter if nessisarry
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

    #set up onkney() functions
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
        instructions_turtle.write("Press enter to select", font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.5)
        instructions_turtle.color(FONT_COLOUR_ALT)
        instructions_turtle.write("Press enter to select", font=(FONT_TYPE, FONT_SIZE), align="center")
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
# TODO
# The spin_slots() function randomly generates three numbers and siplays them to the screen (slot1, slot2, slot3)
# all number are between 1 and 10.

# Local Variable List
# TODO document special turtle variables
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

    slot1_turtle.clear()
    slot2_turtle.clear()
    slot3_turtle.clear()


########################################
# TODO
# The calculate_winnings() function calculates how much the user won in a roudn based on thier bed and
# if there are any winning sequances
########################################


def calculate_winnings():
    global slot1, slot2, slot3, bet_num, bet_amount, winnings, bank

    slot1_and_2_match = slot1 == bet_num and slot2 == bet_num
    slot2_and_3_match = slot2 == bet_num and slot3 == bet_num
    slot1_and_3_match = slot1 == bet_num and slot3 == bet_num
    all_match = slot1 == bet_num and slot2 == bet_num and slot3 == bet_num

    turtle.setpos(0,50)
    if slot1 == bet_num or slot2 == bet_num or slot3 == bet_num:
        if slot1_and_2_match or slot2_and_3_match:
            turtle.write("side by side match", font=(FONT_TYPE, FONT_SIZE), align="center")
            winnings = bet_amount*2
        elif slot1_and_3_match:
            turtle.write("outside match", font=(FONT_TYPE, FONT_SIZE), align="center")
            winnings = bet_amount * 3
        elif all_match:
            turtle.write("Three of a kind", font=(FONT_TYPE, FONT_SIZE), align="center")
            winnings = bet_amount * 10
        elif slot2 == bet_num + 1 and slot3 == bet_num + 2:
            turtle.write("straight slot 1", font=(FONT_TYPE, FONT_SIZE), align="center")
            winnings = bet_amount * 5
        elif slot1 == bet_num - 1 and slot3 == bet_num + 1:
            turtle.write("straight slot 2", font=(FONT_TYPE, FONT_SIZE), align="center")
            winnings = bet_amount * 5
        elif slot1 == bet_num - 2 and slot2 == bet_num - 1:
            turtle.write("straight slot 3", font=(FONT_TYPE, FONT_SIZE), align="center")
            winnings = bet_amount * 5
        else:
            turtle.write("number in slot but no match", font=(FONT_TYPE, FONT_SIZE), align="center")
            winnings = -bet_amount
    else:
        turtle.write("not match", font=(FONT_TYPE, FONT_SIZE), align="center")
        winnings = -bet_amount

    bank = bank + winnings



########################################
# The display_results() function wites the values of the three slots to the turtle screen
########################################


def display_results():
    global slot1, slot2, slot3, bank

    turtle.setpos(-250, 200)
    turtle.write("Slot 1: " + str(slot1), font=(FONT_TYPE, FONT_SIZE), align="center")
    turtle.setpos(0, 200)
    turtle.write("Slot 2:" + str(slot2), font=(FONT_TYPE, FONT_SIZE), align="center")
    turtle.setpos(250, 200)
    turtle.write("Slot 3:" + str(slot3), font=(FONT_TYPE, FONT_SIZE), align="center")
    turtle.setpos(0,0)
    turtle.write('Bank: ' + str(bank), font=(FONT_TYPE, FONT_SIZE), align="center")



########################################
# TODO
# The continue_game() changes the variable not_done_check to exit the while loop in
# # check_end_game and the variable not_done_main in the main program to exit the program
########################################


def end_game():
    global not_done_game, not_done_check
    not_done_game = False
    not_done_check = False


########################################
# The continue_game() changes the variable not_done_scheck to exit thw while loop in
# check_end_game to play again
########################################


def continue_game():
    global not_done_check
    not_done_check = False


########################################
# TODO
# The check_end_game() function checks if the user wishes to end th game or continue
########################################



def check_end_game():
    global not_done_check
    if bank > 0:

        turtle.onkey(end_game, "q")
        turtle.onkey(continue_game, "Return")
        turtle.listen()
        turtle.setpos(0,-200)

        not_done_check = True
        while not_done_check:
            turtle.color(FONT_COLOUR)
            turtle.write("Press q to quit,\n Enter to play again", font=(FONT_TYPE, FONT_SIZE), align="center")
            time.sleep(0.25)
            turtle.color(FONT_COLOUR_ALT)
            turtle.write("Press q to quit,\n Enter to play again", font=(FONT_TYPE, FONT_SIZE), align="center")
            time.sleep(0.25)
    turtle.clear()

########################################
# The save_game() function save te surrent bank ballance to SaveSlotGame.dat
########################################


def save_game():
    global not_done_check
    not_done_check = False
    save_file = open("SaveSlotGame.dat", "w")
    save_file.write(str(bank) + "\n")

########################################
# TODO
# check_save_game() functon asl the user if they would like to sace their game. if so it calls save_game()
########################################



def check_save_game():
    global not_done_check
    not_done_check = True
    print("in check save game")

    turtle.onkey(save_game, "s")
    turtle.onkey(continue_game, "Return")
    turtle.listen()
    turtle.setpos(0,0)
    while not_done_check:
        turtle.color(FONT_COLOUR)
        turtle.write("Press s to save game,\n enter to exit without saving", font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.25)
        turtle.color(FONT_COLOUR_ALT)
        turtle.write("Press s to save game,\n enter to exit without saving", font=(FONT_TYPE, FONT_SIZE), align="center")
        time.sleep(0.25)

    turtle.clear()
########################################
# The calculate_high_score() function sort the top ten socres and adds them to the list
########################################


def calculate_high_score():
    global high_scores
    my_file = open("SlotHighScores.dat", 'r')


    for i in range(10):
        high_scores.append(int(my_file.readline()))

    print(high_scores)

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

    print(high_scores)

########################################
# TODO
# The display_results() function wites the values of the three slots to the screen
########################################


def display_bank_amount():
    global bank
    turtle.setpos(0,400)
    turtle.write('Bank: ' + str(bank), font=(FONT_TYPE, str((int(FONT_SIZE)-20))), align="center")


# main  program


initialize_game()
check_save()
intro_screen()

not_done_game = True

while not_done_game:
    get_bet_num()
    get_bet_amount()
    spin_slots()
    calculate_winnings()
    display_results()
    check_end_game()
    if not_done_game == False:
        display_bank_amount()
        check_save_game()


display_bank_amount()
calculate_high_score()
turtle.exitonclick()
