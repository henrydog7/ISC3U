######################################################################
## Temperature Conversion Porgram
##
## Lucas Balog
## Creating Date: Sep 22, 2020
## Modify Date: N/A
##
## File Name: U02P01TempConvert.py
## Other Files: none
##
## Program Description
##
## This program take the input of a temperature in celcius, converts to farenheit,
## and reports to user
##
##
## Documented Errors
##
## inputting any not numeric characters causes crash
## anything other then "n", "no", "No", or "NO" will casue program to reapeat
##
## Variable List
## temp_c          temperature in celcuis enter from the key board
## temp_f          temperature in farenheit 
## ask_repeat      holds users awnser to if they would like to restart or exit program

######################################################################

while True:
#input
    temp_c = round(float(input("what is the temperature in Celcuis? ")),2)

#proccessing
    temp_f = round((temp_c*9/5+32),2)

#output
    print (temp_c,"degrees Celcius is", temp_f, "degrees Farenheit")

#exit or restart request
    ask_repeat = input("would you like to restart?y/n: ")
    if ask_repeat == "n" or ask_repeat == "no" or ask_repeat == "No" or ask_repeat == "NO":
        break
   
print ("end")
