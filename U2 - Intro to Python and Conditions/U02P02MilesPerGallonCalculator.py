######################################################################
## Temperature Conversion Porgram
##
## Lucas Balog
## Creating Date: Sep 22, 2020
## Modify Date: N/A
##
## File Name: U02P02MilesPerGallonCalculator.py
## Other Files: none
##
## Program Description
##
## The program converts Kilometers to miles and Liters to Gallons
## It then calculates miles per gallon
##
##
## Documented Errors
##
## inputting any not numeric characters causes crash
## anything other then "n", "no", "No", or "NO" will casue program to reapeat
## 
##
## Variable List
## kilometers           remembers the amout of kilometers input by the user
## liters               remembers the amount of liters input by the userS
## miles                remembers the amout of miles after calucaltion
## gallons              remembers the amout of gallons after calucaltion
## miles_per_gallon     remembers the amout of miles per gallon after calucaltion
## ask_repeat      holds users awnser to if they would like to restart or exit program

######################################################################

while True:
#input
    kilometers = float(input("what is the amount of kilometers: "))
    liters = float(input("what is the amount of liters: "))

#proccessing
    gallons = liters/3.6368
    miles = kilometers/1.6
    miles_per_gallon = miles/gallons

#output

    print ("\nKilometers:", end =" ")
    print ('{0:19.2f}'.format(kilometers))
    print ("Liters:", end =" ")
    print ('{0:23.2f}'.format(liters))
    print ("\nMiles:", end =" ")
    print ('{0:24.2f}'.format(miles))
    print ("Gallons:", end =" ")
    print ('{0:22.2f}'.format(gallons))
    print ("\nMiles / Gallon", end =" ")
    print ('{0:16.2f}'.format(miles_per_gallon))

#exit or restart request
    ask_repeat = input("would you like to restart?y/n: ")
    if ask_repeat == "n" or ask_repeat == "no" or ask_repeat == "No" or ask_repeat == "NO":
        break

    
print ("end")
