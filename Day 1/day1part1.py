import re
def get_input(filename):
    with open(filename) as rawInput:
        return [(line.strip()) for line in rawInput]


def get_calibration_value(line):
    first_digit = 0
    last_digit = 0

    # First digit
    for character in line:
        if character.isdigit():
            first_digit = character
            break

    # Second digit
    for character in reversed(line):
        if character.isdigit():
            last_digit = character
            break


    value = int(first_digit + last_digit)

    return value


if __name__ == "__main__":

    test_value = 0

    test_value += get_calibration_value('1abc2')
    test_value += get_calibration_value('pqr3stu8vwx')
    test_value += get_calibration_value('a1b2c3d4e5f')
    test_value += get_calibration_value('treb7uchet')

    print("Advent of Code 2023 Day 1, part 1")

    input = get_input('input.txt')

    sum_calibration_values = 0

    for line in input:
        sum_calibration_values += get_calibration_value(line)


    print('The sum of all the calibration values is: ' + str(sum_calibration_values))








