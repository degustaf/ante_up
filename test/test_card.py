import pytest

from ante.card import create_card, card_value

def test_valid_create_card():
    card = create_card('9C')
