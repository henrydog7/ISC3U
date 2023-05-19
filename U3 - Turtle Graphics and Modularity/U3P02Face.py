######################################################################
# Face

# Lucas Balog
# Creating Date: Sep 24, 2020
# Modify Date: N/A

# File Name: U03P02Face.py
# Other Files: none

# Program Description
#   program randomly generates a number between 1 and 3. Draws a face using the turtle library.
#   Face will either be happy -1, indifferent -2, or sad -3.

# Documented Errors
#    N/A
# Variable List
# START_X           Constant variable used as a central point for x values to base positions from
# START_Y           Constant variable used as a central point for y values to base positions from
# face_type         Contains the number to determine what face to display
# bgcolour          Contains the background colour of the window depending on the type being displayed
# face_colour       Contains the face colour on the  type being displayed
######################################################################

import random
import turtle


######################################################################
# function draw a square given the length od the sides and starting x,y coordinates

# Variable List
# length     Length of the sides of the square
# xpos       starting x position of the square measuring point is bottom right corner of square
# xpos       starting y position of the square measuring point is bottom right corner of square
# colour     colour the shape will be filled with
######################################################################

def draw_square(length, xpos, ypos, colour):
    turtle.fillcolor(colour)
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
# colour     colour the shape will be filled with
# counter    keeps track of position in loop
######################################################################

def draw_mouth_happy(xpos, ypos, colour):
    turtle.fillcolor(colour)
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
# function draws the mouth of the face given starting x,y coordinates

# Variable List
# xpos       starting x position of the mouth measuring point is bottom right corner of square
# xpos       starting y position of the mouth measuring point is bottom right corner of square
# colour     colour the shape will be filled with
# counter    keeps track of position in loop
######################################################################

def draw_mouth_indifferent(xpos, ypos, colour):
    turtle.fillcolor(colour)
    turtle.setpos(xpos, ypos)

    turtle.begin_fill()

    turtle.setheading(0)
    turtle.forward(160)
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(160)
    turtle.setheading(270)
    turtle.forward(50)

    turtle.end_fill()


######################################################################
# function draws the mouth of the face given starting x,y coordinates

# Variable List
# xpos       starting x position of the mouth measuring point is bottom right corner of square
# xpos       starting y position of the mouth measuring point is bottom right corner of square
# colour     colour the shape will be filled with
# counter    keeps track of position in loop
######################################################################

def draw_mouth_sad(xpos, ypos, colour):
    turtle.fillcolor(colour)
    turtle.setpos(xpos, ypos)

    turtle.begin_fill()

    turtle.setheading(0)
    turtle.forward(150)
    turtle.setheading(-80)
    turtle.forward(50)
    turtle.setheading(-230)
    turtle.forward(20)
    turtle.setheading(-180)
    turtle.forward(130)
    turtle.setheading(-130)
    turtle.forward(20)
    turtle.setheading(-280)
    turtle.forward(50)
    turtle.setheading(0)

    turtle.end_fill()


######################################################################
# function draw a equilateral triangle given the length od the sides and starting x,y coordinates

# Variable List
# length     Length of the sides of the triangle
# xpos       starting x position of the triangle measuring point is bottom right corner of square
# ypos       starting y position of the triangle measuring point is bottom right corner of square
# colour     colour the shape will be filled with
# counter    keeps track of position in loop
######################################################################

def draw_triangle(length, xpos, ypos, colour):
    turtle.fillcolor(colour)
    turtle.setpos(xpos, ypos)
    turtle.begin_fill()
    for counter in range(3):
        turtle.forward(length)
        turtle.setheading(turtle.heading() + 1200)
    turtle.end_fill()


######################################################################
# function draws the eyes of the face given the starting x,y coordinates

# Variable List
# xpos       starting x position of the square measuring point middle of eye
# xpos       starting y position of the square measuring point is bottom right corner of square
# outer_colour     colour the outer circle will be filled with
# inner_colour     colour the inner circle will be filled with
######################################################################

def draw_eye(xpos, ypos, outer_colour, inner_colour):
    # draw outer eye
    turtle.fillcolor(outer_colour)
    turtle.setpos(xpos, ypos - 12.5)
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()

    # draws inner eye
    turtle.fillcolor(inner_colour)

    turtle.setpos(xpos, ypos)
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()


# start of program

START_X = -150
START_Y = -150
face_type = random.randint(1, 3)
bgcolour = "white"
face_colour = "blue"
# set up canvas
turtle.title("Face")
turtle.speed(0)
turtle.up()
turtle.hideturtle()
turtle.setheading(0)

# decide what dace to draw

if face_type == 1:  # happy
    face_colour = "yellow"
    bgcolour = "purple"
    print("happy")
    turtle.bgcolor(bgcolour)
    draw_square(300, START_X, START_Y, face_colour)
    draw_mouth_happy(START_X + 70, START_Y + 50, bgcolour)
elif face_type == 2:  # indifferent
    face_colour = "grey"
    bgcolour = "white"
    print("indifferent")
    turtle.bgcolor(bgcolour)
    draw_square(300, START_X, START_Y, face_colour)
    draw_mouth_indifferent(START_X + 70, START_Y + 50, bgcolour)
elif face_type == 3:  # sad
    face_colour = "blue"
    bgcolour = "GreenYellow"
    print("sad")
    turtle.bgcolor(bgcolour)
    draw_square(300, START_X, START_Y, face_colour)
    draw_mouth_sad(START_X + 70, START_Y + 80, bgcolour)

# draws triangle nose

turtle.setheading(0)
draw_triangle(50, START_X + 125, START_Y + 130, bgcolour)

# draw left eye

turtle.setheading(0)
draw_eye(START_X + 90, START_Y + 200, bgcolour, face_colour)

# draw right eye

turtle.setheading(0)
draw_eye(START_X + 210, START_Y + 200, bgcolour, face_colour)

turtle.exitonclick()
