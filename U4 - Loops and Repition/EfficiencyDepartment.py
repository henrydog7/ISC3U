########################################
# Department Program

# Mr. Osborne
# Creation date: Sept. 21, 2020
# Modified date: Sept. 29, 2020

# EfficiencyDepartment.py
# other files: none

# The program will determine the gross pay for an employee based on the department
# they work in

# Documented Errors
# 


# Variable List
# department        department the employee belongs to.
# hours	            number of hours an employee works in a week
# sales         	amount of the sales by an employee in a week.
# wage          	hourly rate a an employee is paid for hourly work
# rate          	commission rate an employee is paid for sales in decimal form
# reg_pay       	pay the employee earns for hourly work
# commission 	    pay the employee earns for the commission on their sales
# gross_pay     	total pay for the employee

########################################

########################################
# The get_department() function will receive the department entry from the user and
# change it to upper case to simply checking. If an invalid department is entered,
# the wage and rate will be set to 0. Otherwise, the wage and rate be be assigned
# values based on the department.
########################################
def get_department():
    global department, wage, rate
    not_valid = True

    while not_valid:
        department = input("Enter the department of the employee: ")
        department = department.upper()
        if department == "A" or department == "B":
            wage = 12
            rate = 0.04
            not_valid = False
        elif department == "C":
            wage = 15
            rate = 0.03
            not_valid = False
        elif department == "D" or department == "E":
            wage = 15
            rate = 0.05
            not_valid = False
        else:
            print("\n Invalid department entry! \n")


########################################
# The get_hours() function will have the number of hours entered by the user.
# If an invalid number of hours is entered, the hours are reset to 0 for the
# calculation of pay
########################################

def get_hours():
    global hours
    not_valid = True

    while not_valid:
        hours = input("Enter the # of hours worked by the employee: ")
        try:
            hours = float(hours)
            if hours < 0:
                print ("\n Hours must be a positive value. \n")
            elif hours > 80:
                print ("\n The maximum number of hours that can be worked in a week is 80. \n")
            elif hours % 0.25 != 0:
                print ("\n The number of hours must be based on quarter hours. \n")
            else:
                not_valid = False
        except ValueError:
            print ("That is not a number please try again.")

########################################
# The get_sales() function will have the amount in sales entered by the user.
# If an invalid sales value is entered, the sales are reset to 0 for the
# calculation of pay
########################################

def get_sales():
    global sales
    not_valid = True

    while not_valid:
        sales = input("Enter the amount of sales for the employee: ")
        try:
            sales = float(sales)
            if sales < 0:
                print ("\n Sales must be a positive value. \n")
            elif sales > 1000000:
                print ("\n The maximum amount for sales is $1 000 000. \n")
            else:
                not_valid = False
        except ValueError:
            print ("That is not a number please try again")


########################################
# The calc_pay() function will determine the regular pay, commission and gross
# pay.
########################################
def calc_pay():
    global department, hours, wage, sales, reg_pay, commission, gross_pay
    reg_pay = hours * wage
    commission = sales * rate
    gross_pay = reg_pay + commission

########################################
# The display_pay() function will display the regular pay, commission and gross
# pay so it is aligned by play value for the pay and the labels all have the $
# aligned.
########################################
def display_pay():
    global reg_pay, commission, gross_pay
    print ("Regular Pay: $" , end = " ")
    print ('{0:8.2f}'.format(reg_pay))
    print (" Commission: $",end = " ")
    print ('{0:8.2f}'.format(commission))
    print ("  Gross Pay: $",end = " ")
    print ('{0:8.2f}'.format(gross_pay))

########################################
# The ask_repeat() function will ask the user if they would like to repeat
# if the string they enter begins with the letter n the function returns False
# anything else the function will return True.
########################################

def ask_repeat():
    awnser = input("Would you like to start again? (Y/N):").upper()
    if awnser[0] == "N":
        return False
    else:
        return True

# main program

repeat_program = True

while repeat_program:
    global department, hours, wage, sales, reg_pay, commission, gross_pay

    get_department()
    get_hours()
    get_sales()
    
    calc_pay()

    display_pay()

    repeat_program = ask_repeat()              