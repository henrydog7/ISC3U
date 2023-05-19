########################################
# Grade Program

# Lcuas Balog
# Creation date: Oct 6, 2020
# Modified date:

# U03P11.py
# other files: none

# The program will determine the letter grade for a student based on their percent grade

# Documented Errors
# none


# Variable List
# grade                 remembers the percent grade input by user
# not_done              remembers if the current while loop still needs to execute or not
# text_color            remembers the colour for the text based on the letter grade
# letter_grade          remembers the letter grade after being calculated
# string                remembers the combined string to be writen by the turtle

########################################


import turtle


########################################
# The  get_grade() function ask the user for the grade and check to see if it is not a
# letter, number higher than 100, negative number. If so it ask the user again
########################################


def get_grade():
    global grade
    not_done = True
    while not_done:
        try:
            grade = round(float(input("Please enter the Mark:")), 2)
            if grade > 100:
                print("The mark you entered was too high. You must enter a mark from 0-100.")
            elif grade < 0:
                print("The mark you entered was too low. You must enter a mark from 0-100.")
            else:
                not_done = False
        except ValueError:
            print("You must enter a numeric value for the mark.")


########################################
# The determine_letter() function determines the letter grade and colour of the text based on the value of the grade
########################################


def determine_letter():
    global letter_grade, text_color
    if grade >= 80:
        letter_grade = "A"
        text_color = "gold3"
    elif grade >= 70:
        letter_grade = "B"
        text_color = "Green"
    elif grade >= 60:
        letter_grade = "C"
        text_color = "yellow"
    elif grade >= 50:
        letter_grade = "D"
        text_color = "orange"
    else:
        letter_grade = "F"
        text_color = "red"

########################################
# The display_letter function generates a turtle window and writes the percent grade,
# and letter grade. the colour of the text changes based on grade value as determined in
# the determine_grade() function.
########################################

def display_letter():
    turtle.title("Grade")
    turtle.speed(0)
    turtle.up()
    turtle.hideturtle()
    turtle.setheading(0)
    global text_color
    turtle.clear()
    string = "A mark of " + str(grade) + " is a " + letter_grade + "."
    turtle.setpos(0, 0)
    turtle.color(text_color)
    turtle.write(string, font=("Britannic", 40, "normal"), align="Center")


# Start of Program



get_grade()
determine_letter()
display_letter()

turtle.exitonclick()
