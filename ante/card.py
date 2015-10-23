"""
Module to contain Card class that implements a standard playing card from a
deck of 52 cards.
"""
import collections

Card = collections.namedtuple('Card', ['value', 'suit'])
SUITS = {'CDHS'}
VALUES = {str(x): x for x in range(2, 10)}
VALUES.update({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14})


def create_card(card_code):
    """
    Create card instance based on value of card_code.
    """
    if len(card_code) != 2:
        raise ValueError("{} is an invalid card".format(card_code))
    new_card = Card(list(card_code.upper()))

    if new_card.value not in VALUES:
        raise ValueError("{} is an invalid card value".format(new_card.value))
    if new_card.suit not in SUITS:
        raise ValueError("{} is an invalid suit".format(new_card.suit))

    return new_card


def card_value(card_instance):
    """
    Assign a value to a card so that a hand can be sorted to test for a
    straight.
    """
    if not isinstance(card_instance, 'Card'):
        raise TypeError("'card_value' is expecting an object of type 'Card'")

    return VALUES[card_instance.value]
