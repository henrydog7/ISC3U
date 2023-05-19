######################################################################
# Average of 7 Numbers Program
#
# Lucas Balog
# Creating Date: Sep 26, 2020
# Modify Date: N/A
#
# File Name: U04P01Average7.py
# Other Files: none
#
# Program Description
#
# program ask for the user to input seven numbers. stores numbers in list.
# it then adds all the numbers together 
# calculates mean average and reports back to user
#
# Documented Errors
# 
# program crashes if letter in entered
#
# Variable List
# numbers       list that stores all the numbers entered by user
# i             counter for loop to get each number from the user
######################################################################
numbers = []
for i in range(7):
    numbers.append(int(input("Enter Number " + str(i+1) + ":")))
print("Total: ", sum(numbers), "\n" + "Average: ", round((sum(numbers)/7), 2))
