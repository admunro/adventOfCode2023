import re

class Node:

    all_nodes = {}
    def __init__(self, location_string, left_string, right_string):
        self.location = location_string
        self.left = left_string
        self.right = right_string

        Node.all_nodes[self.location] = self

    def get_next_location(self, direction):
        if direction == 'L':
            return self.left
        elif direction == 'R':
            return self.right


def get_input(filename):
    with open(filename) as inputFile:
        raw_input = [(line.strip()) for line in inputFile]

    instructions = raw_input[0]

    nodes = []

    for line in raw_input[2:]:
        matches = re.findall('[A-Z]{3}', line)
        nodes.append(Node(matches[0], matches[1], matches[2]))

    return instructions, nodes



if __name__ == "__main__":

    instructions, nodes = get_input('input.txt')

    current_node = Node.all_nodes['AAA']

    steps = 0

    while current_node.location != 'ZZZ':

        for instruction in instructions:

            next_location = current_node.get_next_location(instruction)
            current_node = Node.all_nodes[next_location]
            steps += 1

            if current_node.location == 'ZZZ':
                break


    print('Answer: ' + str(steps))





