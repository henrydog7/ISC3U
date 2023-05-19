######################################################################
# Higest of 10 proram

# Lucas Balog
# Creating Date: Oct 10, 2020
# Modify Date: N/A

# File Name: U04p9Higest.py
# Other Files: none

# Program Description
# program has the user input ten numbers. it records the higest number 
# and how many times it was entered. it reports this information back to the user

# Documented Errors

# Variable List
# Number        remebers the nu,ber entered by the user
# Highest       remebrs the current higest number
# num_times     remembers the number of times the current higest numbe has been entered


######################################################################
number = int(input("Enter a number"))
highest = number
num_times = 1
for i in range (9):
    number = int(input("Enter a Number"))

    if number > highest:
        highest = number
        num_times = 1
    elif number == highest:

        num_times = num_times + 1

print ("The higest number is:",highest)
print ("the number of times it was entered was:",num_times)