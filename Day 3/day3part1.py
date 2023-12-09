import re
def get_input(filename):
    with open(filename) as rawInput:
        return [(line.strip()) for line in rawInput]

def is_symbol(character):
    return not(character.isdigit()) and not(character == '.')

def get_symbols(text):
    return set([character for line in text for character in line if is_symbol(character)])


def get_numbers(line):
    return re.finditer('\d+', line)


def get_surrounding_characters(row, column, text):

    rows = len(text)
    columns = len(text[0]) # Input assumed to be rectangular!

    surrounding_characters = []

    edge = {'topRow': row == 0,
            'bottomRow': row == len(text) - 1,
            'leftColumn': column == 0,
            'rightColumn': column == len(text[0]) - 1}

    # Above
    if not edge['topRow']:
        surrounding_characters.append(text[row - 1][column])

    # Below
    if not edge['bottomRow']:
        surrounding_characters.append(text[row + 1][column])

    # Left
    if not edge['leftColumn']:
        surrounding_characters.append(text[row][column - 1])

    # Right
    if not edge['rightColumn']:
        surrounding_characters.append(text[row][column + 1])

    # Top Left
    if not edge['topRow'] and not edge['leftColumn']:
        surrounding_characters.append(text[row - 1][column - 1])

    # Top Right
    if not edge['topRow'] and not edge['rightColumn']:
        surrounding_characters.append(text[row - 1][column + 1])

    # Bottom Left
    if not edge['bottomRow'] and not edge['leftColumn']:
        surrounding_characters.append(text[row + 1][column - 1])

    # Bottom Right
    if not edge['bottomRow'] and not edge['rightColumn']:
        surrounding_characters.append(text[row + 1][column + 1])

    return surrounding_characters


if __name__ == "__main__":

    input = get_input('input.txt')

    symbols = get_symbols(input)

    valid_part_numbers = []

    for row, line in enumerate(input):
        numbers = get_numbers(line)

        for match in numbers:
            surrounding_characters = []

            for char in range(match.span()[0], match.span()[1]):
                surrounding_characters.extend(get_surrounding_characters(row, char, input))

            if symbols.intersection(set(surrounding_characters)):
                valid_part_numbers.append(int(match.group()))


    print('The sum of the valid part numbers is: ' + str(sum(valid_part_numbers)))