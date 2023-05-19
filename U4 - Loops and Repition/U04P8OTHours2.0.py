########################################
# Over Time Hours Calcualtor Program

# Lucas Balog
# Creation date: Oct. 5, 2020
# Modified date: Oct. 6,2020

# U04P08OTHours2.0.py
# other files: none

# The program will deterimin the amount of overtime hours, if any, the employee has worked

# update: added detection for blank strings created by pressing enter with no value typed

# Documented Errors
# N/A


# Variable List
# hours                 Holds the toal number of hours the employee has worked
# regular_hours         Holds the total number of regular hours the employee has worked
# ot_hours              Holds the total numbe  of regualr hours the employee has worked

########################################

########################################
# The get_hours() function ask the user to input the number of hours the employee has worked.
# it then check to see if it is a quarter hour, less then 90, a posative number, and not a string
########################################

def get_hours():
    repeat_hours_loop = True
    global hours, regular_hours, ot_hours

    while repeat_hours_loop:
        hours = input("Input hours:")
        try:
            hours = float(hours)
            if hours == "":
                print("Please enter a value")
            elif hours % 0.25 != 0:
                print ("Hours must be in quater hours")
            elif hours > 90:
                print ("Total Hours are too high, limit 90")
            elif hours < 0:
                print ("Hours cannot be a negative")
            else:
                repeat_hours_loop = False
        except ValueError:
            if hours == "":
                print("Please enter a value")
            else:
                print ("That is not a valid number")

########################################
# The calculate_ot() function ca;culates how many of the employees hours are regular 
# and how many are over time hours
########################################

def calcualte_ot():
    global hours, regular_hours, ot_hours

    if hours <= 40:
        regular_hours= hours
        ot_hours = 0
    elif hours > 40:
        regular_hours = 40
        ot_hours = hours-40

########################################
# The display_hours() function labels prints and formates the hours,
# regualr hours and over time hours the employee worked
########################################

def display_hours():
    print("Total Hours:", '{0:12.2f}'.format(hours))
    print("Regular Hours:", '{0:10.2f}'.format(regular_hours))
    print("Over Time Hours:",'{0:8.2f}'.format(ot_hours))

#main program

repeat_main_loop = True

while repeat_main_loop:
    get_hours()
    calcualte_ot()
    display_hours()

    awnser = input("Would you like to start again? (Y/N):").upper()
    repeat_main_loop = awnser[0] != "N"