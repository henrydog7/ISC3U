######################################################################
## Growing squares Program
##
## Lucas Balog
## Creating Date: Sep 27, 2020
## Modify Date: N/A
##
## File Name: U04P04GrowSquare.py
## Other Files: none
##
## Program Description
##
## Prgoram draws five squares with the same top left corrner
## Each square has sides twice the length of the previous
##
## Documented Errors
##
## None
##
## Variable List
##
## shape_counter        counts how many squares have been drawn and is used to calculate length of sides
## square_counter       counts how many sides of the square have been drawn
######################################################################
import turtle
for shape_counter in range(1,6):
    for square_counter in range (4):
        turtle.forward(50*shape_counter)
        turtle.right(90)