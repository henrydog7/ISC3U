########################################
# Calculate Average Program

# Lucas Balog
# Creation date: Oct. 10, 2020
# Modified date: 

# U05A03.py
# other files: none

# The program has the user select how many number to gerate between 5 and 10.
# This ammount o numbers are gereated from numbers betwwen -5 and 10 then put on a list
# These number are displayed to the user. The average of the numbers is then calculated and displayed.

# Documented Errors
# 


# Variable List
# amount_of_nums            holds the amount of numbers to generate as specified by the usere
# some_numbers[]            list contaning the randomly generated numbers
# some_numbers_total        holds the total of all the numbers added
# some_numbers_avg          holds the mean average of all the numbers

########################################

import random

########################################
# The get_num_elements() function has the user input the amount of numbers to generate(amount_of_nums)
# the inout is error checked to ensure it is an int between 5 and 10

# Local Variable List
# not_done          used by the while loop to determine if the number needs to be reentered due to an error
########################################

def get_num_elements():
    global amount_of_nums
    not_done = True
    while not_done:
        try:
            amount_of_nums = int(input("How many numbers?"))
            if amount_of_nums <= 10 and amount_of_nums >= 5:
                not_done = False
            else:
                print("number must be between 5 and 10")
        except ValueError:
            print("Input must be a number")

########################################
# The fill_list() function will randomly genreate the number and place them in list some_numbers()
# the amount of numbers generated is from the get_num_elements() function and stored in amount_of_nums
########################################

def fill_list():
    global some_numbers, amount_of_nums

    for k in range(amount_of_nums):
        some_numbers.append(random.randint(-5,10))

########################################
# The display_list() function displays the numbers in the list (some_numbers()) and adds a comma in between each number
########################################

def display_list():
    for i in range(len(some_numbers)):
        if i < len(some_numbers)-1:
            print (some_numbers[i], end = ", ")
        else:
            (print(some_numbers[i]))

########################################
# The calc_avg() function calculates the total(some_numbers_total) of all the numbers.
# from this total the average (some_numbers_avg) is calculated and displayed
########################################

def calc_avg():
    global some_numbers_total, some_numbers_avg
    some_numbers_total = 0
    for i in range(len(some_numbers)):
        some_numbers_total = some_numbers_total + some_numbers[i]
    some_numbers_avg = some_numbers_total/amount_of_nums
    print(some_numbers_avg)




some_numbers = []


get_num_elements()
fill_list()
display_list()
calc_avg()