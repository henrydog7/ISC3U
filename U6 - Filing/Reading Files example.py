def setup():
    window = turtle.Screen()
    window.setup(600, 600, 0, 0)
    turtle.speed(0)
    turtle.color("blue")


def get_info():
    global x, y
    file_name = open('diamond.dat', 'r')

    more_lines = True
    while more_lines:
        line = file_name.readline()
        if line != "":
            line = int(line)
            print(line)
            x.append(line)

            line = file_name.readline()
            line = int(line)
            print(line)
            y.append(line)
        else:
            more_lines = False

    file_name.close()


def draw_shape():
    for n in range(len(x)):
        turtle.goto(x[n], y[n])


#### main program
import turtle, tkinter

x = []
y = []
setup()
get_info()
draw_shape()

turtle.exitonclick()
