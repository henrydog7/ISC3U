########################################
# Name and Gae Program

# Lucas Balog
# Creation date: Oct. 9, 2020
# Modified date: 

# U05A01NameAge.py
# other files: none

# The program ask the user to input 5 names and ages to be stored in parallel list.
# The names and ages are reported back to the sure in revers order from how they were entered

# Documented Errors
# 


# Variable List
# name[]        list remembering the names input
# ages[]        list remembering the ages input

########################################

########################################
# The get_info() function has the user input the names and ages.
# ages is check to make sure if is an int
# Local Variable List
# not_done          boolen variable used by while loop to determin if input loop needs to run again due to an error
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
# The display_info() function displays the names and ages in two collums. 
# the namea nd ages are displayed in the oposite order they are entered.
########################################

def display_info():
    global names, ages
    print("Names:".ljust(10), "Ages:".rjust(10))
    for i in range(4, -1, -1):
        print(names[i].ljust(10), str(ages[i]).rjust(6))


# main program

get_info()
display_info()
