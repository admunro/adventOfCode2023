import re

def get_input(filename):
    with open(filename) as rawInput:
        return [(line.strip()) for line in rawInput]

def number_left(gear, text):

    numbers = re.finditer('\d+', text[gear['row']])

    for number in numbers:
        if number.span()[1] == gear['column']:
            return [int(number.group())]

    return []

def number_right(gear, text):

    numbers = re.finditer('\d+', text[gear['row']])

    for number in numbers:
        if number.span()[0] == gear['column'] + 1:
            return [int(number.group())]

    return []


def check_x_coordinate(match, x):

    coords = list(range(match[0], match[1]))
    return x in coords or (x+1) == coords[0] or (x-1) == coords[-1]


def number_above(gear, text):

    if gear['row'] == 0:
        return []

    return [int(match.group()) for match in re.finditer('\d+', text[gear['row'] - 1]) if check_x_coordinate(match.span(), gear['column'])]


def number_below(gear, text):

    if gear['row'] == len(text) - 1:
        return []

    return [int(match.group()) for match in re.finditer('\d+', text[gear['row'] + 1]) if check_x_coordinate(match.span(), gear['column'])]



if __name__ == "__main__":

    input = get_input('input.txt')

    all_gears = []

    for row, line in enumerate(input):

        for gear in re.finditer('\\*', line):
            all_gears.append({'column': gear.span()[0], 'row': row})


    gear_ratios = []

    for gear in all_gears:
        adjacent_numbers = []

        adjacent_numbers.extend(number_left(gear, input))
        adjacent_numbers.extend(number_right(gear, input))
        adjacent_numbers.extend(number_above(gear, input))
        adjacent_numbers.extend(number_below(gear, input))

        if len(adjacent_numbers) == 2:
            gear_ratios.append(adjacent_numbers[0] * adjacent_numbers[1])


    print('Answer: ' + str(sum(gear_ratios)))