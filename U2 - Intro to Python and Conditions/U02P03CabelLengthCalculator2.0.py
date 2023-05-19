######################################################################
## Temperature Conversion Porgram
##
## Lucas Balog
## Creating Date: Sep 22, 2020
## Modify Date: Sep 23, 2020
##
## File Name: U02P03CabelLengthCalculator2.0.py
## Other Files: none
##
## Program Description
##
## This Program will calculate the legth of cable required to support a pole
## perpendicular to the ground
## Program requires the input of the length of the pole and the distance from the base of
## the pole where the cabel is sucured
##
##
## Documented Errors
##
## inputting any not numeric characters causes crash
## anything other then "n", "no", "No", or "NO" will casue program to reapeat
## 
##
## Variable List
## height           holds the height of a pole
## distance         holds the distance from base of the pole
## cabel_length     holds the length of the cabel required
## ask_repeat       holds users awnser to if they would like to restart or exit program

######################################################################

import math

while True:
#input
    height = float(input("what is the Height of the pole?:"))
    distance = float(input("what is the distance from the base of the pole?:"))                 

#proccessing
    
    cabel_length = round((math.sqrt(height**2+distance**2)),2)

#output
    print ("Height:".rjust(15),end =" ")
    print ('{0:10.2f}'.format(height))
    print ("Distance:".rjust(15),end =" ")
    print ('{0:10.2f}'.format(distance))
    print ("Cabel Length:".rjust(15),end =" ")
    print ('{0:10.2f}'.format(cabel_length))


#exit or restart request 
    ask_repeat = input("would you like to restart?y/n: ")
    if ask_repeat == "n" or ask_repeat == "no" or ask_repeat == "No" or ask_repeat == "NO":
        break

    
print ("end")
