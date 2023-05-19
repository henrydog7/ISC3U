######################################################################
# Multiplication Table Program
#
# Lucas Balog
# Creating Date: Sep 26, 2020
# Modify Date: N/A
#
# File Name: U04P02MultiTable.py
# Other Files: none
#
# Program Description
#
# program ask for the user to input a number
# program then generates and reports multiplication table of 1-12 for the number 
#
# Documented Errors
# 
# program crashes if letter in entered 
#
# Variable List
# number    the number for the multiplication table entered by the user
# i         counter for loop to repeat for each number of the table
######################################################################
number = int(input("Enter the value for the multiplication table:"))
for i in range(1,13):
    print("{0:3}".format(number),"x", "{0:3}".format(i),"=", "{0:6}".format(number*i))