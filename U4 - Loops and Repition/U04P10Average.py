######################################################################
# Average Calculator Program

# Lucas Balog
# Creating Date: Oct 10, 2020
# Modify Date:

# File Name: U04P10Average.py
# Other Files: none

# Program Description
# program allows the user to enter a list of numbers.
# the average is calculated and reported

# Documented Errors

# Variable List
# total         remembers the total of all the numbers added
# how_many      remembers how many numbers have been entered
# average       renembers the average of all the numbers after being calculated
# not_done      used by while loop to determin to run again or exit
######################################################################

not_done = True
total = 0
how_many = 0
while not_done:
    number = input("Enter Number")
    if number == "e":
        not_done = False
    else:
        total = total+int(number)
        how_many = how_many+1
average = total/how_many
print("the average is:",round(average,2))