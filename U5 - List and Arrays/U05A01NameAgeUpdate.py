########################################
# Name and Age Program Update

# Lucas Balog
# Creation date: Oct. 20, 2020
# Modified date: 

# U05A01NameAgeUpdate.py
# other files: none

# The program ask the user to input 5 names and ages to be stored in parallel list.
# The names and ages are sorted from youngest to oldest, oldest to youngest, or alphabetically based
# on what the user chooses. It is then siplayed in a turtle window.

# Documented Errors
# characters or numbers at the start of names do not sort 


# Variable List
# name[]            list remembering the names input
# ages[]            list remembering the ages input
# choice            remembers how the user wishes to sort the information
# not_done_main     boolean variable used todetermin wearther to run sorting again or end program

########################################
import turtle, string
########################################
# The get_info() function has the user input the names and ages.
# ages is check to make sure if is an int
# Local Variable List
# not_done          boolean variable used by while loop to determine if input loop needs to run again due to an error
########################################


def get_info():
    global names, ages
    names = []
    ages = []


    for i in range(5):
        names.append(input("Enter the Name:"))
        not_done = True
        while not_done:
            try:
                ages.append(int(input("Enter the age for " + str(names[i]) + ":")))
                not_done = False
            except ValueError:
                print("age must be a number please try again")


########################################
# The get_order has the user input their choice of sorting(choice). this input is error check to ensure
# it is a digit from 1-4
# Local Variable List
# not_done_get_order          boolean variable used by while loop to determine if
#                             input loop needs to run again due to an error
########################################


def get_order():
    global choice
    print("1.".ljust(10), "Oldest to Youngest".rjust(10))
    print("2.".ljust(10), "Youngest to Oldest".rjust(10))
    print("3.".ljust(10), "Alphabetical Order".rjust(10))
    print("4.".ljust(10), "Quit".rjust(10))

    not_done_get_order = True
    while not_done_get_order:
        try:
            choice = int(input("Enter Choice: "))
            if 0 < choice < 5:
                not_done_get_order = False
            else:
                print("Input must be from 1 to 4")
        except ValueError:
            print("Input must be a number")


########################################
# The sort_old_young() function sorts the names and ages from oldest to youngest.
# the while loop moves items down the list untill it is larger then all before it.
# this repeats for each position until the order is correct.
# Local Variable List
# not_done_sort     boolean variable used by while loop to determine if sorting needs to continue
# pos               holds the position in the three list while sorting
# age_temp          used to temperaroly hold the age of a position while switching values
# name_temp         used to temperaroly hold the name of a position while switching values
########################################


def sort_old_young():
    global names, ages

    pos = 0

    not_done_sort = True
    while not_done_sort:

        if ages[pos] < ages[pos+1]:
            age_temp = ages[pos]
            name_temp = names[pos]
            ages[pos] = ages[pos + 1]
            names[pos] = names[pos + 1]
            ages[pos + 1] = age_temp
            names[pos + 1] = name_temp
            pos = 0
        elif pos < 3:
            pos = pos+1
        else:
            not_done_sort = False


########################################
# The sort_young_old() function sorts the names and ages from youngest to oldest.
# the while loop moves items up the list untill it is larger then all before it.
# this repeats for each position until the order is correct.

# Local Variable List
# not_done_sort          boolean variable used by while loop to determine if sorting needs to continue
# pos                    holds the position in the two list while sorting
# age_temp               used to temperaroly hold the age of a position while switching values
# name_temp              used to temperaroly hold the name of a position while switching values
########################################


def sort_young_old():
    global names, ages

    pos = 4

    not_done_sort = True
    while not_done_sort:

        if ages[pos] < ages[pos-1]:
            age_temp = ages[pos]
            name_temp = names[pos]
            ages[pos] = ages[pos - 1]
            names[pos] = names[pos - 1]
            ages[pos - 1] = age_temp
            names[pos - 1] = name_temp
            pos = 4
        elif pos > 1:
            pos = pos-1
        else:
            not_done_sort = False
            print(pos)


########################################
# The sort_alphabetical() function sorts the list alphabetically when called.
# the first letter of the names area ssigened a number based on their location in the alphabet("a" = 1)
# from this value the names and ages are then sorted

# Local Variable List
# not_done _sort             boolean variable used by while loop to determine if sorting needs to continue
# alpabet_positions[]        list paralel with ages[] and names[]. The numbers in the list coresponds with the
#                            first alphabetical position of the first letter of the name. Ex "a" = 1
# alphabet[]                 list populated with the string library. holds all the letters of the alphabet
# pos_name                   holds the position in the names list that is being compaired
# pos_alphabet               holds the position in the alphabet list of the letter being compaired
# pos                        holds the position in the three list while sorting
# age_temp                   used to temperaroly hold the age of a position while switching values
# name_temp                  used to temperaroly hold the name of a position while switching values
# alphabet_positions_temp    used to temperaroly hold the alpahabet position of a position while switching values
########################################


def sort_alphabetical():
    global names, ages
    alphabet_positions = []
    alphabet = list(string.ascii_lowercase)

    for pos_name in range(5):
        for pos_alphabet in range(26):
            if (names[pos_name][0]).lower() == (alphabet[pos_alphabet][0]):
                alphabet_positions.append(pos_alphabet)

    pos = 4
    not_done_sort = True
    while not_done_sort:

        if alphabet_positions[pos] < alphabet_positions[pos - 1]:
            age_temp = ages[pos]
            name_temp = names[pos]
            alphabet_positions_temp = alphabet_positions[pos]
            alphabet_positions[pos] = alphabet_positions[pos - 1]
            names[pos] = names[pos - 1]
            ages[pos] = ages[pos - 1]
            ages[pos - 1] = age_temp
            names[pos - 1] = name_temp
            alphabet_positions[pos-1] = alphabet_positions_temp
            pos = 4
        elif pos > 1:
            pos = pos - 1
        else:
            not_done_sort = False


########################################
# The display_info() function displays the names and ages in two collums useing a turtle window. 
########################################


def display_info():
    global names, ages

    turtle.setup(1000,1000,10,10)
    turtle.setheading(270)
    turtle.hideturtle()
    turtle.up()
    turtle.bgcolor("black")
    turtle.color("gold4")
    turtle.setpos(-150,150)
    turtle.write("Names:", font=("Arial", 56, "normal"))
    turtle.setpos(150,150)
    turtle.write("Ages:", font=("Arial", 56, "normal"))
    for i in range(5):
        turtle.setpos(-150,100-i*50)
        turtle.write(str(names[i]),  font=("Arial", 36, "normal"))
        turtle.setpos(150,100-i*50)
        turtle.write(str(ages[i]),  font=("Arial", 36, "normal"))


# main program

get_info()
not_done_main = True
while not_done_main:
    get_order()
    if choice == 1:
        sort_old_young()
    elif choice == 2:
        sort_young_old()
    elif choice == 3:
        sort_alphabetical()

    if choice == 4:
        not_done_main = False
    else:
        display_info()
