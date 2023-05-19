######################################################################
# Face

# Lucas Balog
# Creating Date: Sep 23, 2020
# Modify Date: N/A

# File Name: U03P01Happy.py
# Other Files: none

# Program Description
#   Draws a face useing the turtle library

# Documented Errors
#    N/A
# Variable List
# START_X           Constant variable used as a central point for x values to base positions from
# START_Y           Constant variable used as a central point for y values to base positions from
######################################################################
import turtle


######################################################################
# function draw a square given the length od the sides and starting x,y coordinates

# Variable List
# lenght     Length of the sides of the square
# xpos       starting x position of the square measuring point is bottom right corner of square
# xpos       starting y position of the square measuring point is bottom right corner of square
######################################################################

def draw_square(length, xpos, ypos):
    turtle.fillcolor("blue")
    turtle.setpos(xpos, ypos)
    turtle.begin_fill()
    for counter in range(4):
        turtle.forward(length)
        turtle.setheading(turtle.heading() + 90)
    turtle.end_fill()


######################################################################
# function draws the mouth of the face given starting x,y coordinates

# Variable List
# xpos       starting x position of the mouth measuring point is bottom right corner of square
# xpos       starting y position of the mouth measuring point is bottom right corner of square
# counter    keeps track of position in loop
######################################################################

def draw_mouth(xpos, ypos):
    turtle.fillcolor("white")
    turtle.setpos(xpos, ypos)

    turtle.begin_fill()

    turtle.setheading(0)
    turtle.forward(150)
    turtle.setheading(80)
    turtle.forward(50)
    turtle.setheading(230)
    turtle.forward(20)
    turtle.setheading(180)
    turtle.forward(130)
    turtle.setheading(130)
    turtle.forward(20)
    turtle.setheading(280)
    turtle.forward(50)
    turtle.setheading(0)

    turtle.end_fill()


######################################################################
# function draw a equilateral triangle given the length od the sides and starting x,y cordinates

# Variable List
# length     Length of the sides of the triangle
# xpos       starting x position of the triangle measuring point is bottom right corrner of square
# ypos       starting y position of the triangle measuring point is bottom right corrner of square
# counter    keeps track of position in loop
######################################################################

def draw_triangle(length, xpos, ypos):
    turtle.setpos(xpos, ypos)
    turtle.begin_fill()
    for counter in range(3):
        turtle.forward(length)
        turtle.setheading(turtle.heading() + 1200)
    turtle.end_fill()


######################################################################
# function draws the eyes of the face gieven the starting x,y cordinates

# Variable List
# xpos       starting x position of the square measuring point middle of eye
# xpos       starting y position of the square measuring point is bottom right corrner of square
######################################################################

def draw_eye(xpos, ypos):
    # draw outer eye
    turtle.fillcolor("white")
    turtle.setpos(xpos, ypos - 12.5)
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()

    # draws inner eye
    turtle.fillcolor("blue")

    turtle.setpos(xpos, ypos)
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()


# start of program

START_X = -150
START_Y = -150

# set up canvas
turtle.title("Face")
turtle.fillcolor("blue")
turtle.speed(0)
turtle.up()
turtle.hideturtle()

# draws base square

draw_square(300, START_X, START_Y)

# draws mouth

draw_mouth(START_X + 70, START_Y + 50)

# draws triangle nose

draw_triangle(50, START_X + 125, START_Y + 130)

# draw left eye

draw_eye(START_X + 90, START_Y + 200)

# draw right eye

draw_eye(START_X + 210, START_Y + 200)

turtle.exitonclick()