######################################################################
# Card Generator Program
#
# Lucas Balog
# Creating Date: Sep 24, 2020
# Modify Date: N/A
#
# File Name: U02P04Cards.py
# Other Files: none
#
# Program Description
#
# Program randomly generates a number between 2 and 14
# based on the number determines which card is reported to the user
#
#
# Documented Errors
#
#
#
# Variable List
# card_number       number randomly generated
# card              name of card onece translated from number

######################################################################

import random

card_number = random.randint(2,14)

if card_number < 11:
    card = str(card_number)
elif card_number == 11:
    card = "Jack"
elif card_number == 12:
    card = "Queen"
elif card_number == 13:
    card = "King"
elif card_number == 14:
    card = "Ace"
print("Your card is:", card)