"""
Tests functions from ante/card.py
"""
import pytest

from ante.card import create_card, card_value, Card


def test_valid_create_card():
    """
    Test if a card that should be created by create_card is created properly
    """
    card = create_card('9C')
    assert type(card) is Card
    assert card.suit == 'C'
    assert card.value == '9'


def test_invalid_create_card_value():
    """
    Test if passing an invalid string raises a ValueError
    """
    with pytest.raises(ValueError):
        card = create_card('hjnmv')


def test_invalid_create_card_type():
    """
    Test if passing something other than a string raises a type error
    """
    with pytest.raises(TypeError):
        card = create_card((9, 'C'))

# if __name__ == "__main__":
#     test_valid_create_card()
#     test_invalid_create_card_value()
#     test_invalid_create_card_type()
