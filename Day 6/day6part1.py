import re
import math

def get_input(filename):
    with open(filename) as rawInput:
        return [(line.strip()) for line in rawInput]

if __name__ == "__main__":

    input = get_input('input.txt')

    times = [int(time) for time in re.sub(' +', ' ', input[0]).split(' ')[1:]]
    distances = [int(distance) for distance in re.sub(' +', ' ', input[1]).split(' ')[1:]]

    possibilities = []

    for race, time in enumerate(times):
        distance_to_beat = distances[race]
        winning_distances = []

        for button_time in range(1, time):

            remaining_time = time - button_time

            distance_travelled = button_time * remaining_time


            if distance_travelled > distance_to_beat:
                winning_distances.append(distance_travelled)

        possibilities.append(len(winning_distances))


    print('Answer: ' + str(math.prod(possibilities)))


