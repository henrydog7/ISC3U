import turtle
import time

#Set up the turtle features
turtle.title ("Turtle Commands Example 2")
turtle.shape("circle")
turtle.shapesize(1)
turtle.speed(1)

#draw the outer circle to represent an eye
turtle.color("blue")
turtle.begin_fill()
turtle.circle(10,-180)
turtle.end_fill()

time.sleep(1)

#draw the pupil of the eye
turtle.hideturtle()
turtle.pencolor("white")
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.exitonclick()
