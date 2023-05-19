######################################################################
# Card Generator Program
#
# Lucas Balog
# Creating Date: Sep 24, 2020
# Modify Date: N/A
#
# File Name: U02P05Department.py
# Other Files: none
#
# Program Description
#
# Proogram calclulates an employees pay based on total sales, hours works, and department
# as for input of employeee name, total sales, total hours, and depeartment code
# depeartment A has a commsion rate of 5% and pay per hour pf 4.00$
# depeartment B and C have a commsion rate of 7% and pay per hour pf 4.50$ 
# depeartment D and E have a commsion rate of 10% and pay per hour pf 5.00$ 
# depeartment F has a commsion rate of 13% and pay per hour pf 5.00$
# reparts employeee name, total sales, total hours, depeartment code,
# commison rate, pay per hours (wage rate), commsion, wages, and gross pay
#
#
# Documented Errors
# 
# program crashes if letter in entered for total hours or total sales
#
#
# Variable List
# wage_rate                 the rate per hour employee is payed per hour
# commission_rate           the percntage of sales employees earn as commision
# name                      the name of the employee
# number_of_hours           the total numbe rof hours the employee has worked
# total_sales               the total amount in sales the employee has made
# exit_loop                 boolean variable to determin if the loop determaning the department code should be broken
######################################################################

######################################################################
## set_department_code function
## 
##  fuctnion sets the wage rate and commision rate for the progrm to calculate
##  returns true when the entered character is a department
##  returns false when the entered character is not a department
##
##  Variable List
##  N/A
######################################################################
def set_department_info():
    global wage_rate
    global commission_rate
    if department_code == "a" or department_code == "A":
        wage_rate = 4.00
        commission_rate = 5
        return True
    elif department_code == "b" or department_code == "B" or department_code == "c" or department_code == "C":
        wage_rate = 4.50
        commission_rate = 7
        return True
    elif department_code == "d" or department_code == "D" or department_code == "e" or department_code == "E":
        wage_rate = 5.00
        commission_rate = 10
        return True
    elif department_code == "f" or department_code == "F":
        wage_rate = 5.00
        commission_rate = 13
        return True
    else:
        print("not department code try again")
        return False

#start of program

wage_rate = 4.00
commission_rate = 5

#input

name = input("Employee Name: ")
number_of_hours = float(input("Number of Hours: "))
total_sales = float(input("Total Sales:"))

#processing

exit_loop = False

while exit_loop == False:
    department_code = input("Department Code: ")
    if set_department_info() == True:
        exit_loop = True

commision = total_sales*commission_rate/100
wages = number_of_hours*wage_rate
gross_pay = commision + wages

#output

print("\n\n\n")
print("Name:".rjust(17), name.rjust(15))
print("Number of Hours:".rjust(17), '{0:15.2f}'.format(number_of_hours))
print("Total Sales:". rjust(17), '{0:15.2f}'.format(total_sales)+"$")
print("Deatment Code:".rjust(17), department_code.rjust(15))
print("Wage Rate".rjust(17), '{0:15.2f}'.format(wage_rate)+"$")
print("Commision Rate:".rjust(17), '{0:15.2f}'.format(commission_rate)+"%")

print("\n")
print("Commision:".rjust(17), '{0:15.2f}'.format(commision)+"$")
print("Wages:".rjust(17), '{0:15.2f}'.format(wages)+"$")
print("----------------------------------------")
print("Gross Pay".rjust(17), '{0:15.2f}'.format(gross_pay)+"$")
