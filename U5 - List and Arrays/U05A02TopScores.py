########################################
# Top Scores Program

# Lucas Balog
# Creation date: Oct. 9, 2020
# Modified date: May. 5, 2021

# U05A02TopScores.py
# other files: none

# The program will sort the top five scores in a list from higest to lowest.
# for demonstration perposes the score is randomly generated between 100-300.
# the user inputs the name for each score. this name is displayed with the high score.
# UPDATE: Added Feature to only take the first leter input when asked to continue

# Documented Errors
# 


# Variable List
# new_score         holds the score input by the user
# new_name          holds the name input by the user
# scores[]          list holding the top 5 scores            
# names[]           list holding the names accossiated with the top 5 scores
# not_done_main     boolen variable used for main while loop to determin if to enter a new score

########################################

import random


########################################
# The get_score_name() function randomly generates the score(new_score) and has the name input 
# by the user (new_name)
########################################

def get_score_name():
    global new_name, new_score
    new_score = random.randint(100, 300)
    print("Score Is:", new_score)
    new_name = input("Enter Name: ")


########################################
# The update_list function determins if the score (new_score) ishigher than a score in the top five(score[])
# if it is the score is placed in the sorret order and the lowest number is removed. the list of names (names[])
# is updated accoridngly

# Local Variable List
# not_done_sort         boolen variable used by while loop to determin if sorting is compleated
# position              variable used to remember place in list
########################################


def update_list():
    global names, scores, new_score, new_name
    not_done_sort = True
    position = 4

    # find posision where new_number is lower and select the posision before knowing new_number is higher
    while not_done_sort:
        if new_score >= scores[position]:
            if position != 0:  # check next number
                position = position - 1
            else:  # positions <= any score on the list
                not_done_sort = False

        else:  # not higher then current position
            not_done_sort = False
            position = position + 1

    # if new_number shoudld be on list add it and remove lowest
    if position < 5:
        scores.insert(position, new_score)
        names.insert(position, new_name)
        del (scores[5])
        del (names[5])
        return True


########################################
# The display_list() function checks if the users score was placed in the top 5.
# If it was the user is shown th etop five list. if not the user is told they are not
# in the top 5 and the top 5 are not displayed. 
########################################

def display_list(score_on_list):
    global names, scores

    if score_on_list:
        print("Congratulations!!! You are in the top 5")
        print("Names:".ljust(10), "Scores:".rjust(10))
        for i in range(5):
            print(names[i].ljust(10), '{0:10}'.format(scores[i]))
    else:
        print("Sorry, you are not in the top 5")


########################################
# The see_more() function allows the user to choose to continue adding names or exit
# the program.

# Local Variable List
# not_good_input        boolen variable used by the while loop to determin if the loop needs
#                       to run again due to an invalid input
########################################

def see_more():
    global not_done_main
    not_good_input = True
    while not_good_input:
        command_input = input("Would you like to quite(Q) or continue(C): ")
        if command_input[0].upper() == "Q":
            not_good_input = False
            not_done_main = False
        elif command_input[0].upper() == "C":
            not_good_input = False
            not_done_main = True
        else:
            
            print("Please enter 'Q' or 'C'")


# main program

names = ["xxx", "xxx", "xxx", "xxx", "xxx"]
scores = [0, 0, 0, 0, 0]

not_done_main = True
while not_done_main:
    get_score_name()
    if update_list():
        display_list(True)
    else:
        display_list(False)
    see_more()
