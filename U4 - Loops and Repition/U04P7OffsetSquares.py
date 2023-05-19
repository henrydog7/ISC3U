######################################################################
## Offset Squares Program
##
## Lucas Balog
## Creating Date: Sep 27, 2020
## Modify Date: N/A
##
## File Name: U04P04OffsetSquares.py
## Other Files: none
##
## Program Description
##
## program draws 12 squares. all with the same start point rotated 90 degrees to the right 
## and 30 units bigeger then the last
##
## Documented Errors
##
## None
##
## Variable List
##
## j        used to count how many squares have been draw
## i        used to count how many sides of the square have been drawn
######################################################################
import turtle
for j in range (12):
    for i in range(4):
        turtle.forward(30*(j+1))
        turtle.right(90)
    turtle.right(90)
turtle.exitonclick()