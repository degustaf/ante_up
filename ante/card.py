"""
Module to contain Card class that implements a standard playing card from a
deck of 52 cards.
"""

class Card:
    """
    Class for cards.  Takes a 2 character string and converts it to a suit and
    value.
    """

    Suits = {'C': 'Clubs', 'D': 'Diamonds', 'H': 'Hearts', 'S': 'Spades'}

    def __init__(self, card_code):
        """
        Convert card_code into instance variables.
        """
        self.suit = self.Suits[card_code[1].upper()]
