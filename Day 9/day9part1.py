def get_input(filename):
    with open(filename) as inputFile:
        raw_input = [(line.strip()) for line in inputFile]

    parsed_input = []

    for line in raw_input:
        parsed_input.append([int(value) for value in line.split()])

    return parsed_input


def reduce(input):

    results = [input]

    while True:

        differences = []
        for index, number in enumerate(results[-1][1:]):
            differences.append(number - results[-1][index])

        results.append(differences)

        if differences.count(0) == len(differences):
            break

    return results


def extrapolate_next_value(line):

    tree = reduce(line)

    tree.reverse()

    extrapolated_values = []

    for index, sequence in enumerate(list(tree[1:])):
        new_value = sequence[-1] + tree[index][-1]
        extrapolated_values.append(new_value)
        tree[index + 1].append(new_value)

    return tree[-1][-1]


if __name__ == "__main__":

    next_values = [extrapolate_next_value(line) for line in get_input('input.txt')]

    result = sum(next_values)
    print('Answer: ' + str(result))