from enum import IntEnum
from enum import auto
from collections import Counter


class Type(IntEnum):
    
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIR = auto()
    THREE_OF_A_KIND = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    FIVE_OF_A_KIND = auto()

card_strengths = { 'A': 13,
                   'K': 12,
                   'Q': 11,
                   'T': 10,
                   '9': 9,
                   '8': 8,
                   '7': 7,
                   '6': 6,
                   '5': 5,
                   '4': 4,
                   '3': 3,
                   '2': 2,
                   'J': 1 }



class Hand:

    def get_type(hand):

        c = Counter(hand.cards)
        jokers = hand.cards.count('J')

        if len(c) == 1:
            return Type.FIVE_OF_A_KIND

        elif len(c) == 2 and 4 in list(c.values()):
            if jokers in [1, 4]:
                return Type.FIVE_OF_A_KIND

            return Type.FOUR_OF_A_KIND

        elif 3 in list(c.values()) and 2 in list(c.values()):
            if jokers in [2, 3]:
                return Type.FIVE_OF_A_KIND

            return Type.FULL_HOUSE

        elif 3 in list(c.values()) and len(c) == 3:
            if jokers in [1, 3]:
                return Type.FOUR_OF_A_KIND

            return Type.THREE_OF_A_KIND

        elif list(c.values()).count(2) == 2:
            if jokers == 1:
                return Type.FULL_HOUSE
            elif jokers == 2:
                return Type.FOUR_OF_A_KIND

            return Type.TWO_PAIR

        elif list(c.values()).count(2) == 1:
            if jokers in [1, 2]:
                return Type.THREE_OF_A_KIND

            return Type.ONE_PAIR

        elif len(c) == 5:
            if jokers == 1:
                return Type.ONE_PAIR

            return Type.HIGH_CARD
        else:
            raise 'Unknown card type'

    def __init__(self, cards, bidstring='0'):
        self.cards = cards
        self.type = Hand.get_type(self)
        self.bid = int(bidstring)

    def __eq__(self, other):
        return self.cards == other.cards

    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        else:
            for position, card in enumerate(self.cards):
                if card == other.cards[position]:
                    continue

                return card_strengths[card] < card_strengths[other.cards[position]]

        return False


def get_input(filename):
    with open(filename) as rawInput:
        return [(line.strip()) for line in rawInput]

if __name__ == "__main__":

    puzzle_input = get_input('input.txt')

    hands = []

    for line in puzzle_input:
        hands.append(Hand(line.split(' ')[0], line.split(' ')[1]))

    hands.sort()

    result = sum([card.bid * (rank+1) for rank, card in enumerate(hands)])

    print('Answer: ' + str(result))
