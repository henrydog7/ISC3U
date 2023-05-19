######################################################################
# Multiplication Tables Program
#
# Lucas Balog
# Creating Date: Sep 26, 2020
# Modify Date: N/A
#
# File Name: U04P03MultiTable.py
# Other Files: none
#
# Program Description
#
# program ask for the user to input start and end numbers
# program then generates and reports multiplication table of 1-12 for the first number
# program repeats this for every number untill end number tabel is generated and reported
#
# Documented Errors
# 
# program crashes if letter in entered 
#
# Variable List
# number_one        the start number entered by the user
# number_two        the end number entered by the user
# j                 counter for first loop repeating table to table
# i                 counter for second loop to repeat for each number of the table
######################################################################
number_one = int(input("Enter the start value for the multiplication tables:"))
number_two = int(input("Enter the end value for the multiplication tables:"))
for j in range (number_one, number_two+1):
    for i in range(1,13):
        print("{0:3}".format(j),"x", "{0:3}".format(i),"=", "{0:6}".format(j*i))
    print("\n")