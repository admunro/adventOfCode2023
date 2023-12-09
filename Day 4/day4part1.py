import re

def get_input(filename):
    with open(filename) as rawInput:
        return [(line.strip()) for line in rawInput]


def get_score(gameLine):

    winning_numbers = [int(number) for number in re.findall('\d+', gameLine.split('|')[0])[1:]]
    actual_numbers = [int(number) for number in re.findall('\d+', gameLine.split('|')[1])]

    matches = list(set(winning_numbers) & set(actual_numbers))

    if matches:
        return pow(2, len(matches)-1)
    else:
        return 0


if __name__ == "__main__":

    puzzle_input = get_input('input.txt')

    scores = [get_score(line) for line in puzzle_input]

    print('Sum of all scores: ' + str(sum(scores)))

