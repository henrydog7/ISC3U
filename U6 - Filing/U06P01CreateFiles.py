########################################
# Filing Prgram

# Lucas Balog
# Creation date: Oct. 23, 2020
# Modified date:

# U06P01CreateFiles.py
# other files: none

# The program ask the user to input their choice of operation. based on this the program
# will create a new file, add to an existing file, display/verify a file, format a file
# or exit the program

# Documented Errors
# none

# Variable List
# choice                    used to determine the function the user wishes to run
# not_done_main             boolean variable used to determin if to run again or exit
########################################


########################################
# The get_choice() function propmts the user to input a number(choice) between 1 and 5.
# this number is used by the main program to determine what function to run.

# Local Variable List
# not_done_get_choice           used on while loop to repeat if there is an error
########################################
def get_choice():
    global choice

    print("1.	Start a New File\n"
          "2.	Add to an Existing File\n"
          "3.	Verify File\n"
          "4.	Format File\n"
          "5.	Exit")

    not_done_get_choice = True
    while not_done_get_choice:
        try:
            choice = int(input("Enter choice"))
            if choice < 1 or choice > 5:
                print("Value must be from 1-5")
            else:
                not_done_get_choice = False
        except ValueError:
            print("Input must be a number")


########################################
# The get_choice() function propmts the user to input a number(choice) between 1 and 5.
# this number is used by the main program to determine what function to run.

# Local Variable List
# not_done_get_choice           used on while loop to repeat if there is an error
########################################


def start_new_file():

    file_name = input("Please enter file name")
    new_file = open(file_name + ".dat", 'w')

    print("Enter done to first name when finished")

    not_done_new_file = True
    while not_done_new_file:
        first_name = input("Please enter first name: ")
        if first_name != "done":
            new_file.write(first_name + "\n")
            last_name = input("please last name: ")
            new_file.write(last_name + "\n")
            age = input("please enter age: ")
            new_file.write(age + "\n")
        else:
            not_done_new_file = False
    new_file.close()


########################################
# The add_to_existing_file()


# Local Variable List
# not_done_existing_file        boolean file used in while loop to decided to continue writing
#                               information or end based on user input
# file_name                     used to hold the name of the files after input
# existing_file                 used to refer to the file with the information being writen to
########################################


def add_to_existing_file():

    try:
        file_name = input("please enter file name")
        existing_file = open(file_name + ".dat", 'a')

        print("enter done to first name when finished")

        not_done_existing_file = True
        while not_done_existing_file:
            first_name = input("Please enter first name: ")
            if first_name != "done":
                existing_file.write(first_name + "\n")
                last_name = input("please last name: ")
                existing_file.write(last_name + "\n")
                age = input("please enter age: ")
                existing_file.write(age + "\n")
            else:
                not_done_existing_file = False

        existing_file.close()
    except FileNotFoundError:
        print("File Cannot be found")


########################################
# The verify_file() function proms the user to enter a file name. The infomation in the
# file is then printed to the console

# Local Variable List
# file_name                 name of file to be displayed
# not_done_verify_file      boolean variable used by while loop to determine to continue
#                           printing or end
# file                      used to refer to the file with the information being read
########################################


def verify_file():
    file_name = input("please enter file name")
    try:
        file = open(file_name + ".dat", 'r')

        not_done_verify_file = True

        while not_done_verify_file:
            line = file.readline()
            if line != "":
                print(line.strip())
            else:
                not_done_verify_file = False

        file.close()

    except FileNotFoundError:
        print("File Cannot be found")


########################################
# The format_file() function prpms the user to input the name of a current file and
# new file. The information is read from the current file and it is formatted to the new file
# Format:
#       last name: 30 available characters, left-justified.
#       first name: 20 available characters, left-justified
#       age: 8 available characters, centred

# Local Variable List
# file_name                 name of file to be displayed
# not_done_format_file      boolean variable used by while loop to determine to continue
#                           printing or end
# file_found                boolean variable used to determine if the files are available
# current_file              used to refer to the file with the information being read
# new_file                  used to refer to the file with the information being writen to
# first_name                holds the first name in a set of information
# last_name                 holds the last name in a set of information
# age                       holds the age in a set of information
########################################


def format_file():

    file_found = True
    try:
        file_name = input("please enter current file name")
        current_file = open(file_name + ".dat", 'r')
    except FileNotFoundError:
        print("File Cannot be found")
        file_found = False

    if file_found:
        try:
            file_name = input("please enter new file name")
            new_file = open(file_name + ".dat", 'w')
        except FileNotFoundError:
            print("File Cannot be found")
            file_found = False
            current_file.close()

    if file_found:
        not_done_format_file = True

        while not_done_format_file:
            first_name = current_file.readline().strip()
            if first_name != "":
                last_name = current_file.readline().strip()
                age = current_file.readline().strip()

                new_file.write(last_name.ljust(30) + first_name.ljust(20) + age.rjust(8) + "\n")
            else:
                not_done_format_file = False

        current_file.close()
        new_file.close()


########################################
# The exit_program() function changes the global not_done_main variable to False to
# end the main loop and program
########################################


def exit_program():
    global not_done_main
    not_done_main = False


# main program

not_done_main = True

while not_done_main:
    get_choice()
    if choice == 1:
        start_new_file()
    elif choice == 2:
        add_to_existing_file()
    elif choice == 3:
        verify_file()
    elif choice == 4:
        format_file()
    else:
        exit_program()
