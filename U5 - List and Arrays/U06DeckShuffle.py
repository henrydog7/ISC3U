# Card Shuffling Program
# J. Osborne
# Created: October 14, 2020
# Modified:

# Documented Errors
# None

# Variable List
# SUIT[]            the posible suits for the cards
# CARD[]            the possible values for the cards
# deck_suit[]       the suit of the card in the deck
# deck_card[]       the value of the card in the deck


#############################################
# The initialize_deck function will create a deck of 52 cards that contatins
# the 13 cards for each of the four suits.
#############################################
def initialize_deck():
    global deck_suit, deck_card

    for s in range(4):
        for c in range(13):
            deck_card.append(CARD[c])
            deck_suit.append(SUIT[s])

#############################################
# The display_deck function will print each card in the deck from the top to
# the bottom.
#############################################


def display_deck():
    global deck_suit, deck_card

    for c in range(52):
        print(deck_suit[c], end="    ")
        print(deck_card[c])


#############################################
# The shuffle_deck function will mix up the cards in the deck by selecting two
# random positions in the deck and switching the cards at these positions.
# This process is repeated 100 times so the deck will be mixed up.
#
# Variable List
# temp_card     used to keep a copy of the card from the first position
# temp_suit     used to keep a copy of the suit from the first position
# pos_1         the first position in the array to be switched
# pos_2         the second position in the array to be switched
#############################################
def shuffle_deck():
    global deck_suit, deck_card

    pos_1 = random.randint(0, 51)
    pos_2 = random.randint(0, 51)

# main program

import random

SUIT = ["Clubs", "Spades", "Hearts", "Diamonds"]
CARD = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

deck_suit = []
deck_card = []

initialize_deck()
display_deck()
shuffle_deck()
display_deck()
