my_file = open('newlist.dat',  'w')

name = "z"
while name != "q":
    name = input("enter a name")
    if name != "q":
        grade = input("enter a grade")

        my_file.write(name + "\n")
        my_file.write(grade + "\n")

my_file.close()
