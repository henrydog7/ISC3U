######################################################################
## Circle art program
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
## program draws 4 sets of 8 circles
## all circles satart at the same point with the furthest side being pointed 
## 45 degrees away from the last circle
## each set of 8 gets bigger
##
## Documented Errors
##
## None
##
## Variable List
##
## j        used to count how many times the loop to draw the sets has been exicuted
## i        used to count how many times the loop to draw the circles has been exicuted
######################################################################
import turtle
for j in range (4):
    for i in range(8):
        turtle.circle(30*(j+1))
        turtle.left(45)
turtle.exitonclick()