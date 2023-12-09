import re
def get_input(filename):
    with open(filename) as rawInput:
        return [(line.strip()) for line in rawInput]


def extract_first_digit(line):

    first_digit = re.findall(regex, line.lower())[0]

    if first_digit.isdigit():
        return first_digit

    return string_to_int[first_digit]

def extract_last_digit(line):

    for index in range(len(line) - 1, -1, -1):

        test_string = line[index:]
        match = re.findall(regex, test_string)

        if len(match) != 0:

            second_digit = match[0]

            if second_digit.isdigit():
                return second_digit
            else:
                return string_to_int[second_digit]

    return None




def get_calibration_value(line):

    first_digit = extract_first_digit(line)
    second_digit = extract_last_digit(line)

    return_value = first_digit + second_digit

    return int(return_value)

def sum_calibration_values(input):
    calibration_values = {}

    for line in input:
        calibration_values[line] = get_calibration_value(line)

    return sum(calibration_values.values())


regex = "\d|one|two|three|four|five|six|seven|eight|nine"
string_to_int = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

if __name__ == "__main__":

    print("Advent of Code 2023 Day 1, part 2")

    test_input = ['two1nine',
                  'eightwothree',
                  'abcone2threexyz',
                  'xtwone3four',
                  '4nineeightseven2',
                  'zoneight234',
                  '7pqrstsixteen']

    print('Test value: ' + str(sum_calibration_values(test_input)) + '\n')

    print('The sum of all the calibration values is: ' + str(sum_calibration_values(get_input('input.txt'))))
