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

card_strengths = { 'A' : 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1 }



class Hand:

    def get_type(hand):

        c = Counter(hand.cards)

        if len(c) == 1:
            return Type.FIVE_OF_A_KIND
        elif len(c) == 2 and 4 in list(c.values()):
            return Type.FOUR_OF_A_KIND
        elif 3 in list(c.values()) and 2 in list(c.values()):
            return Type.FULL_HOUSE
        elif 3 in list(c.values()) and len(c) == 3:
            return Type.THREE_OF_A_KIND
        elif list(c.values()).count(2) == 2:
            return Type.TWO_PAIR
        elif list(c.values()).count(2) == 1:
            return Type.ONE_PAIR
        elif len(c) == 5:
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


_AAAAA = Hand('AAAAA')
_AA8AA = Hand('AA8AA')
_23332 = Hand('23332')
_TTT98 = Hand('TTT98')
_23432 = Hand('23432')
_A23A4 = Hand('A23A4')
_23456 = Hand('23456')

_32T3K = Hand('32T3K',  '765')
_T55J5 = Hand('T55J5',  '684')
_KK677 = Hand('KK677',  '28')
_KTJJT = Hand('KTJJT',  '220')
_QQQJA = Hand('QQQJA',  '483')

_3275Q = Hand('3275Q')
_286K4 = Hand('286K4')


def get_input(filename):
    with open(filename) as rawInput:
        return [(line.strip()) for line in rawInput]

if __name__ == "__main__":

    puzzle_input = get_input('input.txt')

    assert _286K4 < _3275Q

    hands = []

    for line in puzzle_input:
        hands.append(Hand(line.split(' ')[0], line.split(' ')[1]))

    hands.sort()

    result = sum([card.bid * (rank+1) for rank, card in enumerate(hands)])

    print('Answer: ' + str(result))
