######################################################################
## Square Art Program
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
## Program draws a continuous square with 89 degree angles so no square encoloses
## a total of 11 almost squares are draw with side clolours alternating between 
## red and green
##
## Documented Errors
##
## None
##
## Variable List
##
## i            used to calculate how many times the loop has been exicuted
######################################################################

import turtle
turtle.speed(0)
turtle.pensize(2)
for i in range (22):
    turtle.right(89)
    turtle.color("GreenYellow")
    turtle. forward(200)
    turtle.right(89)
    turtle.color("red")
    turtle.forward(200)
turtle.exitonclick()