"""
Module to contain Card class that implements a standard playing card from a
deck of 52 cards.
"""
import collections

Card = collections.namedtuple('Card', ['value', 'suit'])
SUITS = {'CDHS'}
VALUES = ('ATJQK', range(2, 10))


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
