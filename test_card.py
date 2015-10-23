import pytest

from ante.card import create_card, card_value, Card

def test_valid_create_card():
    card = create_card('9C')
    assert type(card) is Card
    assert card.suit == 'C'
    assert card.value == '9'

def test_invalid_create_card_value():
    with pytest.raises(ValueError):
        card = create_card('hjnmv')

def test_invalid_create_card_type():
    with pytest.raises(TypeError):
        card = create_card((9,'C'))

if __name__ == "__main__":
    test_valid_create_card()
    test_invalid_create_card_value()
    test_invalid_create_card_type()
