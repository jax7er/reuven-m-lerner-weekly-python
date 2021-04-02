from enum import IntEnum, auto
from dataclasses import dataclass
from random import sample

class CardValue(IntEnum):
    ACE = 1
    TWO = auto()
    THREE = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()

    def __str__(self):
        return str(self.value)

class CardSuit(IntEnum):
    DIAMONDS = auto()
    HEARTS = auto()
    CLUBS = auto()
    SPADES = auto()

    def __str__(self):
        return self.name.title()

@dataclass
class Card:
    value: CardValue
    suit: CardSuit

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    def __gt__(self, other):
        return self.value > other.value or self.suit > other.suit

    def __str__(self):
        return f"{self.value} of {self.suit}"

deck = [Card(value, suit) for suit in CardSuit for value in CardValue]

cards = sample(deck, k=5)

print(*map(str, cards), sep="\n")