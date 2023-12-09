import re
import math

def get_input(filename):
    with open(filename) as rawInput:
        return [(line.strip()) for line in rawInput]

if __name__ == "__main__":

    input = get_input('input.txt')

    time = int(re.sub(' +', '', input[0])[5:])
    distance_to_beat = int(re.sub(' +', '', input[1])[9:])

    possibilities = []

    winning_distances = []

    for button_time in range(1, time):

        remaining_time = time - button_time

        distance_travelled = button_time * remaining_time

        if distance_travelled > distance_to_beat:
            winning_distances.append(distance_travelled)


    print('Answer: ' + str(len(winning_distances)))
