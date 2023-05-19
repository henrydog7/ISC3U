def get_info():
    global grade, name
    file_name = open('student.dat', 'r')

    more_lines = True

    while more_lines:
        temp_name = file_name.readline()
        if temp_name != "":
            temp_grade = file_name.readline()

            name.append(temp_name.strip())
            grade.append(int(temp_grade.strip()))
        else:
            more_lines = False

    file_name.close()


def sort_grade():
    for n in range(len(grade) - 1):
        for m in range(len(grade) - 1):
            if grade[m] > grade[m + 1]:
                temp = grade[m]
                grade[m] = grade[m + 1]
                grade[m + 1] = temp

                temp = name[m]
                name[m] = name[m + 1]
                name[m + 1] = temp


def display_info():
    print("Name".ljust(15) + "Grade".rjust(3))
    for n in range(len(grade)):
        print(name[n].ljust(15) + str(grade[n]).rjust(3))


#### main program
import turtle, tkinter

name = []
grade = []
get_info()
sort_grade()
display_info()
