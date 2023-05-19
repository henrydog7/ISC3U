######################################################################
# Guessing Game

# Lucas Balog
# Creating Date: Oct 10, 2020
# Modify Date:

# File Name: GuessingGamePhase3.py
# Other Files: none

# Program Description
# program ask user to choose number of rounds. it then generates a random number between 1 and 100
# the use goes takes to guess the number. They get accuracy points based on how close they are to the number and bonus
# points based on how many guesses they take. bonus and accuracy points combine to equal round points.
# the points of each round are combines to equal total points or the points of the entire game. if the user
# enters a number outside of the 0-100 range they loose 25 points. when a user getts the correct awnser a graphical
# window using the turtle library displays a message.

# Documented Errors
# Turtle Window becomes unresponsive when new round started

# Variable List
#
# num_rounds            the number of rounds the user selected to play
# num_guess             the number the user guessed
# round_guesses         the number of guesses in a round
# total_guesses         the number of guesses in a game
# num_answer            the number randomly generated for the user to guess
# average_guesses       the average number rof guesses per round in a game
# points{}              a dictionary containing all the points
#       "accuracy"      the points earned in a round based on accuracy
#       "round"         the points earned in a round
#       "bonus"         the points earned in a round based on the number of guesses
#       "total"         the total points earned in a game
# not_done              used to determine if a while loop should run


######################################################################

import random
import turtle

########################################
# The initialize_game() function initializes the variables required for the game
########################################


def initialize_game():
    global num_rounds, num_guess, round_guesses, total_guesses, num_answer, average_guesses, points
    num_rounds = num_guess = round_guesses = total_guesses = num_answer = average_guesses = 0
    points = {"round": 0, "bonus": 0, "accuracy": 0, "total": 0}


########################################
# The get_rounds() asl the user to select the number of rounds to play.
# the number is error checked and converted to an int. the program repeats in a while loop
# until a valid number is input

# Local Variable List
# not_done          used to communicate if the error checking while loop can be exited
########################################


def get_rounds():
    global num_rounds

    not_done = True
    while not_done:
        try:
            num_rounds = int(input("Enter Number of Rounds"))
            if num_rounds <= 0:
                print("rounds must be larger than 0")
            else:
                not_done = False
        except ValueError:
            print("Input must be a number")


########################################
# The initialize_round() function sets all the round variables to their starting values
# for a round (rounds, points["round", "bonus", "accuracy"], round guesses)
# it then generates a random number (round_answer) for the user to guess
########################################


def initialize_round():
    global points, num_answer, round_guesses, rounds
    print("\n")
    print("Round", rounds+1)
    points["round"] = points["bonus"] = points["accuracy"] = round_guesses = 0
    num_answer = random.randint(1, 100)


########################################
# The get_guess(min_number, max_number) function takes the parameters of the minimum and maximum numbers.
# The guessed number(num_guess) is inoout by the user and error checked. If the guessed number is outside
# the range set by the min and max numbers the user is alerted and 25 points are removed. if the input is
# not a number the user is alerted. the user will be continually asked to input a number until it meets the
# min, max and character type requirements.

# Local Variable List
# min_number        the minimum number of the acceptable range
# max_number        the maximum number of the acceptable range
# not_done          used to communicate if the error checking while loop can be exited
########################################


def get_guess(min_number, max_number):
    global num_guess, round_guesses, points
    not_done = True
    while not_done:
        try:
            num_guess = int(input("Enter your Guess"))
            if num_guess < min_number:
                print("Number below minimum", min_number, ". -25 points")
                points["round"] = points["round"] - 25
            elif num_guess > max_number:
                print("Number above maximum", max_number, ". -25 points")
                points["round"] = points["round"] - 25
            else:
                round_guesses = round_guesses+1
                not_done = False
        except ValueError:
            print("guess must be a number")


########################################
# The check_high_low() function takes the entered guess (num_guess) and compaires it
# to the randomly generated answer (num_answer). it tells the user if the number is too high,
# too low, or correct
########################################


def check_high_low():
    global num_guess, num_answer
    if num_guess < num_answer:
        print("guess too low")
    elif num_guess > num_answer:
        print("guess too high")
    else:
        print("guess is correct")


########################################
# The check_accuracy() function check how close the guessed number(num_guess)
# is to the randomly generated answer number (num_answer). accuracy points(points["accuracy"])
# are assigned based on how close it is 30 points for within 5, 10 points for within 15, and
# 2 points for within 30. a custom message for eac category plus a category for more than 30
# is displayed to the user to hint how close they are
########################################


def check_accuracy():
    global num_guess, num_answer, points
    if num_guess == num_answer:
        pass
    elif num_guess >= num_answer - 5 and num_guess <= num_answer + 5:
        print("Oh! So close!")
        points["accuracy"] = points["accuracy"] + 30
    elif num_guess >= num_answer - 15 and num_guess <= num_answer + 15:
        print("That was a good guess!")
        points["accuracy"] = points["accuracy"] + 10
    elif num_guess >= num_answer - 30 and num_guess <= num_answer + 30:
        print("That is a long way away.")
        points["accuracy"] = points["accuracy"] + 2
    else:
        print("That is a long way away.")


########################################
# The update_user() function calculates th points earned in the current round and reports
# the accuracy points(points["accuracy"]), round points(points["round"]),
# bonus points(points["bonus"]), round guesses(round_guesses), and total points(points["total"])
########################################


def update_user():
    global points

    points["round"] = points["bonus"] + points["accuracy"] + points["round"]
    print("\n")
    print("Points - Accuracy:" + str(points["accuracy"]), end=" ")
    print("Points - Round:" + str(points["round"]), end=" ")
    print("Points - Bonus:" + str(points["bonus"]), end=" ")
    print("Guesses - Round:" + str(round_guesses), end=" ")
    print("Points - Total:" + str(points["total"]))


########################################
# The check_bonus_points() function gives the user bonus points(points["bonus"]) based
# on how many guesses (num_guess) it took them to get the correct answer(num_answer).
# 100 for 3 or less, 50 for 4-6, 20 for 7-10, 5 for 11-15
########################################


def check_bonus_points():
    global round_guesses, points, num_guess, num_answer
    if num_guess == num_answer:
        if round_guesses <= 3:
            points["bonus"] = points["bonus"]+100
        elif round_guesses <= 6:
            points["bonus"] = points["bonus"]+50
        elif round_guesses <= 10:
            points["bonus"] = points["bonus"]+20
        elif round_guesses <= 15:
            points["bonus"] = points["bonus"]+5


########################################
# The show_win() function draws a graphical message with the turtle library.
# the message tells the user they win and how many guesses(round_guesses) they made that round.
########################################


def show_win():
    global round_guesses

    turtle.clear()
    turtle.setpos(0, 0)
    turtle.color("gold4")
    turtle.write("You Win!", font=("Britannic", 40, "normal"), align="Center")
    turtle.setpos(0, -100)
    turtle.write("It took " + str(round_guesses) + " guesses to get the answer",
                 font=("Britannic", 40, "normal"), align="Center")
    turtle.setpos(0, -200)
    turtle.color("black")


########################################
# The avg guess function calculates the average number of guesses(average_guesses).
# the is done by dividing the total guesses (total_guesses), by the total
# number of rounds (num_rounds)
########################################


def avg_guess():
    global total_guesses, num_rounds, average_guesses
    average_guesses = total_guesses//num_rounds
    print("The average number of guesses was", average_guesses)
    print("The Total Points are", points["total"])

# Main Program


initialize_game()
get_rounds()

turtle.title("Score")
turtle.speed(0)
turtle.up()
turtle.hideturtle()
turtle.setheading(0)

for rounds in range(num_rounds):

    initialize_round()

    while num_guess != num_answer:

        get_guess(1, 100)
        check_high_low()
        check_accuracy()
        update_user()

    check_bonus_points()
    points["total"] = points["round"]+points["accuracy"]+points["bonus"]+points["total"]

    update_user()
    show_win()
    total_guesses = total_guesses + round_guesses

avg_guess()

turtle.exitonclick()
