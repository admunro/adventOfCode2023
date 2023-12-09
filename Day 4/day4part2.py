import re

def get_input(filename):
    with open(filename) as rawInput:
        return [(line.strip()) for line in rawInput]



def get_card_number(card):
    return int(re.findall('\d+', card)[0])

def win_cards(card):

    card_number = get_card_number(card)
    winning_numbers = [int(number) for number in re.findall('\d+', card.split('|')[0])[1:]]
    actual_numbers = [int(number) for number in re.findall('\d+', card.split('|')[1])]

    matches = list(set(winning_numbers) & set(actual_numbers))

    new_cards = list(range(card_number + 1, card_number + len(matches) + 1))

    return new_cards



if __name__ == "__main__":

    deck = get_input('input.txt')

    # Initialise each card's number of instances to 1
    card_instances = {card_number + 1: 1 for card_number in range(len(deck))}

    for card in deck:

        card_number = get_card_number(card)
        new_cards = win_cards(card)

        for new_card in new_cards:
            card_instances[new_card] += card_instances[card_number]

    print('Total number of cards: ' + str(sum(card_instances.values())))

