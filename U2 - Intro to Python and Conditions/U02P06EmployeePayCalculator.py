name = input("Employee Name: ")
number_of_hours = float(input("Number of Hours: "))
total_sales = float(input("Total Sales:"))

wage_rate = 4.00
commission_rate = 5


def set_department_info():
    print(department_code)
    if department_code == "a" or department_code == "A":
        wage_rate = 4.00
        commission_rate = 5
        department_ok = True
    elif department_code == "b" or department_code == "B" or department_code == "c" or department_code == "C":
        wage_rate = 4.50
        commission_rate = 7
        department_ok = True
    elif department_code == "d" or department_code == "D" or department_code == "e" or department_code == "E":
        wage_rate = 5.00
        commission_rate = 10
        department_ok = True
    elif department_code == "f" or department_code == "F":
        wage_rate = 5.00
        commission_rate = 13
        department_ok = True
    else:
        print("not department code try again")
        department_ok = False

    return department_ok


exit = False

while exit == False:
    department_code = input("Department Code: ")
    if set_department_info() == True:
        exit = True




commision = total_sales*commission_rate/100
wages = number_of_hours*wage_rate
gross_pay = commision + wages
print("name:",name.ljust(10))
print("Number of Hours:", number_of_hours)
print("Total_Sales:", total_sales)
print("Department Code:", department_code)
print("Wages pe Hour:", wage_rate)
print("commission rate:", commission_rate+"%")
print("commisin:",commision)
print(wages)
print(gross_pay)
